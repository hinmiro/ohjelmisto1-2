cabin = input("Mikä on hyttiluokkanne? ")
if cabin.upper() == "LUX":
    print("LUX on parvekkeelinen hytti yläkannella.")
elif cabin.upper() == "A":
    print("A on ikkunallinen hytti autokannen alapuolella.")
elif cabin.upper() == "B":
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif cabin.upper() == "C":
    print("C on ikkunaton hytti autokannen alapuolella.")
else:
    print("Virheellinen syöte!")
