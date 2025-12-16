import datetime
import random
import platform
import requests

def calculate(expression: str) -> str:
    """
    Safely evaluates a simple mathematical expression.
    
    Args:
        expression: A string containing a math expression like '2 + 2' or '5 * 10'.
        
    Returns:
        The result of the calculation as a string, or an error message.
    """
    allowed_chars = "0123456789+-*/(). "
    if not all(char in allowed_chars for char in expression):
        return "Error: Expression contains invalid characters. Only numbers and basic math operators are allowed."
    
    try:
        # potentially unsafe if not strictly sanitized, but 'allowed_chars' mitigates most risks for this demo
        result = eval(expression, {"__builtins__": None}, {})
        return str(result)
    except Exception as e:
        return f"Error evaluating expression: {e}"

def get_current_time() -> str:
    """
    Returns the current local date and time.
    """
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")

def get_system_info() -> str:
    """
    Returns information about the system the agent is running on.
    """
    system = platform.system()
    release = platform.release()
    version = platform.version()
    machine = platform.machine()
    python_version = platform.python_version()
    return f"System: {system} {release}\nVersion: {version}\nMachine: {machine}\nPython: {python_version}"

def generate_random_number(min_val: int, max_val: int) -> int:
    """
    Generates a random integer between min_val and max_val (inclusive).
    """
    return random.randint(min_val, max_val)

def get_current_weather(city: str) -> str:
    """
    Gets the current weather for a given city using Open-Meteo.
    Args:
        city: The name of the city (e.g. "London", "New York").
    """
    try:
        # 1. Geocoding to get lat/long
        geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1&language=en&format=json"
        geo_response = requests.get(geo_url).json()
        
        if not geo_response.get("results"):
            return f"Could not find coordinates for {city}."
            
        location = geo_response["results"][0]
        lat = location["latitude"]
        lon = location["longitude"]
        name = location["name"]
        country = location.get("country", "")
        
        # 2. Weather API
        weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        weather_response = requests.get(weather_url).json()
        
        if "current_weather" not in weather_response:
             return f"Could not fetch weather data for {name}."
             
        cw = weather_response["current_weather"]
        temp = cw["temperature"]
        wind_speed = cw["windspeed"]
        
        return f"Weather in {name}, {country}: {temp}°C, Wind Speed: {wind_speed} km/h."
        
    except Exception as e:
        return f"Error fetching weather: {e}"
