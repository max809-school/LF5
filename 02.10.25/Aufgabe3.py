def getIntInput(prompt_text):
    while True:
        try:
            return int(input(prompt_text))
        except ValueError:
            print("Das ist keine Zahl.")


def main():
    zahl = getIntInput("Gib den Umsatz an: ")

    if zahl > 25_000:
        if zahl <= 50_000:
            return print(f"{(zahl * 0.02):.2f}")
        elif zahl <= 75_000:
            return print(f"{(zahl * 0.03):.2f}")
        elif zahl <= 100_000:
            return print(f"{(zahl * 0.04):.2f}")
        else:
            return print(f"{(zahl * 0.05):.2f}")
    else:
        return None


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nEingabe Abgebrochen")
    except ValueError as e:
        print(e)
