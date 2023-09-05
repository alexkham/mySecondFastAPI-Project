#Fast API is great
from fastapi import FastAPI,APIRouter,File, UploadFile
from routers import basicMath
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import json
from db import *
import os
from dbjson import db_new ,db_inner




app=FastAPI()
app.include_router(basicMath.router)

@app.get("/")
async def root():
    return os.getcwd()




# @app.get("/")
# async def root():
#     return {"message":"HELLO"}
#new route
@app.get("/question")
async def question():

    # action=db.actions[0]['action']
    return {"message":f"How old are you ?"}

@app.get("/json")
def jsonData():
    data=json.loads(actions_list)
    
    return data

@app.get("/json1")
def jsonData1():
    data=json.loads(db_new.actions_list_new)
    
    return data

@app.get("/json-file")
def jsonDataFile():
    action=json_data['actions'][1]['action']
    
    return  action

@app.get("/params/{x}/{y}")
async def params(x,y):
    result=int(x)+int(y)
    return {"message":str(result)}

origins={"http://localhost:3000"}
app.add_middleware(CORSMiddleware,
                   allow_origins=origins,
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"]                   
                   )