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
            query = text("SELECT * FROM users WHERE email = :email and password = :password")
            print(hash_password)
            result = connection.execute(query, [{"email": email, "password": hash_password}])
            if result:
                for row in result:
                    access_token = Helper.generate_access_token(
                        {"email": row.id, "password": row.password}
                    )
                    refresh_token = Helper.generate_access_token(
                        {"email": row.id, "password": row.password}
                    )
                    return {
                        "access_token": access_token,
                        "refresh_token": refresh_token,
                    }
        except SQLAlchemyError as e:
            print(e)
            raise HTTPException(status_code=500, detail="Database Error!")

    @staticmethod
    def register(data: Any):
        try:
            connection.begin()
            hash_password = Helper.generate_hash_password(password=data.password)
            query = text(
                """
                INSERT INTO users (username, email, password, role_id, created_at, updated_at)
                VALUES(:username, :email, :password, :role_id, now(), now());
                """
            )
            connection.execute(query, {
                "username": data.username,
                "email": data.email,
                "password": hash_password,
                "role_id": 1
            })
            connection.commit()
        except SQLAlchemyError as e:
            connection.rollback()
            raise HTTPException(status_code=500, detail="Database Error!")
