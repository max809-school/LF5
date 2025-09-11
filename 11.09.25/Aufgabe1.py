def getFloatInput(prompt_text):
    while True:
        try:
            return float(input(prompt_text))
        except ValueError:
            print("Das ist keine Zahl.")


def getInput():
    import sys

    if "-y" in sys.argv:
        brutto_income = 2456
        income_tax = 625.6
        return {"brutto_income": brutto_income, "income_tax": income_tax}

    brutto_income = getFloatInput("Das Bruttoeinkommen:")
    income_tax = getFloatInput("Die Lohnsteuer:")

    return {"brutto_income": brutto_income, "income_tax": income_tax}


def calcAndPrint():
    inputs = getInput()

    brutto_income = inputs["brutto_income"]
    income_tax = inputs["income_tax"]

    # 9.0 % of income_tax
    church_tax = income_tax * 0.090

    #  5.5 of income_tax
    solidarity_tax = income_tax * 0.055

    # sum of all taxes
    sum_of_tax = church_tax + solidarity_tax + income_tax

    # SV
    # 18,6 % of brutto_income / 2
    pension_insurance = (brutto_income * 0.186) / 2

    # 14.0 % of brutto_income / 2
    health_insurance = (brutto_income * 0.140) / 2

    # 2.4 % of brutto_income / 2
    unemployment_insurance = (brutto_income * 0.024) / 2

    # 3.3 % of brutto_income / 2
    care_insurance = (brutto_income * 0.033) / 2

    sum_of_sv = (
        pension_insurance + health_insurance + unemployment_insurance + care_insurance
    )

    # netto income
    netto_income = brutto_income - sum_of_tax - sum_of_sv

    personnel_expenditure = brutto_income + sum_of_sv

    print(f"{'Programm Gehaltsabrechnung':^60}")
    print(f"{'Bezeichnung':<30}{'Betrag (€)':>15}{'Summe (€)':>15}")
    print(f"{'Bruttogehalt':<30}{brutto_income:>15.2f}")
    print(f"{'Lohnsteuer (lt. Tabelle)':<30}{income_tax:>15.2f}")
    print(f"{'Kirchensteuer':<30}{church_tax:>15.2f}")
    print(f"{'Solidaritätszuschlag':<30}{solidarity_tax:>15.2f}{sum_of_tax:>15.2f}")
    print(f"{'AN-Anteil zu Sozialversicherung':<30}")
    print(f"{'Rentenversicherung':<30}{pension_insurance:>15.2f}")
    print(f"{'Krankenversicherung':<30}{health_insurance:>15.2f}")
    print(f"{'Arbeitslosenversicherung':<30}{unemployment_insurance:>15.2f}")
    print(f"{'Pflegeversicherung':<30}{care_insurance:>15.2f}{sum_of_sv:>15.2f}")
    print(f"{'Nettogehalt':<30}{netto_income:>30.2f}")
    print(f"{'Personalkosten':<30}{personnel_expenditure:>30.2f}")


if __name__ == "__main__":
    try:
        calcAndPrint()
    except KeyboardInterrupt:
        print("\n\nEingabe Abgebrochen")
    except ValueError as e:
        print(e)
    except ZeroDivisionError:
        print("Division durch 0 ist nicht erlaubt")
