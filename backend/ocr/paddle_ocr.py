# Lawan Mai
# Version 1.0
# Module for text recognition from manga panels using PaddleOCR

from paddleocr import PaddleOCR

def get_ocr_result(img_path):
    ocr = PaddleOCR(use_angle_cls=True, lang='japan')
    result = ocr.ocr(img_path, cls=True)
    return result[0]
