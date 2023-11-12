import requests

api = "ENTER YOU TOKEN!"
query = input("What citys weather you want to check: ")

request = f"https://api.openweathermap.org/data/2.5/weather?q={query}&appid={api}"

try:
    data = requests.get(request).json()
    if int(data["cod"]) == 200:
        temperature_celsius = data['main']['temp'] - 273.15
        print(f"\n*** Weather in {data['name']} ***\n"
              f"{data['weather'][0]['main']} ({data['weather'][0]['description']})\n"
              f"Temperature is {temperature_celsius:.1f} degrees celsius")
    else:
        print(f"error {data['cod']}")

except requests.exceptions.RequestException as e:
    print("Unable to execute query")
