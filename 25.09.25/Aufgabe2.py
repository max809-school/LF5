import sys


def getFloatInput(prompt_text):
    while True:
        try:
            return float(input(prompt_text))
        except ValueError:
            print("Das ist keine Zahl.")


schema = {
    "segment1": {
        "start": 0,
        "end": 500,
        "percentage": 3.0,
    },
    "segment2": {
        "start": 501,
        "end": 2_147_483_647,  # Maximaler Wert für ein 32-Bit-Integer
        "percentage": 5,
    },
}


def getSegment(value):
    for segment in schema:
        if value >= schema[segment]["start"] and value <= schema[segment]["end"]:
            return segment
    return None


def calcAndPrint(value=None):
    if value is None:
        value = getFloatInput("Der Wert: ")
    else:
        value = int(value)

    segment = getSegment(value)
    print("-" * 60)
    print(f"{'Bezeichnung':<20}{'Wert':<35}")
    print(f"{'Segment':<20}{segment:<35}")
    print(f"{'Prozentsatz':<20}{f'{schema[segment]["percentage"]} %':<35}")
    print(f"{'Wert':<20}{f'{value} €':<35}")
    print(
        f"{'Betrag':<20}{f'{value / 100 * schema[segment]["percentage"]:,.2f} €':<35}"
    )
    print(
        f"{'Zahlungsbetrag':<20}{f'{value / 100 * (100 - schema[segment]["percentage"]):,.2f} €':<35}"
    )
    print("-" * 60)


testValues = [400, 500, 501, 600, 700, 800]

if __name__ == "__main__":
    if "--test" in sys.argv:
        for value in testValues:
            calcAndPrint(value)
    else:
        try:
            calcAndPrint()
        except KeyboardInterrupt:
            print("\n\nEingabe Abgebrochen")
        except ValueError as e:
            print(e)
        except ZeroDivisionError:
            print("Division durch 0 ist nicht erlaubt")
