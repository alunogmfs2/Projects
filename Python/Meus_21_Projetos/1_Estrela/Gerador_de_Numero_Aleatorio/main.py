from random import random, randint

while True:
    print("")
    tipo = input("Voce gostaria gerar um número de 0 à 1 ou de qualquer número até qualquer número [A/B]: ")

    if tipo == "A":
        num = round(random(), 2)
        print("")
        print(f"O número gerado é {num}")
    elif tipo == "B":
        try:
            print("")
            comeco = int(input("De que Número: "))
            final = int(input("Até que Número: "))
            num = randint(comeco, final)
            print("")
            print(f"O número gerado é {num}")
        except:
            print("")
            print("ERRO: Digite um número inteiro")

    print("")
    continuar = input("Voce gostaria de gerar outro número [s/n]: ")

    if continuar == 'n' or continuar == 'N':
        break
