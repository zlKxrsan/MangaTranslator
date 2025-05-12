
# 🗨️ ToonLingo

**ToonLingo** is a web-based tool that allows users to upload English Webtoon or comic images and automatically translate them into another language. (DE, FR, ES, PT-BR, PL, TR) 

It combines OCR, translation, and image processing to create a seamless Webtoon localization workflow.

---

## 🚀 Features

- 🖼️ Upload Webtoon/comic pages as images
- 🔍 Detect and extract text from speech bubbles using **[PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR)**
- 🌐 Translate the extracted text using **[DeepL API](https://www.deepl.com/pro#developer)**
- 🧽 Remove original text and overlay translated text with **[OpenCV](https://opencv.org/)**
- 📥 Download fully translated comic panels

---

## 🛠️ Tech Stack

| Component     | Technology                                                |
|---------------|-----------------------------------------------------------|
| OCR           | [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR)     |
| Translation   | [DeepL API](https://www.deepl.com/pro#developer)           |
| Image Editing | [Pillow](https://python-pillow.org/)                       |
| Backend       | [Python FastAPI](https://fastapi.tiangolo.com/)            |
| Frontend      | [React](https://reactjs.org/) / [Vite](https://vitejs.dev/) / [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript) / [Tailwind CSS](https://tailwindcss.com/) |

---

## 📦 Installation and Setup

Follow these steps to set up the project locally:

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/ToonLingo.git
    cd ToonLingo
    ```

2. Add your DeepL API key to the backend configuration:
    ```bash
    echo "DEEPL_API_KEY='YOUR_PERSONAL_KEY'" >> backend/config.py
    ```

3. Build and run the Docker containers:
    ```bash
    docker-compose up --build -d
    ```

4. Once the containers are running, open your browser and visit (the first request will download the models and may take 1 minute):  
   [http://127.0.0.1:5173/](http://127.0.0.1:5173/)

5. Start translating your Webtoon/comic pages! 😊

---

## 💭 Future Plans

I experimented with training a model specifically for Manga/Manhwa OCR, but due to limited resources, the results were less accurate than expected. The codebase has been designed to potentially support future OCR models to improve the project. Same goes for future translation models to offer more language-support.

---

## 📜 Sources

- **Bangers-Regular** - Copyright 2010, The Bangers Project Authors  
   [Bangers-Regular on GitHub](https://github.com/googlefonts/bangers)

---

## License

This project is licensed under the MIT License – see the [LICENSE](./LICENSE) file for details.

