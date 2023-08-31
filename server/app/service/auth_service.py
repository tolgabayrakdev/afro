from database import connection
from sqlalchemy import text

class AuthService:

    @staticmethod
    async def login():
        query = text("SELECT * FROM users")
        result = connection.execute(query)
        for row in result:
            return row
