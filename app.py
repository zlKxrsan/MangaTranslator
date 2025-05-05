# Lawan Mai
# Version 1.0
# Main application for manga translation

from backend.ocr.paddle_ocr import get_ocr_result
from backend.translation.deepl import translate_deepl_batch
from backend.visualization.embed_text import draw_translations_on_image

def process_image(img_path):
    ocr_results = get_ocr_result(img_path)

    filtered = [(line[0], line[1][0].strip()) for line in ocr_results if line[1][0].strip()]
    if not filtered:
        return []

    boxes, texts = zip(*filtered)
    translations = translate_deepl_batch(texts)

    combined = []
    for box, orig, trans in zip(boxes, texts, translations):
        combined.append({
            "bounding_box": box,
            "original_text": orig,
            "translated_text": trans
        })

    return combined

#TODO: Change dummy results to actual OCR and translation results
if __name__ == "__main__":
    image_name = "panel1.jpg"
    image_path = f".panels/{image_name}"
    output_path = f".output/{image_name}"
    #results = process_image(image_path)


    # Dummy 'results' example to simulate the output from OCR and translation
    dummy_results = [
        {
            "bounding_box": [[100.0, 150.0], [200.0, 150.0], [200.0, 180.0], [100.0, 180.0]],
            "original_text": "こんにちは",
            "translated_text": "Hello"
        },
        {   
            "bounding_box": [[220.0, 160.0], [350.0, 160.0], [350.0, 190.0], [220.0, 190.0]],
            "original_text": "世界",
            "translated_text": "World"
        },
        {
            "bounding_box": [[370.0, 170.0], [500.0, 170.0], [500.0, 190.0], [370.0, 190.0]],
            "original_text": "どうぞ",
            "translated_text": "Please"
        }
    ]

    draw_translations_on_image(image_path, dummy_results, output_path)
