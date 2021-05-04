class User:
    def __init__(self, name: str, email: str, hashed_password: str, user_id: int = None) -> None:
        self.id = user_id
        self.name = name
        self.email = email
        self.hashed_password = hashed_password

    def __repr__(self) -> str:
        return f""""User<Id={self.id}, Name={self.name}, Email={self.email}, Hashed password={self.hashed_password}>"""
