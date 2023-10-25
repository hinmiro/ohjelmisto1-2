def array_refiner(numbers):
    refined_numbers = []
    for i in range(0, len(numbers)):
        if numbers[i] % 2 == 0:
            refined_numbers.append(numbers[i])
            i += 1
    return refined_numbers


print("Luodaan lista. --------->\n")
list_of_numbers = [1, 45, 13, 7, 10, 8, 12, 23, 45, 9, 2]
print("Kutsutaan listan muokkaaja. --------->\n")
refined_nums = array_refiner(list_of_numbers)
print(*refined_nums, sep=", ")
