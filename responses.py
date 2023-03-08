import requests

def get_response(message:str) -> str:
    p_message = message.lower()

    # Expects message to be in the following format: "weather city"
    if p_message.startswith("weather "):

        baseurl = 'http://api.openweathermap.org/data/2.5/weather?'
        city = p_message[8:]  # Uses the rest of the string after "weather " as city name
        city = city.capitalize()

        # Insert OpenWeatherMap API key here!!!
        key = ''

        # Function to convert kelvin value from API into Celsius and Fahrenheit
        def convert_kelvin(kelvin):
            celsius = kelvin - 273.15
            fahrenheit = celsius * (9/5) + 32
            return celsius, fahrenheit

        # Sending a request to API and getting response
        url = baseurl + "appid=" + key + "&q=" + city
        response = requests.get(url).json()

        # Formats output if the city is valid, prints error otherwise
        if response["cod"] != "404":
            kelvin = response['main']['temp']
            celsius, fahrenheit = convert_kelvin(kelvin)
            humidity = response['main']['humidity']
            desc = response['weather'][0]['description']
            windspeed = response['wind']['speed']
            weather = f"Weather in {city}:\n"
            weather += f"Temperature: {celsius:.2f}°C or {fahrenheit:.2f}°F\n"
            weather += f"Humidity: {humidity}%\n"
            weather += f"Description: {desc}\n"
            weather += f"Wind Speed: {windspeed} m/s"
        else:
            weather = f"The City \"{city}\" Was Not Found!"

        return weather

