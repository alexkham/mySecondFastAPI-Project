from fastapi import APIRouter,Body
from pydantic import BaseModel
from typing import Optional
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder


def say_hi(name: Optional[str] = None):
    if name is not None:
        print(f"Hey {name}!")
    else:
        print("Hello World")





router=APIRouter(
    prefix='/basic',
    tags=['basic']
)

@router.get('/add/{x}/{y}')
def add(x,y):
    result=int(x)+int(y)
    return {"result":str(result)}

@router.get('/multiply')
def add(x,y):
    result=float(x)*float(y)
    return {"result":str(result)}

@router.get('/divide')
def divide(x,y):
    result=float(x)/float(y)
    return {"result":str(result)}

class BlogModel(BaseModel):
    title:str
    content:str
    published:Optional[bool]


@router.post("/new")
async def new(blog:BlogModel):
    
     return {"body2":blog}