from sqlalchemy import Column, Integer, String
from src.utils.database import Base

# Una vez creada la base de datos
# Será necesario crear la tabla, usa alembic para ello
# alembic revision --autogenerate -m "create users table"
# alembic upgrade head

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key= True)
    username = Column(String(50), unique = True ,nullable= False)
    password = Column(String(256), nullable = False)
    email =  Column(String(60), unique = True, nullable= False)

