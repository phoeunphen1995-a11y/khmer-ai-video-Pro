
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Khmer AI Video Translator Pro"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://phoeunphen1995-a11y.github.io"
    ],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {
        "app": "Khmer AI Video Translator Pro",
        "status": "AI Server is running"
    }

@app.get("/health")
def health():
    return {
        "status": "OK",
        "message": "Khmer AI Server Ready"
    }
