import re


def getInputs():
    while True:
        firstname = input("Vorname: ")
        if len(firstname) > 0 and firstname.isalpha():
            break
        print("Vorname muss mindestens 1 Zeichen lang sein")

    while True:
        lastname = input("Nachname: ")
        if len(lastname) > 0 and lastname.isalpha():
            break
        print("Nachname muss mindestens 1 Zeichen lang sein")

    while True:
        street = input("Straße: ")
        if len(street) > 0:
            break
        print("Straße muss mindestens 1 Zeichen lang sein")

    while True:
        city = input("Stadt: ")
        if len(city) > 0 and city.isalpha():
            break
        print("Stadt muss mindestens 1 Zeichen lang sein")

    while True:
        zipCode = input("PLZ: ")
        if len(zipCode) > 0 and zipCode.isdigit():
            break
        print("PLZ muss mindestens 1 Zeichen lang sein und darf nur Zahlen enthalten")

    while True:
        birthdate = input("Geburtsdatum (dd.mm.yyyy): ")
        if re.fullmatch(r"\d{2}\.\d{2}\.\d{4}", birthdate):
            break
        print("Geburtsdatum muss im Format dd.mm.yyyy eingegeben werden")

    while True:
        hobbies = input("Hobbies (mindestens 2, getrennt durch Komma): ")
        hobbies_list = [h.strip() for h in hobbies.split(",") if h.strip()]
        if len(hobbies_list) >= 2:
            hobbies = ", ".join(hobbies_list)
            break
        print("Bitte geben Sie mindestens 2 Hobbys ein, getrennt durch ein Komma.")

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
