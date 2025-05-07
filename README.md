# 🗨️ ToonLingo

**ToonLingo** is a web-based tool that allows users to upload Webtoons or comic images and get them automatically translated into another language.  
It combines OCR, translation, and image processing to create a seamless Webtoon localization workflow.

---

## 🚀 Features

- 🖼️ Upload Webtoon/comic pages as images
- 🔍 Detect and extract text from speech bubbles using **PaddleOCR**
- 🌐 Translate extracted text using **DeepL**
- 🧽 Remove original text and overlay translated text with **OpenCV**
- 📥 Download fully translated comic panels

---

## 🛠️ Tech Stack

| Component      | Technology         |
|----------------|--------------------|
| OCR            | [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) |
| Translation    | [DeepL API](https://www.deepl.com/pro#developer)       |
| Image Editing  | [OpenCV](https://opencv.org/)                          |
| Backend (optional) | Python (FastAPI, Flask, etc.)                  |
| Frontend (optional) | React / Vue / Svelte (or static HTML)         |

---

## 📦 Installation

```bash
git clone https://github.com/your-username/ToonLingo.git
cd ToonLingo
pip install -r requirements.txt
