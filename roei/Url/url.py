import requests

while True:
    url = input("please inter a valid url:")
    filename = input("please enter an html name") + '.html'

    try:
        response = requests.get(url)
        response.raise_for_status()
    except:
        print("bad request")
        continue

    try:
        with open(filename, 'wb') as file:
            file.write(response.content)
    except Exception as e:
        print(e)
        continue
    break

