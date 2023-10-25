city_names = []


for i in range(0, 5):
    city = input(f"Anna {i+1}. kaupungin nimi: ")
    i += 1
    city_names.append(city)

print("\nKaupungit ovat:\n")
for i in range(0, len(city_names)):
    print(city_names[i])
