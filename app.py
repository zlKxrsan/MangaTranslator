from fastapi import FastAPI, UploadFile, File
from fastapi.responses import Response
from fastapi.middleware.cors import CORSMiddleware
from backend.core import process_image

app = FastAPI()

# CORS freischalten für Frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React-Dev-Server
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/translate/")
async def translate_image(file: UploadFile = File(...)):
    image_bytes = await file.read()
    processed_image = process_image(img_bytes=image_bytes)
    return Response(content=processed_image, media_type="image/png")
