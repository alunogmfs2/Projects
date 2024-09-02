from os import system

operations: list[str] = ["Addieren", "Subtrahieren", "Multiplizieren", "Dividieren", "Hoch-Rechnen"]
con: bool = True

num1: float = 0
num2: float = 0
result: float = 0


def menu() -> None:
    system("cls")
    print("Willkommen in Taschenrechner")
    print()
    print(" 0 - Ende")
    for i, op in enumerate(operations):
        print(f' {i+1} - {op}')
    print()

def descision() -> None:
    while True:
        try:
            choice: int = int(input("Wahl: "))
            if choice > len(operations) or choice < 0:
                raise ValueError
            break
        except ValueError:
            print("\033[31mFalsche Eingabe. Bitte geben Sie eine gültige Zahl ein.\033[m")
            print()
            continue
    translateDescision(choice)
    system("pause")

def translateDescision(descision: int) -> None:
    global con
    match descision:
        case 0:
            con = False
        case 1:
            add()
        case 2:
            minus()
        case 3:
            multiply()
        case 4:
            divide()
        case 5:
            power()

def continueWithResult(res: float) -> None:
    global result, num1
    while True:
        system("cls")
        choice: str = input("Wollen Sie weiter rechnen mit diesem Zahl [J/N]? ").lower()
        print()
        
        if choice != "j" and choice != "n":
            print("\033[31mFalsche Eingabe, geben Sie eine gültige Wahl ein.\033[m")
            print()
            system("pause")
            continue
        
        if choice != "n":
            result = res
            num1 = result
        else:
            result = 0
            num1 = 0
        break

def numbers() -> tuple[int]:
    while True:
        system("cls")
        try:
            if not num1:
                n1 = float(input("Geben Sie den ersten Zahl ein: "))
            else:
                n1 = num1
                print(f"Erster Zahl: {n1}")
            n2 = float(input("Geben Sie den zweiten Zahl ein: "))
            print()
            return n1, n2
        except ValueError:
            print("\033[31mFalsche Eingabe, geben Sie eine Zahl ein\033[m")
            print()
            system("pause")

def add() -> None:
    num1, num2 = numbers()
    result: float = num1 + num2
    print(f"{num1} + {num2} = {result}")
    system("pause")
    continueWithResult(result)
    print()

def minus() -> None:
    num1, num2 = numbers()
    result: float = num1 - num2
    print(f"{num1} - {num2} = {result}")
    system("pause")
    continueWithResult(result)
    print()

def multiply() -> None:
    num1, num2 = numbers()
    result: float = num1 * num2
    print(f"{num1} * {num2} = {result}")
    system("pause")
    continueWithResult(result)
    print()

def divide() -> None:
    while True:
        num1, num2 = numbers()
        if num2 == 0:
            print("\033[31mEs kann nicht durch 0 geteilt werden.\033[m")
            system("pause")
            continue
        result: float = num1 / num2
        print(f"{num1} : {num2} = {result}")
        system("pause")
        continueWithResult(result)
        print()
        break

def power() -> None:
    while True:
        num1, num2 = numbers()
        if num2 > 20 or num1 > 10**20:
            print("\033[31mEs kann nicht hoch-gerechnet werden, weil die Zahl zu groß ist.\033[m")
            system("pause")
            continue
        
        result: float = num1 ** num2
        print(f"{num1} ^ {num2} = {result}")
        system("pause")
        continueWithResult(result)
        print()
        break


while con:
    menu()
    descision()
