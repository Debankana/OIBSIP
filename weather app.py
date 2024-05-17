import requests

api_key='bb39c800896e17ed4fe706f07fbc4afd'
city=input("enter city name: ")
weather_data=requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&=imperial.APPID={api_key}")
if weather_data.json()['cod']=='404':
      print("error")
else:
      weather=weather_data.json()['weather'][0]['main']
      temp=weather_data.json()['main']['temp']
      humidity=weather_data.json()['main']['humidity']
      print(f"weather in {city} is: {weather}")
      print(f"temperature at {city} is: {temp} degrees Fahrenheit")
      print(f"humidity at {city} is: {humidity}%")
