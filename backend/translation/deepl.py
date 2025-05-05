# Lawan Mai
# Version 1.0
# Module for translating Japanese text into English using DeepL API

import requests
from config import DEEPL_API_KEY

DEEPL_API_URL = "https://api-free.deepl.com/v2/translate"

def translate_deepl_batch(texts, source_lang="JA", target_lang="EN"):
    if not texts:
        return []

    data = [("auth_key", DEEPL_API_KEY)]
    for txt in texts:
        data.append(("text", txt))
    data.append(("source_lang", source_lang))
    data.append(("target_lang", target_lang))

    try:
        response = requests.post(DEEPL_API_URL, data=data)
        response.raise_for_status()
        translations = response.json()["translations"]
        return [t["text"] for t in translations]
    except Exception as e:
        print(f"[Translation error: {e}]")
        return ["[Translation error]"] * len(texts)
