import network
import requests
import json #dictornies
# import PyWin32
import win32com.client as wincom
speak = wincom.Dispatch("SAPI.SpVoice")

city = input("Enter city :: ")
url = f"https://api.weatherapi.com/v1/current.json?key=30652597cd6c441888463216231311&q=delhi={city}"
r = requests.get(url)
# print(r.text)
# print(type(r.text))
wdic=json.loads(r.text)
print(wdic["current"]["temp_c"])
w=(wdic["current"]["temp_c"])
print(f'The current Weather in {city} is {w}degrees')
speak.Speak(f'The current Weather in {city} is {w }degrees')
