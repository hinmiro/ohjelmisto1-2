def array_calculator(numbers):
    return sum(numbers)


print("------ Luodaan lista ------")
list_of_numbers = [1, 12, 32, 11, 87, 65]
print("------ Kutsutaan laskuria ------")
list_sum = array_calculator(list_of_numbers)
print("--------------------------------")
print(f"Listan alkioiden summa on {list_sum}")
