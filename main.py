from unittest.mock import sentinel
from fastapi import FastAPI
import tensorflow as tf
import tensorflow_text as text
import numpy as np
from pydantic import BaseModel

app = FastAPI()

class MRPC(BaseModel):
    sentence1: str
    sentence2: str

#model= tf.saved_model.load("/Model_2")
model= tf.saved_model.load("C://Users/Gaurav Agrawal/Downloads/vscode/Model_2")

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/predict")
async def fetch_pred(tr:MRPC):
    example= {"sentence1": tf.constant([tr.sentence1]),"sentence2": tf.constant([tr.sentence2])}
    result = model(example)['class_id'].numpy().tolist()
    return {"class is": result}