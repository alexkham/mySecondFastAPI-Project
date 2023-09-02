from fastapi import APIRouter


router=APIRouter(
    prefix='/basic',
    tags=['basic']
)

@router.get('/add/{x}/{y}')
def add(x,y):
    result=int(x)+int(y)
    return {"result":str(result)}