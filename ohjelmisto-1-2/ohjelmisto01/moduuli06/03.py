def gallon_in_litre(gallons):
    return gallons * 3.785


user_gallons = 1

while True:
    user_gallons = int(input(f"Kuinka monta gallonaa käännetään litroiksi: "))
    if user_gallons > 0:
        litres = (gallon_in_litre(user_gallons))
        print(f"{user_gallons} gallonaa on {litres} litraa.")
    else:
        print("Lopetit ohjelman.")
