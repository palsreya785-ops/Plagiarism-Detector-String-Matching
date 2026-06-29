from fastapi import FastAPI
from routes import router

app = FastAPI(
    title="Plagiarism Detector",
    version="1.0"
)

app.include_router(router)

@app.get("/")
def home():
    return {"message": "Plagiarism Detector API Running"}