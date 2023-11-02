import requests

request = requests.get("https://api.chucknorris.io/jokes/random").json()

print(f"{request['value']}")
