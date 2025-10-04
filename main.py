from fastapi import FastAPI
from fastapi.responses import TextResponse

app = FastAPI()


@app.get("/ping")
def read_root():
    return TextResponse("Hello, World!")
