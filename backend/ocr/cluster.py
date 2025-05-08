"""
Utility functions for working with bounding boxes and clustering text regions.

This module provides functions to convert polygons to bounding boxes, merge bounding boxes,
check proximity between bounding boxes, and cluster bounding boxes based on proximity.
"""

from typing import List, Tuple


def polygon_to_bbox(polygon: List[List[float]]) -> Tuple[float, float, float, float]:
    """
    Convert a polygon (list of [x, y] points) into a bounding box.

    Args:
        polygon (List[List[float]]): A list of points representing the polygon.

    Returns:
        Tuple[float, float, float, float]: Bounding box as (x_min, y_min, x_max, y_max).
    """
    x_coords = [point[0] for point in polygon]
    y_coords = [point[1] for point in polygon]
    return min(x_coords), min(y_coords), max(x_coords), max(y_coords)


def union_of_bboxes(
    polygon1: List[List[float]], polygon2: List[List[float]]
) -> List[List[float]]:
    """
    Create a new bounding box that covers both input polygons.

    Args:
        polygon1 (List[List[float]]): First polygon as a list of points.
        polygon2 (List[List[float]]): Second polygon as a list of points.

    Returns:
        List[List[float]]: A new bounding box as a list of points.
    """
    x1_min, y1_min, x1_max, y1_max = polygon_to_bbox(polygon1)
    x2_min, y2_min, x2_max, y2_max = polygon_to_bbox(polygon2)

    new_x_min = min(x1_min, x2_min)
    new_y_min = min(y1_min, y2_min)
    new_x_max = max(x1_max, x2_max)
    new_y_max = max(y1_max, y2_max)

    return [
        [new_x_min, new_y_min],
        [new_x_max, new_y_min],
        [new_x_max, new_y_max],
        [new_x_min, new_y_max],
    ]


def bboxes_within_x_pixels(
    polygon1: List[List[float]], polygon2: List[List[float]], x: float
) -> bool:
    """
    Check if two polygons have at least one point within `x` pixels of each other.

    Args:
        polygon1 (List[List[float]]): First polygon as a list of points.
        polygon2 (List[List[float]]): Second polygon as a list of points.
        x (float): Proximity threshold in pixels.

    Returns:
        bool: True if the polygons are within `x` pixels of each other, False otherwise.
    """
    x1_min, y1_min, x1_max, y1_max = polygon_to_bbox(polygon1)
    x2_min, y2_min, x2_max, y2_max = polygon_to_bbox(polygon2)

    horizontal_close = (x1_max + x >= x2_min) and (x2_max + x >= x1_min)
    vertical_close = (y1_max + x >= y2_min) and (y2_max + x >= y1_min)

    return horizontal_close and vertical_close


def cluster_bounding_boxes(
    bbox: List[List[List[float]]], txts: List[str], proximity_threshold: int = 30
) -> List[Tuple[List[List[float]], str]]:
    """
    Cluster bounding boxes and merge their associated text if they are within a proximity threshold.

    Args:
        bbox (List[List[List[float]]]): List of bounding boxes as polygons.
        txts (List[str]): List of text corresponding to the bounding boxes.
        proximity_threshold (int): Maximum pixel distance to consider boxes as close.

    Returns:
        List[Tuple[List[List[float]], str]]: A list of tuples containing merged bounding boxes and their associated text.
    """
    clusters = []

    while bbox:
        # Start a new cluster with the first bounding box and text
        clusters.append((bbox.pop(0), txts.pop(0)))

        curr_box = clusters[-1][0]
        i = 0

        while i < len(bbox):
            if bboxes_within_x_pixels(curr_box, bbox[i], proximity_threshold):
                # Merge the bounding boxes and texts
                temp_box, temp_txt = clusters.pop()
                clusters.append(
                    (union_of_bboxes(temp_box, bbox[i]), temp_txt + " " + txts[i])
                )
                bbox.pop(i)
                txts.pop(i)
                curr_box = clusters[-1][0]  # Update the current box after merging
            else:
                i += 1  # Only increment if no merge occurred

    return clusters
