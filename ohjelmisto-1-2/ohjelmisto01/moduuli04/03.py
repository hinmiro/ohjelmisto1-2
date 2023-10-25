user_input = 0
nums_array = []
while user_input != str(""):
    user_input = input("Syötä luku: ")
    if user_input.isdigit() or user_input[1:].isdigit():
        nums_array.append(int(user_input))

print(f"Suurin numero oli {max(nums_array)}")
print(f"Pienin numero oli {min(nums_array)}")

