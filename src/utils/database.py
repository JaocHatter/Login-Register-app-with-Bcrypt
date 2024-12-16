from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Una vez creada la base de datos y tablas
# visualiza la lista de tablas
# docker exec -it <nombre_del_contenedor_db> psql -U admin -d app_db
# \dt

DATABASE_URL = "postgresql+psycopg2://admin:admin@db:5432/app_db"

# Creamos un motor de conexión a la base de datos
engine = create_engine(url = DATABASE_URL)
# Creamos una fabrica  de sesiones que se usarán para interactuar con la base de datos
SessionLocal = sessionmaker(bind=engine, autocommit = False)
# Crea una clase base que se usará utilizada para definir los modelos de datos
Base = declarative_base()

# Funcion para retornar una sesión a la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
