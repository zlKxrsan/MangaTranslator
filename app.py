from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import Response
from fastapi.middleware.cors import CORSMiddleware
from backend.core import process_image

app = FastAPI()

# CORS freischalten für Frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5173"],  # React-Dev-Server
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/translate/")
async def translate_image(
    file: UploadFile = File(...),
    target_lang: str = Form(...)
):
    image_bytes = await file.read()
    processed_image = process_image(img_bytes=image_bytes, target_lang=target_lang)
    return Response(content=processed_image, media_type="image/png")
