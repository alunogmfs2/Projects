import time
from plyer import notification

print("")
print("Bem vindo ao Timer Pomodoro")
print("")

contador = 0

while True:
    comecar = input("Comecar Pomodoro [s/n]: ")
    if comecar == "n" or comecar == "N":
        break

    print("")

    time.sleep(60 * 25)

    if contador == 5:
        notification.notify(
            title="O seu Tempo de Descansar chegou",
            message="O seu Tempo de Concentracao acabou, a pausa de 15 minutos comeca em 10 segundos",
            app_name="Pomodoro Timer",
            timeout=10
        )
        contador = 0
        time.sleep(60 * 15)
    else:
        notification.notify(
            title="O seu Tempo de Descansar chegou",
            message="O seu Tempo de Concentracao acabou, a pausa de 5 minutos comeca em 10 segundos",
            app_name="Pomodoro Timer",
            timeout=10
        )
        time.sleep(60 * 5)

    print("")

    repetir = input("Voce gostaria de repetir [s/n]: ")
    if repetir == "n" or repetir == "N":
        break

    contador += 1
