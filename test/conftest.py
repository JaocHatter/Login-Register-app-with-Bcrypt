import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.utils.database import Base

@pytest.fixture(scope="function")
def db_session():
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(bind = engine)
    Sesion = sessionmaker(bind  = engine)
    session = Sesion()
    try:
        yield session
    finally:
        session.close()
        Base.metadata.drop_all(bind = engine)