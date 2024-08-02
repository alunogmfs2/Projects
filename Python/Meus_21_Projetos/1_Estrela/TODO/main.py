import ast


def espaco(vezes=1):
    for i in range(vezes):
        print()


def linha(vezes=40):
    for i in range(vezes):
        print("-", end="")
    print("\n")


todos = []
continuar = True


def adicionarTODO(todo, feito, index):
    todos.append([index, feito, todo])


def perguntarTODO(tipo):
    global todos
    if tipo == 1:
        while True:
            todo = input("Novo TODO: ")
            if len(todos) == 0:
                adicionarTODO(todo, False, len(todos) + 1)
            else:
                adicionarTODO(todo, False, len(todos) + 1)

            res = input("Criar mais um TODO [s/n]: ")
            if res == "n" or res == "N":
                break
            espaco()
    elif tipo == 2:
        while True:
            try:
                todo = int(input("Digite o número do TODO que voce gostaria de editar: "))
                try:
                    todos[todo - 1] = todos[todo - 1]

                    novo_todo = input("Digite seu novo TODO: ")

                    todos[todo - 1][2] = novo_todo

                    break
                except:
                    print("ERRO: Digite um TODO válido")
            except:
                print("ERRO: Digite um número")
        espaco()
    elif tipo == 3:
        while True:
            try:
                todo = int(input("Digite o número do TODO que voce gostaria de excluir: "))
                try:
                    todos.pop(todo - 1)
                    for Todo in todos:
                        Todo[0] = todos.index(Todo) + 1
                    espaco()
                    print(f"TODO {todo} excluido")
                    break
                except:
                    print("ERRO: Digite um TODO válido")
            except:
                print("ERRO: Digite um número")
        espaco()
    elif tipo == 4:
        while True:
            try:
                todo = int(input("Digite o número do TODO que voce gostaria de marcar como Concluido: "))
                try:
                    todos[todo - 1][1] = True
                    print(f"TODO {todo} concluido")
                    break
                except:
                    print("ERRO: Digite um TODO válido")
            except:
                print("ERRO: Digite um número")
        espaco()
    else:
        print("Opcao nao disponível")
        espaco()


def TODOS():
    for todo in todos:
        if todo[1]:
            print(f"{todo[0]}. {comCheck()} {todo[2]}")
        else:
            print(f"{todo[0]}. {semCheck()} {todo[2]}")


def menu():
    espaco()
    print("Acoes possíveis: ")
    print("1. Criar novo TODO")
    print("2. Editar TODO ")
    print("3. Excluir TODO ")
    print("4. Marcar TODO como concluido ")
    print("0. Sair ")
    espaco()

    res = input("O que voce gostaria de fazer: ")

    espaco()

    while True:
        match res:
            case "1":
                return 1
            case "2":
                return 2
            case "3":
                return 3
            case "4":
                return 4
            case "0":
                return 0
            case _:
                print("ERRO: Opcao nao é válida")


def semCheck():
    return "□"


def comCheck():
    return "☑"


def salvar():
    with open("TODOS.txt", "w") as arquivo:
        arquivo.write(f"{todos}")


def ler():
    global todos
    with open("TODOS.txt", "r") as arquivo:
        todos = arquivo.read()
    todos = ast.literal_eval(todos)


def telaInicial():
    global continuar
    linha()
    print("Bem vindo à Lista TODO")
    espaco()
    print("TODOs: ")
    TODOS()
    espaco()

    des = menu()

    match des:
        case 1:
            perguntarTODO(1)
        case 2:
            perguntarTODO(2)
        case 3:
            perguntarTODO(3)
        case 4:
            perguntarTODO(4)
        case 0:
            continuar = False

    linha()




if __name__ == "__main__":
    ler()
    while continuar:
        telaInicial()
    salvar()
