from fastapi import FastAPI
from fastapi import UploadFile
from fastapi import File

import shutil

from inference.predict import predict

app = FastAPI()


@app.get("/")
def home():

    return {
        "message": "AgriLens AI API"
    }


@app.post("/predict")
async def classify_crop(
    file: UploadFile = File(...)
):

    file_path = f"uploads/{file.filename}"

    with open(
        file_path,
        "wb"
    ) as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )

    result = predict(file_path)

    return result