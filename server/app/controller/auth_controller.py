from fastapi import APIRouter
from fastapi import Request, Response, HTTPException, Depends
from service.auth_service import AuthService
from schema.user_schema import UserLogin, UserRegister
from fastapi.security import OAuth2PasswordBearer
from typing import Annotated

auth_router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@auth_router.post("/login")
async def login(user: UserLogin, response: Response):
    data = await AuthService.login(user.email, user.password)
    if data is None:
        return HTTPException(status_code=400, detail="Username or password wrong!")
    response.set_cookie(key="access_token", value=data["access_token"], httponly=True)
    response.set_cookie(key="access_token", value=data["access_token"], httponly=True)
    return {
        "access_token": data["access_token"],
        "refresh_token": data["refresh_token"],
    }


@auth_router.post("/register", status_code=201)
async def register(user: UserRegister):
        try:
            AuthService.register(user)
            return {"message": "User created succesful."}
        except HTTPException as e:
             raise HTTPException(status_code=500, detail="Internal Server Error")


@auth_router.get("/test")
async def test(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"message": "Secret Router Here...!"}
