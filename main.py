# Lawan Mai
# Version 1.0
# Main application for webtoon translation

from backend.ocr.paddle_ocr import ocr_and_cluster
from backend.translation.deepl import translate_deepl_batch
from backend.visualization.embed_text import embed_text_in_image


def main():
    # Path to the image
    img_path = ".panels/eldrich.png"
    output_path = ".output/eldrich_translated.png"

    # Perform OCR and clustering
    speech_bubbles = ocr_and_cluster(img_path, treshold=30)

    # Print the results
    # for speech_bubble in speech_bubbles:
    #     print(f"Cluster: {speech_bubble[0]}, Text: {speech_bubble[1]}")

    bubbles = [sb[0] for sb in speech_bubbles]
    texts = [sb[1] for sb in speech_bubbles]
    translated_texts = translate_deepl_batch(texts, source_lang="EN", target_lang="DE")
    speech_bubbles_data = [
        bubble + [text] for bubble, text in zip(bubbles, translated_texts)
    ]

    embed_text_in_image(img_path, speech_bubbles_data, output_path)
    print("done")


if __name__ == "__main__":
    main()
