from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.security import OAuth2PasswordRequestForm
# import bcrypt
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from app.admin.security import get_hashed_password, generate_token
from app.database import get_db
import app.cruds.user as crud
from app.admin.utils import current_time
from app.cruds.user import UserCrud
from app.schemas.user import UserDTO
from app.models.user import User
from sqlalchemy.orm import Session
'''
It receives an object, like a Pydantic model, and returns a JSON compatible version:
https://fastapi.tiangolo.com/tutorial/encoder/#__tabbed_1_1
'''
router = APIRouter()


@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register_user(dto: UserDTO, db: Session = Depends(get_db)):
    user_crud = UserCrud(db)
    print(f" 회원가입에 진입한 시간: {current_time()} ")
    userid = user_crud.find_userid_by_email(request_user=dto)
    if userid == "":
        print(f"해시 전 비번 : {dto.password}")
        dto.password = get_hashed_password(dto.password)
        print(f"해시 후 비번 : {dto.password}")
        # newUser = jsonable_encoder(user)
        # newUser['password'] = hashPW
        result = user_crud.add_user(request_user=dto)
    else:
        result = JSONResponse(status_code=400, content=dict(msg="Already Existed Email"))
    return {"data": result}


@router.post("/login", status_code=200)
async def login(dto: UserDTO, db: Session = Depends(get_db)):
    user_crud = UserCrud(db)
    userid = user_crud.find_userid_by_email(request_user=dto)
    dto.userid = userid
    print(f" >>> login 넘기기 전에 보는 id {dto.userid}, pw {dto.password}")
    if userid != "":
        login_user = user_crud.login(request_user=dto)
        if login_user is not None:
            print(f" 1 $$$$$$$ 로그인 성공 정보 : {login_user}")
            new_token = generate_token(login_user.email)
            login_user.token = new_token
            print(f" 2 $$$$$$$ 로그인 성공 정보 : {login_user}")
            result = {"data": login_user}
        else:
            print(f"로그인 실패")
            result = JSONResponse(status_code=400, content=dict(msg="Password is not correct"))
    else:
        result = JSONResponse(status_code=400, content=dict(msg="Email Not Exist"))
    return result




@router.put("/modify/{id}")
async def modify_user(id:str, request_user: UserDTO, db: Session = Depends(get_db)):
    crud.update_user(id=id, request_user=request_user)
    return {"data": "success"}


@router.delete("/remove/{id}", tags=['age'])
async def remove_user(id:str, request_user: UserDTO, db: Session = Depends(get_db)):
    crud.delete_user(id, request_user=request_user)
    return {"data": "success"}


@router.get("/page/{page}")
async def get_all_users(page: int, db: Session = Depends(get_db)):
    ls = crud.find_all_users(page=page)
    return {"data": ls}


@router.get("/id?={id}")
async def get_user_by_id(id: str, db: Session = Depends(get_db)):
    crud.find_user_by_id(id=id)
    return {"data": "success"}


@router.get("/job/{search}/{page}")
async def get_users_by_job(search:str, page: int, db: Session = Depends(get_db)):
    crud.find_users_by_job(search=search, page=page)
    return {"data": "success"}

