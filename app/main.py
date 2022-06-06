from typing import Optional

from fastapi import FastAPI
from starlette.responses import StreamingResponse
from PIL import Image
import io

app = FastAPI()


@app.get("/")
def read_root():
    return {"LA API FUNCIONA"}



@app.get("/nombre")

def hello(name = None):

    if name is None:
        text = 'Hello!'

    else:
        text = 'Hello ' + name + '!'

    return text


 