names = set()
flag = True

while flag:
    name = input("Anna nimi (lopeta rivinvaihdolla): ")
    if name == "":
        flag = False
    else:
        if name not in names:
            names.add(name)
            print("Uusi nimi lisätty.")
        else:
            print("Antamasi nimi on jo syötetty.")

for i in names:
    print(i)
