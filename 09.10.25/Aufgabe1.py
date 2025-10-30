def getFloatInput(prompt_text):
    while True:
        try:
            return float(input(prompt_text))
        except ValueError:
            print("Das ist keine Zahl.")


schema = {
    "segment1": {
        "start": 0,
        "end": 48_000,
        "percentage": 10.0,
    },
    "segment2": {
        "start": 48_001,
        "end": 75_000,
        "percentage": 20.0,
    },
    "segment3": {
        "start": 75_001,
        "end": 2_147_483_647,  # Maximaler Wert für ein 32-Bit-Integer
        "percentage": 30.0,
    },
}


def getSegment(revenue):
    for segment in schema:
        if revenue >= schema[segment]["start"] and revenue <= schema[segment]["end"]:
            return segment
    return None


def main():
    income = getFloatInput("Gib dein Einkommen ein: ")

    segment = getSegment(income)
    print("-" * 20)
    print(f"{'Dein Einkommen liegt ist:':<30} {income:>25.2f}")
    print(
        f"{'Dein Steuersatz beträgt:':<30} {f'{schema[segment]["percentage"]} %':>25}"
    )
    print(
        f"{'Dein Steuerbetrag beträgt:':<30} {f'{income * schema[segment]["percentage"] / 100:,.2f} €':>25}"
    )
    print("-" * 20)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nEingabe Abgebrochen")
    except ValueError as e:
        print(e)
    except ZeroDivisionError:
        print("Division durch 0 ist nicht erlaubt")
