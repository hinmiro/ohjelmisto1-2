numbers = []
number = 0

while number != "":
    number = input("Anna luku (rivinvaihdolla lopettaa): ")
    if number.isdigit():
        numbers.append(int(number))

numbers.sort(reverse=True)
print(*numbers[0:5], sep=", ")
