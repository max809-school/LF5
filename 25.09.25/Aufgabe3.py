def getFloatInput(prompt_text):
    while True:
        try:
            return float(input(prompt_text))
        except ValueError:
            print("Das ist keine Zahl.")


def getSelectInput(prompt_text, options):
    while True:
        print(prompt_text)
        for idx, option in enumerate(options, 1):
            print(f"{idx}. {option}")
        try:
            choice = int(input("Bitte wählen Sie eine Option (Zahl eingeben): "))
            if 1 <= choice <= len(options):
                return options[choice - 1]
            else:
                print("Bitte eine gültige Zahl aus der Liste wählen.")
        except ValueError:
            print("Das ist keine Zahl.")


def getInput():
    liters = getFloatInput("Die Liter: ")
    select = getSelectInput("Die Auswahl: ", ["Benzin", "Diesel"])
    return {"liters": liters, "select": select}


schema = {
    "Benzin": {
        "price": 1.36,
    },
    "Diesel": {
        "price": 1.28,
    },
}


def calcAndPrint():
    inputs = getInput()
    liters = inputs["liters"]
    select = inputs["select"]
    netto = liters * schema[select]["price"]
    mwst = netto * 0.19
    brutto = netto + mwst

    print("-" * 60)
    print(f"{'Bezeichnung':<25}{'Wert':<30}")
    print("-" * 60)
    print(f"{'Liter':<25}{liters:<30}")
    print(f"{'Kraftstoffart':<25}{select:<30}")
    print(f"{'Preis pro Liter':<25}{schema[select]['price']:.2f} €")
    print(f"{'Gesamtpreis Netto':<25}{netto:.2f} €")
    print(f"{'MwSt (19%)':<25}{mwst:.2f} €")
    print(f"{'Gesamtpreis Brutto':<25}{brutto:.2f} €")
    print("-" * 60)


if __name__ == "__main__":
    calcAndPrint()
