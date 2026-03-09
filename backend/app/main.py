from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Conversational BI API running"}