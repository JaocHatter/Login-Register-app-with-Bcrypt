import bcrypt

class HashUtil:
    @staticmethod
    def hash(password):
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode(), salt).decode()

    @staticmethod
    def verify(password, hashed_password):
        return bcrypt.checkpw(password.encode(), hashed_password.encode())
