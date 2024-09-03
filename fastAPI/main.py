from fastapi import FastAPI
from core.config import settings

app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)


@app.get("/test")
def hello_api():
    return {"message": "hello api"}

@app.get("/testBranch")
def hi_api():
    return {"message": "hi api"}