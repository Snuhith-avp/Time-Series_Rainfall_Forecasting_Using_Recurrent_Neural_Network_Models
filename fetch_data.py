import requests
from dotenv import load_dotenv
import os

def fetch_data(date):
    """
    Fetches weather data for a specific date from the OpenWeatherMap API.

    Args:
        date (str): The date in the format 'YYYY-MM-DD' for which weather data is requested.

    Returns:
        tuple: A tuple containing arrays of temperature, humidity, sea level, visibility, wind speed, and events.
               Each array contains the corresponding data for the specified date.
    """

    load_dotenv()
    secret_key = os.environ.get('API_KEY')
    api_key = secret_key
    city = 'Austin'
    country_code = 'US'
    date = date # Specify the date you are interested in

    endpoint = 'http://api.openweathermap.org/data/2.5/forecast'
    params = {
        'q': f'{city},{country_code}',
        'appid': api_key,
    }

    response = requests.get(endpoint, params=params)
    data = response.json()

    # Filter data for the specific date
    target_date_data = [item for item in data['list'] if item['dt_txt'].split()[0] == date]

    temp_array=[]
    humidity_array=[]
    sea_level_array=[]
    visibility_array=[]
    wind_speed_array=[]
    Events_array=[]

    for entry in target_date_data:
        temp_array.append(entry['main']['temp'])
        humidity_array.append(entry['main']['humidity'])
        sea_level_array.append(entry['main']['sea_level'])
        visibility_array.append(entry['visibility'])
        wind_speed_array.append(entry['wind']['speed'])
        Events_array.append(entry['weather'][0]['description'])

    return temp_array, humidity_array, sea_level_array, visibility_array, wind_speed_array, Events_array
