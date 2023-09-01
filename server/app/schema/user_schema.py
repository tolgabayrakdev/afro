from pydantic import BaseModel


class UserLogin(BaseModel):
    email: str
    password: str

class UserRegister(BaseModel):
    username: str
    email: str
    password: str


class UserResetToken(BaseModel):
    email: str

class UserChangePassword(BaseModel):
    password: str    