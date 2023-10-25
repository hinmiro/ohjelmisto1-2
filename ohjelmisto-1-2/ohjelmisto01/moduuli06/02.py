import random

dice = 0


def rand_num(dice_max):
    return random.randint(1, dice_max)


dice_value = int(input("Anna nopan maksimi silmäluku: "))

while dice < dice_value:
    dice = rand_num(dice_value)
    print(f"Heitto! {dice}")
