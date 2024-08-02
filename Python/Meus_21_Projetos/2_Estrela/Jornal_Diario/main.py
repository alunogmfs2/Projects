import sqlite3
from sqlite3 import Error


def ConexaoBanco():
    caminho = "E:\\Banco_de_Dados\\Projetos\\Teste\\teste.db"
    con = None

    try:
        con = sqlite3.connect(caminho)
    except Error as e:
        print(e)

    return con


vcon = ConexaoBanco()

# vsql = """CREATE TABLE tb_contatos(
#             N_IDCONTATO INTEGER PRIMARY KEY AUTOINCREMENT,
#             T_NOMECONTATO VARCHAR(30),
#             T_TELEFONECONTATO VARCHAR(30),
#             T_EMAILCONTATO VARCHAR(30)
#           );"""


# def criarTabela(conexao, sql):
#     try:
#         c = conexao.cursor()
#         c.execute(sql)
#         print("Tabela Criada")
#     except Error as e:
#         print(e)
#
#
# criarTabela(vcon, vsql)

# vcon.close()

nome = input("Digite o Nome: ")
telefone = input("Digite o Telefone: ")
email = input("Digite o Email: ")

vsql = "INSERT INTO tb_contatos (T_NOMECONTATO, T_TELEFONECONTATO, T_EMAILCONTATO) VALUES('"+nome+"', '"+telefone+"', '"+email+"')"
print(vsql)


def inserir(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
        print("Registro inserido")
    except Error as e:
        print(e)


def deletar(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
        print("Registro removido")
    except Error as e:
        print(e)


inserir(vcon, vsql)

vsql = "DE"
