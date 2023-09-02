#Fast API is great
from fastapi import FastAPI

app=FastAPI()

@app.get("/")
async def root():
    return {"message":"HELLO"}

@app.get("/question")
async def question():
    return {"message":"How old are you?"}
