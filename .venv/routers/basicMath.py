from fastapi import APIRouter


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