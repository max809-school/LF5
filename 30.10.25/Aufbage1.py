# Inputs


def getIntInput(prompt_text):
    while True:
        try:
            return int(input(prompt_text))
        except ValueError:
            print("Das ist keine Zahl.")


def getFloatInput(prompt_text):
    while True:
        try:
            return float(input(prompt_text))
        except ValueError:
            print("Das ist keine Zahl.")


def getInputs():
    import sys

    if "-y" in sys.argv:
        last_month_salary = 2000
        children_count = 2
        years = 14
        days_absent = 12
        return {
            "last_month_salary": last_month_salary,
            "children_count": children_count,
            "years": years,
            "days_absent": days_absent,
        }

    last_month_salary = getFloatInput("Letzter Monatslohn: ")
    children_count = getIntInput("Anzahl der Kinder: ")
    years = getIntInput("Anzahl der Jahre im Betrieb: ")
    days_absent = getIntInput("Anzahl der Abwesenheiten: ")

    return {
        "last_month_salary": last_month_salary,
        "children_count": children_count,
        "years": years,
        "days_absent": days_absent,
    }


def main():
    inputs = getInputs()
    bonus = 0

    # Weniger als 3 Jahre im Betrieb
    if inputs["years"] < 3 and inputs["days_absent"] <= 2:
        # 10% of last month's salary
        bonus = inputs["last_month_salary"] * 0.10

    # Mehr als 3 Jahre im Betrieb
    elif inputs["years"] >= 3 and inputs["years"] < 10:
        # wenn weniger als 20 Abwesenheiten, dann 15% von letztem Monatslohn
        if inputs["days_absent"] < 20:
            bonus = inputs["last_month_salary"] * 0.15

        else:
            bonus = inputs["last_month_salary"] * 0.10
    elif inputs["years"] >= 10:
        bonus = inputs["last_month_salary"] * 1

    if inputs["children_count"] > 0:
        bonus = bonus + (50 * inputs["children_count"])

    if bonus > 0:
        print(f"Prämie: {bonus:.2f} €")
    else:
        print("Keine Prämie")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nEingabe Abgebrochen")
    except ValueError as e:
        print(e)
