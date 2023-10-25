optimus_prime = int(input("Anna luku, kokeilen onko se alkuluku: "))

if optimus_prime <= 1:
    print(f"{optimus_prime}, ei ole alkuluku.")

elif optimus_prime > 2:
    for i in range(2, optimus_prime):
        if optimus_prime % i != 0 and optimus_prime != i:
            print(f"{optimus_prime} on alkuluku!")
            break
        else:
            print(f"{optimus_prime}, ei ole alkuluku.")
            break
else:
    print(f"{optimus_prime}, ei ole alkuluku.")
