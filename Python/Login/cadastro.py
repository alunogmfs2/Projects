from database import Database
from os import system


class Cadastro:
    def __init__(self) -> None:
        self.db = Database()
        self.conn = self.db.connectToDatabase()
        
        self.continuar: bool = True
        
        self.u: str = ""
        self.s: str = ""
    
    def perguntarUsuario(self) -> str:
        return input("Enter username: ")
    
    def perguntarSenha(self) -> str:
        return input("Enter password [min. 8 characters]: ")
    
    def usuario(self) -> None:
        usuario = self.perguntarUsuario()
        dados = self.db.get(self.conn)
        
        if usuario in dados:
            print("Username already exists.")
            self.continuar_u = False
        else:
            self.u = usuario
            self.continuar_u = True
    
    def senha(self) -> None:
        senha = self.perguntarSenha()
        
        if len(senha) < 8:
            print("Password must be at least 8 characters long.")
            self.continuar_s = False
        else:
            self.s = senha
            self.continuar_s = True

    def cadastro(self) -> None:
        try:
            while self.continuar:
                system("cls")
                print("Welcome to the Sign Up Center\n")
                
                self.usuario()
                if not self.continuar_u:
                    continue
                
                self.senha()
                if not self.continuar_s:
                    continue
                
                print(f"Username: {self.u}, Password: {self.s}")
                self.db.query(self.conn, "INSERT INTO dados (T_USUARIO, T_SENHA) VALUES (?, ?)", (self.u, self.s))
                
                self.u, self.s = "", ""
                break
        finally:
            self.conn.close()  # Ensure the database connection is closed
