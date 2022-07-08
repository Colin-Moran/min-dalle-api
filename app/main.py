from ast import Bytes
from msilib.schema import Binary
from tkinter import Image
from tokenize import Number
from fastapi import FastAPI
from min_dalle import MinDalle
from pydantic import BaseModel, ValidationError
from fastapi.responses import Response
import io
import PIL

isMega = False

class ImageGenerationRequest(BaseModel):
    text: str
    seed = -1
    grid_size = 2
    log2_k = 6
    log2_supercondition_factor = 5
    is_verbose = False
    
app = FastAPI()
model = MinDalle(is_mega=isMega, models_root='../pretrained')

@app.get("/")
async def root():
    return {"message": "min-dalle-api is running!"}

@app.post("/generate")
async def generate(req: ImageGenerationRequest):
    image = getImage(req)
    imageAsBytes = imageToByteArray(image)
    return Response(imageAsBytes, media_type="image/png")

def getImage(params: ImageGenerationRequest):
    image = model.generate_image(text=params.text, seed=params.seed, grid_size=params.grid_size, log2_k=params.log2_k, log2_supercondition_factor=params.log2_supercondition_factor, is_verbose=params.is_verbose)
    
    ### For Testing ###
    # image = PIL.Image.new(mode="RGB", size=(200, 200))
    
    return image

def imageToByteArray(image: Image) -> bytes:
  imgByteArr = io.BytesIO()
  image.save(imgByteArr, format="png")
  imgByteArr = imgByteArr.getvalue()
  return imgByteArr