"""
Utility for selecting font paths based on language codes.

This module provides a function to retrieve the appropriate font file path
for a given language code.
"""

import os
from typing import Dict


def get_font_path_for_language(lang_code: str) -> str:
    """
    Retrieve the font file path for the specified language code.

    Args:
        lang_code (str): Language code (e.g., "EN" for English, "DE" for German).

    Returns:
        str: The file path to the font corresponding to the language code.

    Raises:
        ValueError: If no font is mapped for the given language code.
        FileNotFoundError: If the font file does not exist at the specified path.
    """
    font_map: Dict[str, str] = {
        "DE": ".fonts/Bangers/Bangers-Regular.ttf",
        "EN": ".fonts/Bangers/Bangers-Regular.ttf",
        "FR": ".fonts/Bangers/Bangers-Regular.ttf",
        "ES": ".fonts/Bangers/Bangers-Regular.ttf",
        "PT-BR": ".fonts/Bangers/Bangers-Regular.ttf",
        "PL": ".fonts/Bangers/Bangers-Regular.ttf",
        "JA": ".fonts/Noto_Sans_JP/NotoSansJP-VariableFont_wght.ttf",
        "KO": ".fonts/Noto_Sans_KR/NotoSansKR-VariableFont_wght.ttf",
        "ZH": ".fonts/Noto_Sans_SC/NotoSansSC-VariableFont_wght.ttf",  # Simplified Chinese
        "TR": ".fonts/Bangers/Bangers-Regular.ttf",
        "RU": ".fonts/Russo_One/RussoOne-Regular.ttf",
    }

    # Retrieve the font path from the map
    font_path = font_map.get(lang_code.upper())
    if not font_path:
        raise ValueError(f"No matching font found for language code: {lang_code}")

    # Validate the existence of the font file
    if not os.path.isfile(font_path):
        raise FileNotFoundError(f"Font file not found at path: {font_path}")

    return font_path
