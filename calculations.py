import fetch_data
from collections import Counter
from datetime import datetime
import pandas as pd

def calculate_temp(temp):
    """
    Calculate the minimum, maximum, and average temperature from a given list of temperatures.

    Args:
        temp (list): A list of temperatures.

    Returns:
        tuple: A tuple containing the minimum temperature, maximum temperature, and average temperature.
    """
    min_temp = min(temp)
    max_temp = max(temp)
    avg_temp = sum(temp) / len(temp)
    return min_temp, max_temp, avg_temp

def calculate_dew_point(temp, humd):
    """
    Calculate the dew point for a given temperature and humidity.

    Parameters:
    temp (list): A list of temperatures.
    humd (list): A list of humidities.

    Returns:
    tuple: A tuple containing the minimum dew point, maximum dew point, and average dew point.
    """
    dew_array=[]
    for i in range(len(temp)):
        dew_point = temp[i] - (100 - humd[i]) / 5
        dew_array.append(dew_point)

    min_dew = min(dew_array)
    max_dew = max(dew_array)
    avg_dew = sum(dew_array) / len(dew_array)
    return min_dew, max_dew, avg_dew

def calculate_sea_level(sea_level):
    """
    Calculate the minimum, maximum, and average sea level from a given list of sea levels.

    Args:
        sea_level (list): A list of sea level values.

    Returns:
        tuple: A tuple containing the minimum sea level, maximum sea level, and average sea level.

    """
    min_sea = min(sea_level)
    max_sea = max(sea_level)
    avg_sea = sum(sea_level) / len(sea_level)
    return min_sea, max_sea, avg_sea

def calculate_visibility(visibility):
    """
    Calculate the minimum, maximum, and average visibility from a list of visibility values.

    Args:
        visibility (list): A list of visibility values.

    Returns:
        tuple: A tuple containing the minimum visibility, maximum visibility, and average visibility.
    """
    min_vis = min(visibility)
    max_vis = max(visibility)
    avg_vis = sum(visibility) / len(visibility)
    return min_vis, max_vis, avg_vis

def calculate_wind_speed(wind_speed):
    """
    Calculate the minimum, maximum, and average wind speed.

    Args:
        wind_speed (list): A list of wind speeds.

    Returns:
        tuple: A tuple containing the minimum, maximum, and average wind speed.
    """
    min_wind = min(wind_speed)
    max_wind = max(wind_speed)
    avg_wind = sum(wind_speed) / len(wind_speed)
    return min_wind, max_wind, avg_wind
    
def find_Event(Events):
    """
    Find the most common event in the given list of events.

    Args:
        Events (list): A list of events.

    Returns:
        str: The most common event.

    """
    if not Events:
        return None

    counter = Counter(Events)
    most_common = counter.most_common(1)[0][0]
    return most_common

def calculate_humidity(humidity):
    """
    Calculate the minimum, maximum, and average humidity from a list of humidity values.

    Args:
        humidity (list): A list of humidity values.

    Returns:
        tuple: A tuple containing the minimum humidity, maximum humidity, and average humidity.
    """
    min_hum = min(humidity)
    max_hum = max(humidity)
    avg_hum = sum(humidity) / len(humidity)
    return min_hum, max_hum, avg_hum

def getData(date):
    """
    Fetches weather data for a given date and calculates various statistics.

    Args:
        date (str): The date in the format 'YYYY-MM-DD'.

    Returns:
        pandas.DataFrame: A DataFrame containing the calculated statistics for the given date.
    """
    temp, humidity, sea_level, visibility, wind_speed, Events = fetch_data.fetch_data(date)
    min_temp, max_temp, avg_temp = calculate_temp(temp)
    min_dew, max_dew, avg_dew = calculate_dew_point(temp, humidity)
    min_sea, max_sea, avg_sea = calculate_sea_level(sea_level)
    min_vis, max_vis, avg_vis = calculate_visibility(visibility)
    min_wind, max_wind, avg_wind = calculate_wind_speed(wind_speed)
    most_common_event = find_Event(Events)
    min_hum, max_hum, avg_hum = calculate_humidity(humidity)

    date_obj = datetime.strptime(date, "%Y-%m-%d")
    # Extract date, month, and year
    day = date_obj.day
    month = date_obj.month
    year = date_obj.year

    input = {
        'TempHighF': max_temp,
        'TempAvgF': min_temp,
        'TempLowF': avg_temp,
        'DewPointHighF': max_dew,
        'DewPointAvgF': avg_dew,
        'DewPointLowF': min_dew,
        'HumidityHighPercent': max_hum,
        'HumidityAvgPercent': avg_hum,
        'HumidityLowPercent': min_hum,
        'SeaLevelPressureHighInches': max_sea,
        'SeaLevelPressureAvgInches': avg_sea,
        'SeaLevelPressureLowInches': min_sea,
        'VisibilityHighMiles': max_vis,
        'VisibilityAvgMiles': avg_vis,
        'VisibilityLowMiles': min_vis,
        'WindHighMPH': max_wind,
        'WindAvgMPH': avg_wind,
        'WindGustMPH': min_wind,
        'Events': most_common_event,
        'Day': day,
        'Year': year,
        'Month': month
    }
    df = pd.DataFrame([input])
    return df

    