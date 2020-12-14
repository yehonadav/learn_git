import requests

response = requests.get("https://api.chucknorris.io/jokes/random")
joke = response.json()['value']
print(joke)
