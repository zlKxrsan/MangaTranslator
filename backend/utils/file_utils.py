"""
Utility functions for handling file operations, such as retrieving the first image
from a directory and preparing output paths.
"""

import os
from typing import Tuple, List


def get_first_image_path(
    panel_dir: str = "resources/.panels",
    output_dir: str = "resources/.output",
    image_extensions: Tuple[str, ...] = (".png", ".jpg", ".jpeg", ".webp"),
) -> Tuple[str, str]:
    """
    Retrieve the first image file from the specified directory and prepare the output path.

    Args:
        panel_dir (str): Directory containing the image panels.
        output_dir (str): Directory where the output will be saved.
        image_extensions (Tuple[str, ...]): Supported image file extensions.

    Returns:
        Tuple[str, str]: A tuple containing the input image path and the output image path.

    Raises:
        FileNotFoundError: If no image files are found in the panel directory.
    """
    # Find the first image file in the directory
    try:
        first_image = next(
            f for f in os.listdir(panel_dir) if f.lower().endswith(image_extensions)
        )
    except StopIteration:
        raise FileNotFoundError(f"No image files found in the directory: {panel_dir}")

    # Define paths
    img_path = os.path.join(panel_dir, first_image)

    # Split name and extension
    name, ext = os.path.splitext(first_image)
    output_path = os.path.join(output_dir, f"{name}_translated{ext}")

    return img_path, output_path


def list_image_files(
    directory: str,
    image_extensions: Tuple[str, ...] = (".png", ".jpg", ".jpeg", ".webp"),
) -> List[str]:
    """
    List all image files in the specified directory.

    Args:
        directory (str): Directory to search for image files.
        image_extensions (Tuple[str, ...]): Supported image file extensions.

    Returns:
        List[str]: A list of image file names in the directory.
    """
    return [f for f in os.listdir(directory) if f.lower().endswith(image_extensions)]
