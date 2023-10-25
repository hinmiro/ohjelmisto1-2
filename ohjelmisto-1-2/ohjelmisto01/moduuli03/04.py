year = int(input("Anna vuosiluku: "))

if year % 4 == 0 and year % 100 != 0 or 100 and 400 == 0:
    print(f"{year} on karkausvuosi.")
else:
    print(f"{year} ei ole karkausvuosi.")
