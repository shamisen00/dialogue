from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/hello")
async def hello():
    return {"message": "hello world!"}
