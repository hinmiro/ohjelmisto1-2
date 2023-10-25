flag = True
airports = {"EFHK": "Helsinki-Vantaa lentoasema",
            "EDDF": "Frankfurt lentoasema",
            "LTFM": "Istanbul lensoasema"}
print("Lentoasema hakemisto\n")

while flag:
    try:
        choice = int(input("\nSyötä uusi lentoasema(1)\nHae lentoaseman tiedot(2)\nLopeta ohjelma(3): "))

        if choice == 3:
            print("Lopetit ohjelman.")
            flag = False

        elif choice == 1:
            new_icao = input("Anna uuden lentoaseman ICAO-koodi: ").upper()
            new_airport = input("\nAnna uuden lentoaseman nimi: ")
            airports[new_icao] = new_airport

        elif choice == 2:
            icao = input("Haetaan lentoasema ICAO-koodilla: ").upper()
            print(f"\nHaetun lentoaseman nimi on {airports[icao]}")

    except ValueError:
        print("Virheellinen valinta.")
