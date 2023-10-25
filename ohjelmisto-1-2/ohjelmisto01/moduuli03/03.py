b_gender = input("Mikä on biologinen sukupuolesi? ")
hemogl = int(input("Mikä on hemoglobiini arvosi g/l? "))



if b_gender == "mies":
    if hemogl < 134:
        print("Hemoglobiini arvosi on alhainen.")
    elif hemogl > 195:
        print("Hemoglobiini arvosi on korkea.")
    else:
        print("Hemoglobiini arvosi on normaali.")
elif b_gender == "nainen":
    if hemogl < 117:
        print("Hemoglobiini arvosi on alhainen.")
    elif hemogl > 175:
        print("Hemoglobiini arvosi on korkea.")
    else:
        print("Hemoglobiini arvosi on normaali.")
else:
    print("Virheellinen sukupuoli.")
