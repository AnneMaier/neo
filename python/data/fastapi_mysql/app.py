from fastapi import FastAPI
from pydantic import BaseModel
from database import db_conn
from models import St_info, St_grade


app = FastAPI()

db = db_conn()
session = db.sessionmaker()

class Item(BaseModel):
    name: str
    number : int


@app.get('/')
async def HealthCheck():
    print({"message": "ok"})
    return {"message": "ok"}

@app.get('/st_info')
async def Select_st_info():
    result = session.query(St_info)
    return result.all()

@app.get('/st_grade')
async def Select_st_grade():
    result = session.query(St_grade)
    return result.all()

@app.get('/getuser')
async def getuser(id=None, name=None):
    if (id is None) and (name is None):
        return "id, name을 입력해줘"
    else:
        if id is None:
            result = session.query(St_info).filter(St_info.name == name).all()
        elif name is None:
            result = session.query(St_info).filter(St_info.id == id).all()
        else:
            result = session.query(St_info).filter(St_info.id == id, St_info.name == name).all()
        return result

@app.get('/useradd')
async def UserAdd(id=None, name=None, dept=None):
    if (id is None) and (name is None) and (dept is None):
        return "id, name, dept을 입력해줘"
    else:
        if id is None:
            result = session.query(St_info).filter(St_info.name == name, St_info.dept == dept).all()
        else:
            user = St_info(ST_ID=id, NAME=name, DEPT=dept)
            session.add(user)
            session.commit()
            result = session.query(St_info).all()
            return result

@app.get('/userupdate')
async def UserUpdate(id=None, name=None, dept=None):
    if (id is None) and (name is None) and (dept is None):
        return "id, name, dept을 입력해줘"
    else:
        if id is None:
            result = session.query(St_info).filter(St_info.name == name, St_info.dept == dept).all()
        else:
            user = session.query(St_info).filter(St_info.ST_ID == id).first()
            user.NAME = name
            user.DEPT = dept
            session.commit()
            result = session.query(St_info).filter(St_info.ST_ID == id).all()
            return result

@app.get('/userdelete')
async def UserDelete(id=None):
    if (id is None):
        return "id를 입력하세요."
    else:
        user = session.query(St_info).filter(St_info.ST_ID == id).first()
        session.delete(user)
        session.commit()
        result = session.query(St_info).all()
        return result