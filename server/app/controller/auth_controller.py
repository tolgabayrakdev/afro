from fastapi import APIRouter
from fastapi import Request, Response, HTTPException
from service.auth_service import AuthService

auth_router = APIRouter()


@auth_router.get("/")
async def test():
    data = await AuthService.login()
    print(data)
    return {"data": {
        "email": data.email
    }}