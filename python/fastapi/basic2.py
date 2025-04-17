from fastapi import FastAPI
from pydantic import BaseModel

class HellloWorldRequest(BaseModel):
    name : str
    age : int

app = FastAPI()

@app.get('/')
async def HealthCheck():
    return {"status": "ok"}

@app.get(path='/hello/{name}')
async def Hello_with_name(name:str):
    return "Hello with name. Your name ins " + name

@app.post(path='hello/post')
async def Hello_post(request: HellloWorldRequest):
    return "Hello with Post. Your name is {} and age is {}".format(request.name, request.age)