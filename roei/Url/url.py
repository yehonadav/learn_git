import requests

while True:
    url = input("please enter a valid url:")
    filename = input("please enter an html file name:") + '.html'

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

