import random

dice_list = []
dices = int(input("Montaako noppaa haluat käyttää: "))

for i in range(dices):
    dice_list.append(random.randint(1, 6))
print(f"Silmälukujen summa on {sum(dice_list)}")
