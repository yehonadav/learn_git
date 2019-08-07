# import requests as  req
#
#
# resp = req.get("http://www.walla.co.il")
#
# respone = print(resp.text)

import socket

url = input("Please put the url you want to find the IP for:")
getit = socket.gethostbyname(str(url))

print(getit)
