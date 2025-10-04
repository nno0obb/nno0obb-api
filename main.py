import uvicorn
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI()


@app.get("/ping")
def read_root():
    return PlainTextResponse("pong")


if __name__ == "__main__":
    config = uvicorn.Config(
        "main:app",
        host="0.0.0.0",
        port=8080,
    )
    server = uvicorn.Server(config)
    server.run()
