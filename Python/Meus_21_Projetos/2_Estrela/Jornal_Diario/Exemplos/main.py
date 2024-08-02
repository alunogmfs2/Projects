import os
import sqlite3
from sqlite3 import Error

# Conexao
def ConexaoBanco():
    caminho = "E:\\Programacao\\Projetos\\Projects\\Python\\Meus_21_Projetos\\2_Estrela\\Jornal_Diario\\Database\\agenda.db"

    con = None
    
    try:
        con = sqlite3.connect(caminho)
    except Error as e:
        print(e)

    return con


vcon = ConexaoBanco()

def query(conexao, sql, dados=None):
    try:
        c = conexao.cursor()
        if dados:
            c.execute(sql, dados)
        else:
            c.execute(sql)
        conexao.commit()
    except Error as e:
        print(e)


def consultar(conexao, sql, dados=None):
    try:
        c = conexao.cursor()
        if dados:
            c.execute(sql, dados)
        else:
            c.execute(sql)
        res = c.fetchall()
        return res
    except Error as e:
        print(e)
        return None


def menuPrincipal():
    os.system("cls" if os.name == "nt" else "clear")

    print("1 - Inserir Novo Registro")
    print("2 - Deletar Registro")
    print("3 - Atualizar Registro")
    print("4 - Consultar Registro")
    print("5 - Consultar Registro por Nome")
    print("0 - Sair")


def menuInserir():
    os.system("cls" if os.name == "nt" else "clear")
    vnome = input("Digite o Nome: ")
    vtelefone = input("Digite o Telefone: ")
    vemail = input("Digite o Email: ")
    vsql = "INSERT INTO tb_contatos (T_NOMECONTATO, T_TELEFONECONTATO, T_EMAILCONTATO) VALUES (?, ?, ?)"
    query(vcon, vsql, (vnome, vtelefone, vemail))


def menuDeletar():
    os.system("cls" if os.name == "nt" else "clear")
    vid = input("Digite o ID do Registro a ser deletado: ")
    vsql = "DELETE FROM tb_contatos WHERE N_IDCONTATO=?"
    query(vcon, vsql, (vid,))


def menuAtualizar():
    os.system("cls" if os.name == "nt" else "clear")
    vid = input("Digite o ID do Registro a ser atualizado: ")
    r = consultar(vcon, "SELECT * FROM tb_contatos WHERE N_IDCONTATO=?", (vid,))
    if r:
        rnome = r[0][1]
        rtelefone = r[0][2]
        remail = r[0][3]
        vnome = input(f"Digite o Nome [{rnome}]: ") or rnome
        vtelefone = input(f"Digite o Telefone [{rtelefone}]: ") or rtelefone
        vemail = input(f"Digite o Email [{remail}]: ") or remail
        vsql = "UPDATE tb_contatos SET T_NOMECONTATO=?, T_TELEFONECONTATO=?, T_EMAILCONTATO=? WHERE N_IDCONTATO=?"
        query(vcon, vsql, (vnome, vtelefone, vemail, vid))
    else:
        print("Registro não encontrado")
    os.system("pause" if os.name == "nt" else "read -n1 -r -p 'Pressione qualquer tecla para continuar...'")


def menuConsultar():
    os.system("cls" if os.name == "nt" else "clear")
    vsql = "SELECT * FROM tb_contatos"
    res = consultar(vcon, vsql)
    if res:
        vlim = 10
        vcont = 0
        for r in res:
            print(f"ID: {r[0]: <3} Nome: {r[1]: <30} Telefone: {r[2]: <30} Email: {r[3]: <30}")
            vcont += 1
            if vcont >= vlim:
                vcont = 0
                os.system("pause" if os.name == "nt" else "read -n1 -r -p 'Pressione qualquer tecla para continuar...'")
                os.system("cls" if os.name == "nt" else "clear")
        print("Fim da Lista")
    else:
        print("Nenhum registro encontrado")
    os.system("pause" if os.name == "nt" else "read -n1 -r -p 'Pressione qualquer tecla para continuar...'")


def menuConsultarNome():
    os.system("cls" if os.name == "nt" else "clear")
    vnome = input("Digite o Nome: ")
    vsql = "SELECT * FROM tb_contatos WHERE T_NOMECONTATO LIKE ?"
    res = consultar(vcon, vsql, ('%' + vnome + '%',))
    if res:
        vlim = 10
        vcont = 0
        for r in res:
            print(f"ID: {r[0]: <3} Nome: {r[1]: <30} Telefone: {r[2]: <30} Email: {r[3]: <30}")
            vcont += 1
            if vcont >= vlim:
                vcont = 0
                os.system("pause" if os.name == "nt" else "read -n1 -r -p 'Pressione qualquer tecla para continuar...'")
                os.system("cls" if os.name == "nt" else "clear")
        print("Fim da Lista")
    else:
        print("Nenhum registro encontrado")
    os.system("pause" if os.name == "nt" else "read -n1 -r -p 'Pressione qualquer tecla para continuar...'")


opc = -1

while opc != 0:
    menuPrincipal()
    opc = int(input("Escolha uma opção: "))
    if opc == 1:
        menuInserir()
    elif opc == 2:
        menuDeletar()
    elif opc == 3:
        menuAtualizar()
    elif opc == 4:
        menuConsultar()
    elif opc == 5:
        menuConsultarNome()
    elif opc == 0:
        os.system("cls" if os.name == "nt" else "clear")
        print("Saindo...")
    else:
        os.system("cls" if os.name == "nt" else "clear")
        print("Opção inválida!")
    os.system("pause" if os.name == "nt" else "read -n1 -r -p 'Pressione qualquer tecla para continuar...'")

vcon.close()
