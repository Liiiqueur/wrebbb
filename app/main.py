from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return { "message": "Helo Root!" }

@app.get("/home")
def home():
    return { "message": "Home!" }