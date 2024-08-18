from os import system
from time import sleep

from database import Database
from login import Login
from cadastro import Cadastro


class Program:
    def __init__(self) -> None:
        self.db = Database()
        self.conn = self.db.connectToDatabase()
    
    def listarUsuarios(self, lim: int=5) -> None:
        system("cls")
        usuarios: list = self.db.get(self.conn)
        cont: int = 0
        for u in usuarios:
            print(f"User: {u[1]} - Password: {u[2]} - ID: {u[0]}")
            if cont == lim:
                system("cls")
                cont = 0
            cont += 1
    
    def cadastro(self) -> None:
        cadastro = Cadastro()
        cadastro.cadastro() 
    
    def login(self) -> None:
        login = Login()
        login.login()
    
    def traduzirEscolha(self, escolha: int) -> None:
        match escolha:
            case 1:
                self.login()
            case 2:
                self.cadastro()
            case 3:
                self.listarUsuarios()
            case 0:
                system("cls")
                print("Exiting...")
                sleep(1)
            case _:
                print("Invalid Option!")
    
    def escolha(self) -> int:
        while True:
            try:
                escolha: int = int(input("Chose an Option: "))
                if escolha < 0 or escolha > 3:
                    print("Invalid Option!")
                else:
                    return self.traduzirEscolha(escolha)
            except ValueError:
                print("Invalid Option!")
    
    def menu(self) -> None:
        system("cls")
        print("1 - Sign In")
        print("2 - Sign Up")
        print("3 - List Users")
        print("0 - Exit")
        self.escolha()
    
    
    def main(self) -> None:
        self.menu()
