def getInputs():
    num1_as_string = input("Gib die erste Zahl ein: ")
    if not num1_as_string.isdigit():
        raise ValueError("Die erste Zahl ist keine Zahl")
    num1 = int(num1_as_string)
    num2_as_string = input("Gib die zweite Zahl ein: ")
    if not num2_as_string.isdigit():
        raise ValueError("Die zweite Zahl ist keine Zahl")
    num2 = int(num2_as_string)
    return num1, num2


def subtract(num1, num2):
    return num1 - num2


def printResult():
    num1, num2 = getInputs()
    result = subtract(num1, num2)
    print("-" * 20)
    print("Subtraktion zweier Zahlen\n")
    print(f"Zahl1: {num1}\n")
    print(f"Zahl2: {num2}\n")
    print(f"Das Ergebnis der Subtraktion {num1}-{num2} ist {result}\n")
    print("Programmende Subtraktion.\n")
    print("-" * 20)


try:
    printResult()
except ValueError as e:
    print(e)
except KeyboardInterrupt:
    print("\n\nEingabe Abgebrochen")
