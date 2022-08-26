from pydoc import cli
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient
from pydantic import BaseModel
import uvicorn
client = MongoClient('mongodb://localhost:27017/')
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
    )
@app.get('/')
async def get():
    return {'200' : "Success"}
class User(BaseModel):
    username: str
    password : str
    name: str
    mob: str
    wallet : int =0
@app.post('/adduser')
async def adduser(user : User):
    if client.digitransfer.user.count_documents({'username' : user.username}) == 0:
        try :
            client.digitransfer.user.insert_one(dict(user))
            return True
        except Exception as e :
            print(str(e))
    else:   
        return False   


 
class Login(BaseModel):
    username : str
    password: str

@app.post('/login')
async def login(login : Login):
    if client.digitransfer.user.count_documents(dict(login)) == 1 :
        return True
    else: 
        return False
class Money(BaseModel):
    username : str
    credit : int

@app.post('/addmoney')
async def addmoney(money : Money):
    filter = {
        'username' : money.username
    }
    project = {
        '_id':0,
        'wallet':1
    }
    wallet = client.digitransfer.user.find_one(filter)['wallet'] + money.credit
    
    update = {
        '$set': { 'wallet':wallet }
    }
    try : 
        client.digitransfer.user.find_one_and_update(filter,update)
        return True
    except Exception as e :
        return False


    
if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload = True ,debug = True)
