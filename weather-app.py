import requests
import json
import pyttsx3

def say(speech):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 160)
    pyttsx3.speak(speech)

print("Weather Check")
print("Created by Stark")
say("welcome to the weather checking app created by Stark")
print("welcome to the weather checking app")

country_ = input("Enter country(optional): ")
city = input("Enter city: ")

while city == "" or city == " ":
    print('Please enter a city (Type "q" to quit)')
    city = input("Enter city: ")
    if city == "q":
        break

print("")


url = f"https://api.weatherapi.com/v1/current.json?key=e845b84953e5460abe290910240506&q={city}/{country_}&aqi=yes"
r = requests.get(url)
wdic = json.loads(r.text)

temp = wdic["current"]["temp_c"]
last_updt_at = wdic["current"]["last_updated"]
feellike = wdic["current"]["feelslike_c"]
country = wdic["location"]["country"]
tz_id = wdic["location"]["tz_id"]
last_updted = wdic["current"]["last_updated"]
condition = wdic["current"]["condition"]["text"]
uv = wdic["current"]["uv"]
region = wdic["location"]["region"]
wind = wdic["current"]["wind_kph"]
windr = wdic["current"]["wind_dir"]
heatidx = wdic["current"]["heatindex_c"]


def winddir():
    if windr == "W":
        print("West")
    elif windr == "E":
        print("East")
    elif windr == "S":
        print("South")
    else:
        print("North")
    return windr

say(f"the current temprature in {city} {region} is {temp} degree celsius, feels like {feellike}")
print(f"The current temprature in {city} is {temp} degree celsius, feels like {feellike}")

say(f"Condition: {condition}")
print(f"Condition: {condition}")

say(f"Wind: {wind}km/h")
print(f"Wind: {wind}km/h")

if windr == "W":
    print("Direction: West")
elif windr == "E":
    print("Direction: East")
elif windr == "S":
    print("Direction: South")
else:
    print("Direction: North")


say(f"Heat index: {heatidx}")
print(f"Heat index: {heatidx}")

print(f"Country: {region}\nState: {country} \nTime zone: {tz_id}")


say(f"Last updated at:{last_updted}")
print(f"Last updated at:{last_updted}")

print("Created by Stark")
