from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get('/')
def getdata():
    return "Hello Mayur"