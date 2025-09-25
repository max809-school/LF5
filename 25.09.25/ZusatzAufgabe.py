import sys


def getNumberInput(prompt_text):
    while True:
        try:
            return int(input(prompt_text))
        except ValueError:
            print("Das ist keine Zahl.")


def getInput():
    revenue = getNumberInput("Der Umsatz:")

    return {"revenue": revenue}


schema = {
    "segment1": {
        "start": 25_000,
        "end": 50_000,
        "percentage": 2,
    },
    "segment2": {
        "start": 50_001,
        "end": 75_000,
        "percentage": 3,
    },
    "segment3": {
        "start": 75_001,
        "end": 100_000,
        "percentage": 4,
    },
    "segment4": {
        "start": 100_001,
        "end": 125_000,
        "percentage": 5,
    },
}


def getSegment(revenue):
    for segment in schema:
        if revenue >= schema[segment]["start"] and revenue <= schema[segment]["end"]:
            return segment
    return None


def calcAndPrint(revenue=None):
    if revenue is None:
        inputs = getInput()
        revenue = inputs["revenue"]
    else:
        revenue = int(revenue)

    segment = getSegment(revenue)
    print("-" * 60)
    print(f"{'Bezeichnung':<25}{'Wert':>20}{'Bemerkung':>15}")
    print(f"{'Segment':<25}{segment:>20}{'':>15}")
    print(f"{'Prozentsatz':<25}{schema[segment]['percentage']:>20.2f}{'%':>15}")
    print(f"{'Umsatz':<25}{revenue:>20,.2f}{'€':>15}")
    print(
        f"{'Betrag':<25}{revenue / 100 * schema[segment]['percentage']:>20,.2f}{'€':>15}"
    )
    print("-" * 60)


testValues = [33_400, 63_400, 75_000, 110_234, 125_000]

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
