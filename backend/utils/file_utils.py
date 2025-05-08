import os


def get_first_image_path(
    panel_dir=".panels",
    output_dir=".output",
    image_extensions=(".png", ".jpg", ".jpeg", ".webp"),
):
    """
    Get the first image file from the specified directory and prepare the output path.

    Args:
        panel_dir (str): Directory containing the image panels.
        output_dir (str): Directory where the output will be saved.
        image_extensions (tuple): Supported image file extensions.

    Returns:
        tuple: A tuple containing the input image path and the output image path.

    Raises:
        FileNotFoundError: If no image files are found in the panel directory.
    """
    # Find all image files in the directory
    panel_files = [
        f for f in os.listdir(panel_dir) if f.lower().endswith(image_extensions)
    ]

    # Raise an error if no image files are found
    if not panel_files:
        raise FileNotFoundError(f"No image files found in the directory: {panel_dir}")

    # Take the first image file
    first_image = panel_files[0]

    # Define paths
    img_path = os.path.join(panel_dir, first_image)

    # Split name and extension
    name, ext = os.path.splitext(first_image)
    output_path = os.path.join(output_dir, f"{name}_translated{ext}")

    return img_path, output_path
