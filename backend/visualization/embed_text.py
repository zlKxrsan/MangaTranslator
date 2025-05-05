# Lawan Mai
# Version 1.0
# Module for visualizing translations in manga images using draw_ocr

from paddleocr import draw_ocr
from PIL import Image
import cv2

def draw_translations_on_image(image_path, results, output_path):
    image = Image.open(image_path).convert("RGB")

    boxes = [item["bounding_box"] for item in results]
    texts = [item["translated_text"] for item in results]

    font_path = ".fonts/Wild-Words-Font-2/CC Wild Words Roman.ttf"

    image_with_boxes = draw_ocr(
        image,
        boxes,
        txts=texts,
        font_path=font_path
    )

    cv2.imwrite(output_path, image_with_boxes)
    print(f"Translated panel saved at: {output_path}")
