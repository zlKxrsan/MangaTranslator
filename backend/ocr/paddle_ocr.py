"""
Module for text recognition and clustering from webtoon images using PaddleOCR.

This module provides a function to perform OCR on an image, extract bounding boxes
and text, and cluster the results based on proximity.
"""

from typing import List, Dict, Any
from paddleocr import PaddleOCR
from .cluster import cluster_bounding_boxes
from functools import lru_cache


@lru_cache(maxsize=1)
def get_ocr(lang: str) -> PaddleOCR:
    """
    Initialize PaddleOCR with the specified language and models.
    This function uses memoization to cache the PaddleOCR instance for efficiency.
    Args:
        lang (str): Language code for PaddleOCR (e.g., 'en' for English).
    Returns:
        PaddleOCR: An instance of PaddleOCR initialized with the specified language.
    """
    return PaddleOCR(
        lang=lang,
        use_angle_cls=True,
        det_model="en_PP-OCRv3_det",
        rec_model="en_PP-OCRv3_rec",
    )


def ocr_and_cluster(
    lang: str, img_path: str, threshold: int = 30
) -> List[Dict[str, Any]]:
    """
    Perform OCR on an image and cluster the detected text regions.

    Args:
        lang (str): Language code for PaddleOCR (e.g., 'en' for English).
        img_path (str): Path to the input image.
        threshold (int): Proximity threshold for clustering bounding boxes.

    Returns:
        List[Dict[str, Any]]: A list of clustered bounding boxes and their associated text.
    """
    # Initialize PaddleOCR with the specified language and models
    ocr = get_ocr(lang)

    # Perform OCR on the image
    result = ocr.ocr(img_path, cls=True)[0]

    # Extract bounding boxes and texts from the OCR result
    bbox = [line[0] for line in result]
    txts = [line[1][0] for line in result]

    # Cluster the bounding boxes and associated texts
    clustered_data = cluster_bounding_boxes(bbox, txts, proximity_threshold=threshold)

    return clustered_data
