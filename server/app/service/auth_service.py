from database import connection
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException
from util.helper import Helper
from typing import Any


class AuthService:
    @staticmethod
    async def login(email: str, password: str):
        try:
            hash_password = Helper.generate_hash_password(password=password)
            query = text(
                "SELECT * FROM users WHERE email = :email and password = :password"
            )
            result = connection.execute(query, email=email, password=hash_password)
            print(result)
            for row in result:
                print(row)
                return row
        except SQLAlchemyError as e:
            raise HTTPException(status_code=500, detail="Database Error!")

    @staticmethod
    async def register(data: Any):
        try:
            hash_password = Helper.generate_hash_password(password=data.password)
            query = text(
                """
                INSERT INTO users(username, email, password)
                VALUES(%s, %s, %s)
                """
            )
            result = connection.execute(query, data.username, data.email, hash_password)
            for row in result:
                print(row)
                return row

        except SQLAlchemyError as e:
            raise HTTPException(status_code=500, detail="Database Error!")
