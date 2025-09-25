def getFloatInput(prompt_text):
    while True:
        try:
            return float(input(prompt_text))
        except ValueError:
            print("Das ist keine Zahl.")


def getInput():
    temperature = getFloatInput("Die Temperatur: ")
    return {"temperature": temperature}


def calcAndPrint():
    inputs = getInput()
    temperature = inputs["temperature"]

    if temperature >= 30:
        print("Heute ist ein schöner Tag!")


if __name__ == "__main__":
    calcAndPrint()
