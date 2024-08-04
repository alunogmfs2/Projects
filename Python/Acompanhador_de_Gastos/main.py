from os import system
import sqlite3
from sqlite3 import Error
import datetime as dt
import time


class Database:
    def __init__(self):
        pass

    def create_connection(self):
        conn = None
        try:
            conn = sqlite3.connect("E:\\Programacao\\Projetos\\Projects\\Python\\Acompanhador_de_Gastos\\Database\\gastos.db")
            print(sqlite3.version)
        except Error as e:
            print(e)
        return conn

    def query(self, connection, sql, values=None):
        try:
            cursor = connection.cursor()
            cursor.execute(sql, values)
            connection.commit()
        except Error as e:
            print(e)
            
    def consultar(self, connection):
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM tb_gastos")
        res = cursor.fetchall()
        return res


class Project:
    def __init__(self):
        self.opc = -1
        self.opcs = {
            "Inserir novo Gasto": 1,
            "Listar Gastos": 2,
            "Excluir Gasto": 3,
            "Sair": 4
        }
        
        self.categorias = ["Programacao", "Comida", "Maker", "Outras Coisas"]

        self.continuar = True

        # Criando a base de dados
        self.database = Database()

        self.connection = self.database.create_connection()
        
        while self.continuar:
            self.programa()
            
    # Perguntar Dados para Inserir
    def perguntarDados(self):
        while True:
            system("cls")
            print("Categorias Disponíveis:")
            for i in self.categorias:
                print(i)
            print()
            categoria = input("Qual Categoria você escolhe: ")
            if categoria in self.categorias:
                system("cls")
                
                try:
                    preco = float(input("Digite o Preco do seu Gasto: "))
                    try:
                        saldo = float(input("Digite seu Saldo Atual: "))
                        self.opc = -1
                        return (dt.datetime.today().date(), categoria, preco, saldo - preco)
                    except:
                        print("ERRO: Digite um Número")
                except:
                    print("ERRO: Digite um Número")
            else:
                print("ERRO: Categoria nao encontrada")

    # Traduzir as Acoes em Funcoes
    def acoes_em_funcoes(self):
        self.perguntarParametros()
        acao = self.opc
        
        if acao == "Inserir novo Gasto":
            dados = self.perguntarDados()
            self.inserirGasto(dados)
        elif acao == "Listar Gastos":
            self.listarGastos()
        elif acao == "Excluir Gasto":
            self.excluirGasto()
        elif acao == "Sair":
            self.continuar = False
    
    # Traduzir as Opcoes em Acoes
    def traduzirOpcoes(self, opc):
        for key, item in self.opcs.items():
            if item == opc:
                return key
        return None
    
    # Perguntar os Parametros
    def perguntarParametros(self):
        while True:
            try:
                opc = int(input("Escolha uma Opcao: "))
                opc = self.traduzirOpcoes(opc)
                
                if opc != None:
                    self.opc = opc
                    break
                else:
                    print("ERRO: Opcao Invalida")
                    
            except:
                print("ERRO: Digite um Número Inteiro")

    # Criando as Funcoes
    def inserirGasto(self, dados):
        vsql = "INSERT INTO tb_gastos (T_DATA, T_CATEGORIA, F_PRECO, F_SALDO) VALUES (?, ?, ?, ?)"
        self.database.query(self.connection, vsql, dados)
        print("Gasto inserido")
    
    def listarGastos(self):
        system("cls")
        gastos = self.database.consultar(self.connection)
        lim = 10
        cont = 0
        
        for i in gastos:
            print(f"ID: {i[0]} Data: {i[1]}, Categoria: {i[2]}, Preco: {str(i[3]).replace(".", ",")}€, Saldo: {str(i[4]).replace(".", ",")}€")
            
            cont += 1
            if cont == lim:
                cont = 0
                print()
                input("Pressione Enter para continuar...")
        system("pause")
    
    def excluirGasto(self):
        self.listarGastos()
        system("cls")
        ID = int(input("Digite o ID do Gasto: "))
        for i in self.database.consultar(self.connection):
            if i[0] == ID:
                vsql = "DELETE FROM tb_gastos WHERE N_IDGASTO=?"
                self.database.query(self.connection, vsql, (ID,))
                print("Gasto excluido")
                break
            else:
                print("ERRO: ID nao encontrado")
                break
            
    # Mostrando as Opcoes de Uso
    def interface(self):
        system("cls")
        print()
        print("Bem-vindo ao Acompanhador de Gastos!")
        print()
        for key, item in self.opcs.items():
            print(f"{item} - {key}")
            
    def programa(self):
        self.interface()
        self.acoes_em_funcoes()


if __name__ == "__main__":
    acom_gastos = Project()
    system("cls")
    print("Saindo...")
    time.sleep(1)
