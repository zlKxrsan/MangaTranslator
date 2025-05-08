# Lawan Mai
# Version 2.0
# Module for text recognition from webtoon images using PaddleOCR

from paddleocr import PaddleOCR, draw_ocr
from PIL import Image
import numpy as np
import os
from .cluster import cluster_bounding_boxes


def ocr_and_cluster(lang, img_path, treshold=30):

    # Initialize PaddleOCR
    ocr = PaddleOCR(
        lang=lang,  # use English-only models
        use_angle_cls=True,
        det_model="en_PP-OCRv3_det",
        rec_model="en_PP-OCRv3_rec",
    )

    # Perform OCR
    result = ocr.ocr(img_path, cls=True)[0]

    # Extract bounding boxes and texts
    bbox = [line[0] for line in result]
    txts = [line[1][0] for line in result]

    # Cluster bounding boxes
    clustered_data = cluster_bounding_boxes(bbox, txts)

    return clustered_data
