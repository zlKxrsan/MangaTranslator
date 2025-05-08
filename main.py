"""
Main application for webtoon translation.

This script performs OCR on webtoon images, translates the extracted text,
and embeds the translated text back into the images.
"""

from backend.ocr.paddle_ocr import ocr_and_cluster
from backend.translation.deepl import translate_deepl_batch
from backend.visualization.embed_text import embed_text_in_image
from backend.utils.font_selector import get_font_path_for_language
from backend.utils.file_utils import get_first_image_path


def main() -> None:
    """
    Main function to process a webtoon image, translate its text, and embed the translated text back into the image.

    Steps:
    1. Retrieve the first image from the panels directory.
    2. Perform OCR and cluster the detected text.
    3. Translate the clustered text using DeepL.
    4. Embed the translated text into the image and save the output.

    Returns:
        None
    """
    # Get the input image path and output path
    img_path, output_path = get_first_image_path()

    # Define language codes
    ocr_lang = "en"  # PaddleOCR language code
    source_lang = "EN"  # DeepL source language code
    target_lang = "DE"  # DeepL target language code
    threshold = 30  # Clustering threshold

    # Get the font path for the target language
    font_path = get_font_path_for_language(target_lang)

    # Perform OCR and cluster the detected text
    speech_bubbles = ocr_and_cluster(ocr_lang, img_path, threshold)

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
    embed_text_in_image(img_path, speech_bubbles_data, output_path, font_path)

    print("Processing complete. Translated image saved to:", output_path)


if __name__ == "__main__":
    main()
