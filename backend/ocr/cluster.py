# backend/utils/geometry.py
def polygon_to_bbox(polygon):
    """Convert a polygon (list of [x,y] points) into a (x_min, y_min, x_max, y_max) bounding box."""
    x_coords = [point[0] for point in polygon]
    y_coords = [point[1] for point in polygon]
    return (min(x_coords), min(y_coords), max(x_coords), max(y_coords))


def union_of_bboxes(polygon1, polygon2):
    """Create a new bounding box covering both input polygons."""
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


def bboxes_within_x_pixels(polygon1, polygon2, x):
    """Check if two polygons have at least one point within `x` pixels of each other."""
    x1_min, y1_min, x1_max, y1_max = polygon_to_bbox(polygon1)
    x2_min, y2_min, x2_max, y2_max = polygon_to_bbox(polygon2)

    horizontal_close = (x1_max + x >= x2_min) and (x2_max + x >= x1_min)
    vertical_close = (y1_max + x >= y2_min) and (y2_max + x >= y1_min)

    return horizontal_close and vertical_close


def cluster_bounding_boxes(bbox, txts, proximity_threshold=30):
    """
    Cluster bounding boxes and merge their associated text if they are within a proximity threshold.

    Args:
        bbox (list): List of bounding boxes.
        txts (list): List of text corresponding to the bounding boxes.
        proximity_threshold (int): Maximum pixel distance to consider boxes as close.

    Returns:
        list: A list of tuples containing merged bounding boxes and their associated text.
    """
    cluster = []

    while bbox:
        # Start a new cluster with the first bounding box and text
        cluster.append((bbox.pop(0), txts.pop(0)))

        curr_box = cluster[-1][0]
        i = 0

        while i < len(bbox):
            if bboxes_within_x_pixels(curr_box, bbox[i], proximity_threshold):
                # Merge the bounding boxes and texts
                temp_box, temp_txt = cluster.pop()
                cluster.append(
                    (union_of_bboxes(temp_box, bbox[i]), temp_txt + " " + txts[i])
                )
                bbox.pop(i)
                txts.pop(i)
                curr_box = cluster[-1][0]  # Update the current box after merging
            else:
                i += 1  # Only increment if no merge occurred

    return cluster
