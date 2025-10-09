def getIntInput(prompt_text):
    while True:
        try:
            return int(input(prompt_text))
        except ValueError:
            print("Das ist keine Zahl.")


def main():
    zahl = getIntInput("Gib deine zahl an: ")

    if 10 <= zahl <= 18:
        print("Eingabe korrekt!")
    else:
        print("Eingabe falsch!")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nEingabe Abgebrochen")
    except ValueError as e:
        print(e)
