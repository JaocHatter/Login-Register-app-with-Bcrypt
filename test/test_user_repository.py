from src.repositories.user_repository import UserRepository
from src.models.user import User

def test_create_user(db_session):
    # Arrange
    user_repo = UserRepository(db_session)
    # Act
    user = user_repo.create_User("testuser", "hashed_password", "test@example.com")
    # Assert
    assert user.username == "testuser"
    assert user.email == "test@example.com"
    assert user.password == "hashed_password"

def test_get_user_by_username(db_session):
    # Arrange
    user_repo = UserRepository(db_session)
    # Act
    db_session.add(User(username="testuser", password="hashed_password", email="test@example.com"))
    db_session.commit()
    user = user_repo.get_User_by_username("testuser")
    # Assert
    assert user is not None
    assert user.username == "testuser"
    assert user.email == "test@example.com"
