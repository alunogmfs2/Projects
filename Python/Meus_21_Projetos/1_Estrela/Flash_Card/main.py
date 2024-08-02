from random import randint
from time import sleep

flash_cards = [
    {"pergunta": "Qual é a capital da França?", "resposta": "Paris"},
    {"pergunta": "Quem pintou a Mona Lisa?", "resposta": "Leonardo da Vinci"},
    {"pergunta": "Qual é a fórmula química da água?", "resposta": "H2O"},
    {"pergunta": "Quem escreveu 'Romeu e Julieta'?", "resposta": "William Shakespeare"},
    {"pergunta": "Qual é o maior planeta do sistema solar?", "resposta": "Júpiter"},
    {"pergunta": "Em que ano o homem pisou na lua pela primeira vez?", "resposta": "1969"},
    {"pergunta": "Qual é o elemento químico de símbolo 'O'?", "resposta": "Oxigênio"},
    {"pergunta": "Quem descobriu a penicilina?", "resposta": "Alexander Fleming"},
    {"pergunta": "Qual é a capital do Japão?", "resposta": "Tóquio"},
    {"pergunta": "Quem foi o primeiro presidente dos Estados Unidos?", "resposta": "George Washington"},
    {"pergunta": "Qual é a fórmula química do dióxido de carbono?", "resposta": "CO2"},
    {"pergunta": "Qual é a montanha mais alta do mundo?", "resposta": "Monte Everest"},
    {"pergunta": "Quem pintou o teto da Capela Sistina?", "resposta": "Michelangelo"},
    {"pergunta": "Qual é o órgão do corpo humano responsável por bombear o sangue?", "resposta": "Coração"},
    {"pergunta": "Em que continente fica o Egito?", "resposta": "África"},
    {"pergunta": "Qual é o número atômico do hidrogênio?", "resposta": "1"},
    {"pergunta": "Quem foi o autor de 'Dom Quixote'?", "resposta": "Miguel de Cervantes"},
    {"pergunta": "Qual é o maior oceano do mundo?", "resposta": "Oceano Pacífico"},
    {"pergunta": "Qual é a língua oficial do Brasil?", "resposta": "Português"},
    {"pergunta": "Quem desenvolveu a teoria da relatividade?", "resposta": "Albert Einstein"},
    {"pergunta": "Qual é a moeda oficial do Reino Unido?", "resposta": "Libra esterlina"},
    {"pergunta": "Quem compôs a Nona Sinfonia?", "resposta": "Ludwig van Beethoven"},
    {"pergunta": "Qual é a capital da Austrália?", "resposta": "Canberra"},
    {"pergunta": "Em que ano começou a Segunda Guerra Mundial?", "resposta": "1939"},
    {"pergunta": "Qual é o rio mais longo do mundo?", "resposta": "Rio Nilo"},
    {"pergunta": "Quem escreveu 'A Origem das Espécies'?", "resposta": "Charles Darwin"},
    {"pergunta": "Qual é o país mais populoso do mundo?", "resposta": "China"},
    {"pergunta": "Qual é o nome do cientista que formulou as Leis de Newton?", "resposta": "Isaac Newton"},
    {"pergunta": "Quem foi a primeira mulher a ganhar um Prêmio Nobel?", "resposta": "Marie Curie"},
    {"pergunta": "Qual é o símbolo químico do ouro?", "resposta": "Au"}
]

print("")
print("Bem vindo ao Flash Cards")
print("")

contador = 0

while contador != 20:
    pergunta = randint(0, len(flash_cards) - 1)

    sleep(1)

    res = input(f"{flash_cards[pergunta]['pergunta']} ")

    if res == flash_cards[pergunta]["resposta"]:
        print("")
        print("Parabéns, resposta certa")
        print("")
    else:
        print("")
        print("Você errou, mas na próxima você consegue")
        print(f"A resposta é {flash_cards[pergunta]['resposta']}")
        print("")

    contador += 1
    flash_cards.pop(pergunta)
