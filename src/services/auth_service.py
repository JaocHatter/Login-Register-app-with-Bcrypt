from src.repositories.user_repository import UserRepository
from src.utils.hash_password import HashUtil

class AuthService:
    def __init__(self, db):
        self.user_repo = UserRepository(db)

    def register_user(self, username, password, email):
        hashed_password = HashUtil.hash(password)
        return self.user_repo.create_User(
                                            username = username,
                                            password= hashed_password,
                                            email = email
                                            )
    
    def authenticate_user(self, username, password):
        user = self.user_repo.get_User_by_username(username)
        if user and HashUtil.verify(password, user.password):
            return user
        return None