from fastapi import FastAPI
from pydantic import BaseModel

appp = FastAPI()

@appp.get('/')
def getdata():
    return "Hiii Mayur"
