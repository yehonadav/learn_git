import requests


url = "https://api.chucknorris.io/jokes/random"


response = requests.get(url)
joke = response.json()['value']
print(joke)
print(response.status_code)
