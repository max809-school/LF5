def getInputs():
    print("-" * 20)
    print("Eingabe der Zahlen")

    num1_as_string = input("Gib die erste Zahl ein: ")
    if not num1_as_string.isdigit():
        raise ValueError("Die erste Zahl ist keine Zahl")
    num1 = float(num1_as_string)
    num2_as_string = input("Gib die zweite Zahl ein: ")
    if not num2_as_string.isdigit():
        raise ValueError("Die zweite Zahl ist keine Zahl")
    num2 = float(num2_as_string)
    return num1, num2


def divide(num1, num2):
    return num1 / num2


def printResult():
    num1, num2 = getInputs()
    result = divide(num1, num2)
    print("-" * 20)
    print("Division zweier Zahlen\n")
    print(f"Zahl1: {num1}\n")
    print(f"Zahl2: {num2}\n")
    print(f"Das Ergebnis der Division {num1}/{num2} ist {result}\n")
    print("Programmende Division.\n")
    print("-" * 20)


try:
    printResult()
except ValueError as e:
    print(e)
except ZeroDivisionError:
    print("Division durch 0 ist nicht erlaubt")
except KeyboardInterrupt:
    print("\n\nEingabe Abgebrochen")
