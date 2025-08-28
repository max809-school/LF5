# Ist immer ein String
name = "Max Mustermann"

# Die Straße und Hausnummer werden zusammen gespeichert, da sie im direkten Zusammenhang stehen.
street = "Musterstrasse 1"

# wird als string gespeichert, da dies nie als int verwendet wird. Außerdem ist können Ints nicht mit 0 beginnen da dies als Oktalzahl interpretiert wird.
zipCode = "10115"
# Der Stadtname ist immer ein String.
city = "Berlin"

# Hier wird nur die Nummer gespeichert, da der string "Telefon:" immer davor steht.
# Dadurch das die Nummer mit 0 beginnt und ein sonderzeichen enthält, wird dies als string gespeichert.
telephone = "0815/123456"


# Print all the data like a letter header
print("------------")
print(f"{name}")
print(f"{street}")
print(f"{zipCode} {city}")
print(f"Telefon: {telephone}")
print("------------")
