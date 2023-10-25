import random
user_input = 0
random_num = (random.randint(1, 10))
while user_input != random_num:
    user_input = int(input("Arvaa numero 1 - 10 välillä: "))
    if user_input != random_num:
        if user_input < random_num:
            print("Liian pieni arvaus!")
        elif user_input > random_num:
            print("Liian suuri arvaus!")
    elif user_input == random_num:
        print("Oikein!")
