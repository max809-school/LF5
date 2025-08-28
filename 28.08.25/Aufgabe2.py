import re


def getInputs():
    def promptUntilValid(prompt, validator, error_message):
        value = input(prompt)
        if validator(value):
            return value
        print(error_message)
        return promptUntilValid(prompt, validator, error_message)

    firstname = promptUntilValid(
        "Vorname: ",
        lambda v: len(v) > 0 and v.isalpha(),
        "Vorname muss mindestens 1 Zeichen lang sein",
    )

    lastname = promptUntilValid(
        "Nachname: ",
        lambda v: len(v) > 0 and v.isalpha(),
        "Nachname muss mindestens 1 Zeichen lang sein",
    )

    street = promptUntilValid(
        "Straße: ",
        lambda v: len(v) > 0,
        "Straße muss mindestens 1 Zeichen lang sein",
    )

    city = promptUntilValid(
        "Stadt: ",
        lambda v: len(v) > 0 and v.isalpha(),
        "Stadt muss mindestens 1 Zeichen lang sein",
    )

    zipCode = promptUntilValid(
        "PLZ: ",
        lambda v: len(v) > 0 and v.isdigit(),
        "PLZ muss mindestens 1 Zeichen lang sein und darf nur Zahlen enthalten",
    )

    birthdate = promptUntilValid(
        "Geburtsdatum (dd.mm.yyyy): ",
        lambda v: re.fullmatch(r"\d{2}\.\d{2}\.\d{4}", v) is not None,
        "Geburtsdatum muss im Format dd.mm.yyyy eingegeben werden",
    )

    def hobbies_validator(v):
        return len([h.strip() for h in v.split(",") if h.strip()]) >= 2

    hobbies_raw = promptUntilValid(
        "Hobbies (mindestens 2, getrennt durch Komma): ",
        hobbies_validator,
        "Bitte geben Sie mindestens 2 Hobbys ein, getrennt durch ein Komma.",
    )
    hobbies_list = [h.strip() for h in hobbies_raw.split(",") if h.strip()]
    hobbies = ", ".join(hobbies_list)

    return {
        "firstname": firstname,
        "lastname": lastname,
        "street": street,
        "zipCode": zipCode,
        "city": city,
        "birthdate": birthdate,
        "hobbies": hobbies,
    }


try:
    data = getInputs()
    print("\nL E B E N S L A U F")
    print("-" * 20)
    print(f"Name: \t\t{data['firstname'].capitalize()} {data['lastname'].capitalize()}")
    print(f"Straße: \t{data['street'].capitalize()}")
    print(f"Ort: \t\t{data['zipCode']} {data['city'].capitalize()}\n")
    print(f"Geburtsdatum: \t{data['birthdate']}\n")
    print(f"Hobbies: \t{data['hobbies'].capitalize()}\n")


except KeyboardInterrupt:
    print("\n\nEingabe Abgebrochen")
