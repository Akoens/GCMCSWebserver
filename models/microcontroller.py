class Microcontroller:
    def __init__(self, name: str, user_id: int, microcontroller_id: int = None) -> None:
        self.id = microcontroller_id
        self.name = name
        self.user_id = user_id

    def __repr__(self) -> str:
        return f"Microcontroller<Id={self.id}, Name={self.name}, User id={self.user_id}>"
