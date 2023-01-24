from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/hello")
async def hello():
    return {"message": "hello world!"}


def main():
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)


if __name__ == "__main__":
    main()
