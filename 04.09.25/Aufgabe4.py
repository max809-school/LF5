def getInputs():
    print("-" * 20)
    print("Widerstands-Parallelschaltung")

    r1_str = input("R1 in Ohm: ")
    if not r1_str.isdigit():
        raise ValueError("R1 ist keine gültige Zahl")
    r1 = float(r1_str)
    if r1 <= 0:
        raise ValueError("R1 muss größer als 0 sein")

    r2_str = input("R2 in Ohm: ")
    if not r2_str.isdigit():
        raise ValueError("R2 ist keine gültige Zahl")
    r2 = float(r2_str)
    if r2 <= 0:
        raise ValueError("R2 muss größer als 0 sein")

    return r1, r2


def parallel_resistance(r1, r2):
    return (r1 * r2) / (r1 + r2)


def printResult():
    r1, r2 = getInputs()
    rg = parallel_resistance(r1, r2)
    print("-" * 20)
    print("Widerstands-Parallelschaltung\n")
    print(f"R1: {r1:.4f} Ohm\n")
    print(f"R2: {r2:.4f} Ohm\n")
    print(f"Der Gesamtwiderstand ist {rg:.4f} Ohm\n")
    print("Programmende ParallelR.\n")
    print("-" * 20)


try:
    printResult()
except ValueError as e:
    print(e)
except ZeroDivisionError:
    print("Division durch 0 ist nicht erlaubt")
except KeyboardInterrupt:
    print("\n\nEingabe Abgebrochen")
