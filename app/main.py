import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse, PlainTextResponse

app = FastAPI()


@app.get("/")
def get_root():
    return JSONResponse({"app": {"name": "nno0obb-api"}})


@app.get("/ping")
def get_ping():
    return PlainTextResponse("pong")


if __name__ == "__main__":
    config = uvicorn.Config(
        "main:app",
        host="0.0.0.0",
        port=8080,
    )
    server = uvicorn.Server(config)
    server.run()
