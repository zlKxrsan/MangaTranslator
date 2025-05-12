"""
Core application for webtoon translation.

This script performs OCR on webtoon images, translates the extracted text,
and embeds the translated text back into the images.
"""

from PIL import Image
import io

from ocr.paddle_ocr import ocr_and_cluster
from translation.deepl import translate_deepl_batch
from visualization.embed_text import embed_text_in_image
from utils.font_selector import get_font_path_for_language


def process_image(
    img_bytes: bytes = None,
    source_lang: str = "EN",
    target_lang: str = "DE",
    ocr_lang: str = "en",
    threshold=30,
) -> bytes:
    """
    core function to process a webtoon image, translate its text, and embed the translated text back into the image.

    Steps:
    1. Retrieve the first image from the panels directory.
    2. Perform OCR and cluster the detected text.
    3. Translate the clustered text using DeepL.
    4. Embed the translated text into the image and save the output.

    Returns:
        None
    """

    # Load the image from bytes
    image = Image.open(io.BytesIO(img_bytes)).convert("RGB")

    # Get the font path for the target language
    font_path = get_font_path_for_language(target_lang)

    # Perform OCR and cluster the detected text
    speech_bubbles = ocr_and_cluster(image)

    # Extract bounding boxes and texts
    bubbles = [sb[0] for sb in speech_bubbles]
    texts = [sb[1] for sb in speech_bubbles]

    # Translate the extracted texts
    translated_texts = translate_deepl_batch(texts, source_lang, target_lang)

    # Combine bounding boxes with translated texts
    speech_bubbles_data = [
        bubble + [text] for bubble, text in zip(bubbles, translated_texts)
    ]

    # Embed the translated text into the image
    result_image = embed_text_in_image(image, speech_bubbles_data, font_path)

    output = io.BytesIO()
    result_image.save(output, format="PNG")

    return output.getvalue()


if __name__ == "__main__":
    process_image()
