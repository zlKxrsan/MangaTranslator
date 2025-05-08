# Lawan Mai
# Version 1.0
# Main application for webtoon translation

from backend.ocr.paddle_ocr import ocr_and_cluster
from backend.translation.deepl import translate_deepl_batch
from backend.visualization.embed_text import embed_text_in_image
from backend.utils.font_selector import get_font_path_for_language
from backend.utils.file_utils import get_first_image_path


def main():
    # Path to the image
    img_path, output_path = get_first_image_path()
    ocr_lang = "en"  # paddleocr language code
    source_lang = "EN"  # deepl language code
    target_lang = "DE"  # deepl language code

    font_path = get_font_path_for_language(target_lang)

    # Perform OCR and clustering
    speech_bubbles = ocr_and_cluster(ocr_lang, img_path, treshold=30)

    # Print the results
    # for speech_bubble in speech_bubbles:
    #     print(f"Cluster: {speech_bubble[0]}, Text: {speech_bubble[1]}")

    bubbles = [sb[0] for sb in speech_bubbles]
    texts = [sb[1] for sb in speech_bubbles]
    translated_texts = translate_deepl_batch(texts, source_lang, target_lang)
    speech_bubbles_data = [
        bubble + [text] for bubble, text in zip(bubbles, translated_texts)
    ]

    embed_text_in_image(img_path, speech_bubbles_data, output_path, font_path)
    print("done")


if __name__ == "__main__":
    main()
