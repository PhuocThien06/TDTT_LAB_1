from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()

# Load model
classifier = pipeline("sentiment-analysis")

# Request model
class TextInput(BaseModel):
    text: str

# API 1
@app.get("/")
def root():
    return {"message": "Sentiment Analysis API using Hugging Face"}

# API 2
@app.get("/health")
def health():
    return {"status": "ok"}

# API 3
@app.post("/predict")
def predict(input: TextInput):
    if not input.text:
        raise HTTPException(status_code=400, detail="Text is required")

    try:
        result = classifier(input.text)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))