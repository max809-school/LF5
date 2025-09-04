def getInputs():
    print("-" * 20)

    dividend_str = input("Dividend: ")
    if not dividend_str.isdigit():
        raise ValueError("Der Dividend ist keine Zahl")
    dividend = int(dividend_str)

    divisor_str = input("Divisor: ")
    if not divisor_str.isdigit():
        raise ValueError("Der Divisor ist keine Zahl")
    divisor = int(divisor_str)

    return dividend, divisor


def integer_division_with_remainder(dividend, divisor):
    quotient = dividend // divisor
    remainder = dividend % divisor
    return quotient, remainder


def printResult():
    dividend, divisor = getInputs()
    quotient, remainder = integer_division_with_remainder(dividend, divisor)
    print("-" * 20)
    print("Ganzzahlige Division mit Rest\n")
    print(f"Dividend: {dividend}\n")
    print(f"Divisor: {divisor}\n")
    print(
        f"Das Ergebnis der Division {dividend}:{divisor} ist {quotient} Rest {remainder}\n"
    )
    print("Programmende Ganzzahldivision.\n")
    print("-" * 20)


try:
    printResult()
except ValueError as e:
    print(e)
except ZeroDivisionError:
    print("Division durch 0 ist nicht erlaubt")
except KeyboardInterrupt:
    print("\n\nEingabe Abgebrochen")
