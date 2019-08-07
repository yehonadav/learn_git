import requests as r

html_data = input(str("enter url:"))
url = r.get(html_data)

print(url.text)