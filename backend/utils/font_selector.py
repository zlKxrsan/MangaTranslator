import os


def get_font_path_for_language(lang_code):
    font_map = {
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

    font_path = font_map.get(lang_code.upper())

    if not font_path:
        raise ValueError(f"Keine passende Schriftart für Sprache: {lang_code}")

    if not os.path.exists(font_path):
        raise FileNotFoundError(f"Font-Datei nicht gefunden: {font_path}")

    return font_path
