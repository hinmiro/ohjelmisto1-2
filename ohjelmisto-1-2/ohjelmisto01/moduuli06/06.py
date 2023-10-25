import math


def pizza_calc(diameter, price):
    price_per_sqr_m = ((math.pi * (diameter / 2) ** 2) * price) / 10
    return price_per_sqr_m


pizza1 = []
pizza2 = []

pizza1_diameter = (int(input("\nAnna ensimmäisen pizzan halkaisija senttimetreinä: ")))
pizza1_price = (float(input("\nAnna ensimmäisen pizzan hinta euroina: ")))
pizza2_diameter = (int(input("\nAnna toisen pizzan halkaisija senttimetreinä: ")))
pizza2_price = (float(input("\nAnna toisen pizzan hinta euroina: ")))

calculated_price1 = pizza_calc(pizza1_diameter, pizza1_price)
calculated_price2 = pizza_calc(pizza2_diameter, pizza2_price)

if calculated_price1 < calculated_price2:
    print(f"Ensimmäinen pizza on halvempi vaihtoeto. {calculated_price1:.2f}€/m2")
elif calculated_price1 > calculated_price2:
    print(f"Toinen pizza on halvempi vaihtoehto. {calculated_price2:.2f}€/m2")
else:
    print(f"Molemmat ovat samanhintaisia. {calculated_price1:.2f}€/m2 & {calculated_price2:.2f}€/m2")
