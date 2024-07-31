import io

from fastapi import FastAPI, File, UploadFile
import numpy as np
from PIL import Image
import torch
import torch.nn.functional as F
import uvicorn

from .cfg import MODEL, IDX2LABEL

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello API!"}

@app.post("/classify_image/")
async def classify_image(file: UploadFile):
    image = Image.open(io.BytesIO(await file.read()))
    preprocessed_image = preprocess_image(image)
    probs = run_classification(preprocessed_image)
    return {"filename": file.filename, "image_size": preprocessed_image.shape, "probs": probs}

def preprocess_image(image):
    # convert PIL image to tensor and normalize
    img_tensor = torch.tensor(np.array(image)) / 255.
    
    # return tensor that's shaped correctly for our neural network
    return img_tensor.permute(2, 0, 1)[None, ...]

def run_classification(image):
    output = MODEL(image)
    probs = F.softmax(output, dim=1)
    
    indices = torch.argsort(probs, descending=True).squeeze(0).tolist()
    prob_list = probs[:, indices].squeeze(0, 1).tolist()
    label_list = list(map(lambda x: IDX2LABEL[x], indices))
    probs_list = {label:prob for label,prob in zip(label_list, prob_list)}
    
    return probs_list

if __name__ == "__main__":
    uvicorn.run("src.main:app", host="0.0.0.0", port=8000)