from src.models.user import User

class UserRepository:
    def __init__(self, db):
        self.db = db

    def create_User(self, username, password, email):
        new_User = User(username = username, password = password, email = email)
        self.db.add(new_User)
        self.db.commit()
        return new_User

    def get_User_by_username(self, username):
        return self.db.query(User).filter(User.username == username).first()
        