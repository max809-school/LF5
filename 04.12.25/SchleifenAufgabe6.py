def jahre_bis_verdoppelt(kapital, zinssatz):
    zielkapital = kapital * 2
    jahre = 0
    while kapital < zielkapital:
        kapital += kapital * (zinssatz / 100)
        jahre += 1
    return jahre


def main():
    try:
        kapital = float(input("Startkapital eingeben: "))
        zinssatz = float(input("Zinssatz in % pro Jahr eingeben: "))
        jahre = jahre_bis_verdoppelt(kapital, zinssatz)
        print(f"Das Kapital hat sich nach {jahre} Jahren verdoppelt.")
    except ValueError:
        print("Bitte geben Sie gültige Zahlen ein.")


if __name__ == "__main__":
    main()
