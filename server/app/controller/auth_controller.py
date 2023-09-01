from fastapi import APIRouter
from fastapi import Request, Response, HTTPException
from service.auth_service import AuthService
from schema.user_schema import UserLogin

auth_router = APIRouter()


@auth_router.post("/")
async def test(user: UserLogin, response: Response):
    data = await AuthService.login(user.email, user.password)
    if data is None:
        return HTTPException(status_code=400, detail="Username or password wrong!")
    
    return {"data": {"email": data.email}}
