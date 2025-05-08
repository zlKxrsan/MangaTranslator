"""
Module for embedding translated text into images.

This module provides functions to calculate text wrapping, determine font sizes,
and embed text into speech bubbles within images.
"""

from PIL import Image, ImageDraw, ImageFont
from typing import List, Tuple


def get_best_font_size(
    text: str, font_path: str, max_width: int, max_height: int
) -> int:
    """
    Determine the optimal font size to fit the given text within specified dimensions.

    This function uses a binary search approach to find the largest font size
    that allows the text to fit within the provided maximum width and height.
    The text is wrapped to fit within the width, and the total height of the
    wrapped lines is calculated to ensure it does not exceed the maximum height.

    Args:
        text (str): The text to fit within the dimensions.
        font_path (str): Path to the font file to be used.
        max_width (int): The maximum allowable width for the text.
        max_height (int): The maximum allowable height for the text.

    Returns:
        int: The largest font size that fits the text within the specified dimensions.

    Raises:
        OSError: If the font file cannot be loaded.
    """
    min_size, max_size = 4, 100  # Reasonable bounds
    best_size = min_size

    while min_size <= max_size:
        mid = (min_size + max_size) // 2
        font = ImageFont.truetype(font_path, size=mid)
        wrapped = wrap_text(text, font, max_width)

        total_height = sum(
            font.getbbox(line)[3] - font.getbbox(line)[1] for line in wrapped
        )
        max_line_width = max(
            (font.getbbox(line)[2] - font.getbbox(line)[0]) for line in wrapped
        )

        if total_height <= max_height and max_line_width <= max_width:
            best_size = mid
            min_size = mid + 1
        else:
            max_size = mid - 1

    return best_size


def draw_bounding_boxes_and_text_with_pillow(
    image: Image.Image,
    draw: ImageDraw.ImageDraw,
    speech_bubbles_data: List[List],
    font_path: str,
) -> Image.Image:
    """
    Draw bounding boxes and embed text into the image.

    Args:
        image (Image.Image): The image to draw on.
        draw (ImageDraw.ImageDraw): The drawing context.
        speech_bubbles_data (List[List]): List of speech bubble data (bounding boxes and text).
        font_path (str): Path to the font file.

    Returns:
        Image.Image: The modified image with text embedded.
    """
    width, height = image.size
    for bubble in speech_bubbles_data:
        cluster = bubble[:-1]
        text = bubble[-1]

        x_min = int(min(p[0] for p in cluster))
        x_max = int(max(p[0] for p in cluster))
        y_min = int(min(p[1] for p in cluster))
        y_max = int(max(p[1] for p in cluster))

        sample_x = (x_min + x_max) // 2
        sample_y = y_max + 1

        # Get the background color of the pixel below the bounding box
        if 0 <= sample_x < width and 0 <= sample_y < height:
            background_color = image.getpixel((sample_x, sample_y))
        else:
            background_color = (0, 0, 0)  # Default to black if out of bounds

        # Fill the bounding box with a semi-transparent background
        draw.rectangle([x_min, y_min, x_max, y_max], fill=(*background_color[:3], 160))

        # Determine the best font size
        try:
            max_width = x_max - x_min - 10  # Add padding
            max_height = y_max - y_min - 10
            best_size = get_best_font_size(text, font_path, max_width, max_height)
            font = ImageFont.truetype(font_path, size=best_size)
        except IOError:
            font = ImageFont.load_default()

        # Wrap the text and calculate vertical alignment
        wrapped_text = wrap_text(text, font, max_width)
        text_height = sum(
            font.getbbox(line)[3] - font.getbbox(line)[1] for line in wrapped_text
        )
        y_offset = y_min + (max_height - text_height) // 2

        # Calculate luminance to determine text color
        r, g, b = background_color[:3]
        luminance = 0.2126 * r + 0.7152 * g + 0.0722 * b
        text_color = (0, 0, 0) if luminance > 160 else (255, 255, 255)

        # Draw each line of text
        for line in wrapped_text:
            text_width = font.getbbox(line)[2] - font.getbbox(line)[0]
            x_offset = x_min + (max_width - text_width) // 2
            draw.text((x_offset, y_offset), line, font=font, fill=text_color)
            y_offset += font.getbbox(line)[3] - font.getbbox(line)[1]

    return image


def wrap_text(text: str, font: ImageFont.FreeTypeFont, max_width: int) -> List[str]:
    """
    Wrap text into multiple lines to fit within a specified maximum width.

    This function splits the input text into words and iteratively builds lines
    that fit within the given width constraint. If a word causes the current line
    to exceed the maximum width, the line is finalized, and the word starts a new line.

    Args:
        text (str): The text to be wrapped.
        font (ImageFont.FreeTypeFont): The font used to measure the text width.
        max_width (int): The maximum allowable width for each line.

    Returns:
        List[str]: A list of strings, where each string represents a line of wrapped text.
    """
    lines = []
    words = text.split()
    current_line = ""

    for word in words:
        test_line = f"{current_line} {word}".strip()
        bbox = font.getbbox(test_line)
        if bbox[2] - bbox[0] <= max_width:
            current_line = test_line
        else:
            if current_line:
                lines.append(current_line)
            current_line = word

    if current_line:
        lines.append(current_line)

    return lines


def embed_text_in_image(
    image: Image.Image,
    speech_bubbles_data: List[List],
    font_path: str,
) -> Image.Image:
    """
    Embed translated text into an image and save the result.

    Args:
        image_path (str): Path to the input image.
        speech_bubbles_data (List[List]): List of speech bubble data (bounding boxes and text).
        output_path (str): Path to save the output image.
        font_path (str): Path to the font file.

    Returns:
        None
    """

    # Create a drawing context
    draw = ImageDraw.Draw(image)

    # Draw bounding boxes and embed text
    result_image = draw_bounding_boxes_and_text_with_pillow(
        image, draw, speech_bubbles_data, font_path
    )

    # Save the result
    return result_image
