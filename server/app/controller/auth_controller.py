from fastapi import APIRouter
from fastapi import Request, Response, HTTPException
from service.auth_service import AuthService
from schema.user_schema import UserLogin, UserRegister

auth_router = APIRouter()


@auth_router.post("/login")
async def login(user: UserLogin, response: Response):
    data = await AuthService.login(user.email, user.password)
    if data is None:
        return HTTPException(status_code=400, detail="Username or password wrong!")
    response.set_cookie(key="access_token", value=data["access_token"])
    return {"data": {"email": data.email}}

@auth_router.route("/register")
async def register(user:  UserRegister, response: Response):
    return 
