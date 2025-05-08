"""
Module for translating text into a target language using the DeepL API.

This module provides a function to batch translate text using the DeepL API,
with options for specifying source and target languages and formality levels.
"""

import requests
from typing import List
from resources.config import DEEPL_API_KEY

DEEPL_API_URL = "https://api-free.deepl.com/v2/translate"


def translate_deepl_batch(
    texts: List[str],
    source_lang: str = "EN",
    target_lang: str = "DE",
    formality: str = "prefer_less",
) -> List[str]:
    """
    Translate a batch of texts using the DeepL API.

    Args:
        texts (List[str]): List of texts to be translated.
        source_lang (str): Source language code (e.g., "EN" for English).
        target_lang (str): Target language code (e.g., "DE" for German).
        formality (str): Formality level for the translation ("default", "prefer_less", "prefer_more").

    Returns:
        List[str]: List of translated texts. If an error occurs, returns a list of error messages.
    """
    if not texts:
        return []

    # Prepare the request payload
    payload = (
        [("auth_key", DEEPL_API_KEY)]
        + [("text", txt) for txt in texts]
        + [
            ("source_lang", source_lang),
            ("target_lang", target_lang),
            ("formality", formality),
        ]
    )

    try:
        # Send the POST request to the DeepL API
        response = requests.post(DEEPL_API_URL, data=payload)
        response.raise_for_status()  # Raise an error for HTTP issues

        # Parse the response JSON
        translations = response.json().get("translations", [])
        return [t["text"] for t in translations]

    except requests.exceptions.RequestException as e:
        # Handle HTTP-related errors
        print(f"[HTTP error: {e}]")
        return ["[HTTP error]"] * len(texts)

    except (KeyError, ValueError) as e:
        # Handle JSON parsing or missing key errors
        print(f"[Response parsing error: {e}]")
        return ["[Parsing error]"] * len(texts)

    except Exception as e:
        # Handle any other unexpected errors
        print(f"[Unexpected error: {e}]")
        return ["[Unexpected error]"] * len(texts)
