from database import Database


class Login:
    def __init__(self) -> None:
        self.db = Database()
        self.conn = self.db.connectToDatabase()
    
    def login(self) -> None:
        ...
        