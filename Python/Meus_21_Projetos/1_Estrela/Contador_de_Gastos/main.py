def espaco(vezes=157):
    print("-" * vezes)


gastos = {
    "diario": {
        "programacao": [],
        "maker": [],
        "comida": [],
        "outras_coisas": []
    },
    "semanal": {
        "programacao": [],
        "maker": [],
        "comida": [],
        "outras_coisas": []
    },
    "mensal": {
        "programacao": [],
        "maker": [],
        "comida": [],
        "outras_coisas": []
    },
    "Anual": {
        "programacao": [],
        "maker": [],
        "comida": [],
        "outras_coisas": []
    }
}


def perguntarTipoGasto():
    while True:
        print("Qual Gasto você gostaria de ver: ")
        print("1. Gasto Diario")
        print("2. Gasto Semanal")
        print("3. Gasto Mensal")
        print("4. Gasto Anual")
        espaco()

        try:
            res = int(input(""))
            if 1 <= res <= 4:
                return res
            else:
                espaco()
                print("ERRO: Digite uma Opcao Válida")
                espaco()

        except:
            espaco()
            print("ERRO: Digite um Número Inteiro")
            espaco()


def imprimirGastos():
    tipo = perguntarTipoGasto()
    match tipo:
        case 1:
            print("Categoria\t\t\t\tDia 1\tDia 2\tDia 3\tDia 4\tDia 5\tDia 6\tDia 7\t\tTotal Diário\t\tMédia Diária")
            espaco()
            for chave, item in gastos["diario"].items():
                total = sum(item)
                media = total / 7 if len(item) == 7 else 0  # Calculando a média diária
                if chave != "outras_coisas":
                    print(f"{chave.capitalize()}\t\t\t\t", end="")
                else:
                    print(f"{chave.capitalize()}\t\t\t", end="")
                if chave == "maker" or chave == "comida":
                    print("\t", end="")
                for i in item:
                    print(f"{i:.2f}\t", end="")
                print(f"\t{total:.2f}\t\t\t\t{media:.2f}")

        case 2:
            print("Categoria\t\t\t\tSemana 1\tSemana 2\tSemana 3\tSemana 4\t\tTotal Semanal\t\tMédia Semanal")
            espaco()
            for chave, item in gastos["semanal"].items():
                total = sum(item)
                media = total / 4 if len(item) == 4 else 0  # Calculando a média semanal
                if chave != "outras_coisas":
                    print(f"{chave.capitalize()}\t\t\t\t", end="")
                else:
                    print(f"{chave.capitalize()}\t\t\t", end="")
                if chave == "maker" or chave == "comida":
                    print("\t", end="")
                for i in item:
                    print(f"{i:.2f}\t\t", end="")
                print(f"\t{total:.2f}\t\t\t\t{media:.2f}")
        case 3:
            print("Categoria\t\t\t\tMês 1\tMês 2\tMês 3\tMês 4\tMês 5\tMês 6\tMês 7\tMês 8\tMês 9\tMês 10\tMês 11\tMês 12\t\tTotal Mensal\t\tMédia Mensal")
            espaco()
            for chave, item in gastos["mensal"].items():
                total = sum(item)
                media = total / 12 if len(item) == 12 else 0  # Calculando a média mensal
                if chave != "outras_coisas":
                    print(f"{chave.capitalize()}\t\t\t\t", end="")
                else:
                    print(f"{chave.capitalize()}\t\t\t", end="")
                if chave == "maker" or chave == "comida":
                    print("\t", end="")
                for i in item:
                    print(f"{i:.2f}\t", end="")
                print(f"\t{total:.2f}\t\t\t\t{media:.2f}")
        case 4:
            print(f"Categoria\t\t\t\t", end="")
            for i in range(0, len(list(gastos["Anual"]["programacao"]))):
                print(f"Ano {i+1}\t\t", end="")
            print("Total Anual\t\tMedia Anual")
            espaco()
            for chave, item in gastos["Anual"].items():
                total = sum(item)
                media = total / len(list(gastos["Anual"]["programacao"]))  # Calculando a média mensal
                if chave != "outras_coisas":
                    print(f"{chave.capitalize()}\t\t\t\t", end="")
                else:
                    print(f"{chave.capitalize()}\t\t\t", end="")
                if chave == "maker" or chave == "comida":
                    print("\t", end="")
                for i in item:
                    print(f"{i:.2f}\t\t", end="")
                if chave != "programacao":
                    print(f"{total:.2f}\t\t\t{media:.2f}")
                else:
                    if len(item) == 1:
                        print(f"{total:.2f}\t\t\t{media:.2f}")
                    else:
                        print(f"{total:.2f}\t\t{media:.2f}")

    # print("Categoria\t\t\t\t\tSemana 1\tSemana 2\tSemana 3\tSemana 4\tTotal Mensal")


def telaInicial():
    espaco()
    print("Bem vindo ao Contador de Gastos")
    espaco()

    imprimirGastos()


if __name__ == "__main__":
    telaInicial()
