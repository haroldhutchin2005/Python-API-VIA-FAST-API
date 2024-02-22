from typing import Union
from fastapi import FastAPI, Query
import requests

app = FastAPI()

@app.get("/")
def read_root():
    return {"Missing Query": "/ai?content=your question here!"}

@app.get("/ai")
def get_hercai_response(content: str = Query(..., title="The question to ask")):
    url = f'https://hercai.onrender.com/v3/hercai?question={content}'

    try:
        response = requests.get(url)
        response_data = response.json()

        return response_data
    except Exception as e:
        return {'error': str(e)}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
