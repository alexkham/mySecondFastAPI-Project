#Fast API is great
from fastapi import FastAPI,APIRouter
from routers import basicMath
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()
app.include_router(basicMath.router)



@app.get("/")
async def root():
    return {"message":"HELLO"}
#new route
@app.get("/question")
async def question():
    return {"message":"How old are you?"}

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