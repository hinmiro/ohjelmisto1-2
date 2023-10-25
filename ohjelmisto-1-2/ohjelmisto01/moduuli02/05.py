import math

leivat = input("Anna leiviskät: ")
naulat = input("Anna naulat: ")
luodit = input("Anna luodit: ")

paino_luoti = 13.3
paino_naula = paino_luoti * 32
paino_leivat = paino_naula * 20

result_g = (paino_luoti * float(luodit)) + (paino_naula * float(naulat)) + (paino_leivat * float(leivat))

result_kg = int(result_g // 1000)
print(f"Massa nykymittojen mukaan: {result_kg} kilogrammaa ja {result_g % 1000:.2f} grammaa.")