import random
dice = 0
def rand_num():
    return random.randint(1, 6)

while dice < 6:
    dice = random.randint(1, 6)
    print(f"Heitto! {dice}")

