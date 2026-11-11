from datetime import datetime
from constant import GREETING_PROMPTS, EXIT_PROMPTS
import re
import json
import urllib.parse
import urllib.request

def get_words(text):
    return re.findall(r"[a-z0-9']+", text.strip().lower())


def is_goodbye(text):
    return bool(EXIT_PROMPTS & set(get_words(text)))


def reply(text):
    words = get_words(text) 


    if is_goodbye(text):
        return "Goodbye! Come back any time."
    
    if set(GREETING_PROMPTS) & set(words):
        return "Hello! Ask me for the time or the weather."

    if "time" in words:
        now = datetime.now()
        return "It's " + now.strftime("%I:%M %p") + " on " + now.strftime("%A, %B %d.")

    if "weather" in words:
        city = extract_city(text)
        if not city:
            return "Which city? Try: weather in Rexburg"
        return get_weather(city)

    
    if "help" in words:
            return "I can say hello, tell you the time, and check the weather (try: weather in Rexburg)."
    

    return "Sorry, I don't understand that yet. Type 'help' to see what I can do."

def fetch_json(url):
    # open an https connection to the weather server
    with urllib.request.urlopen(url, timeout=5) as response:
        return json.loads(response.read().decode())

def describe_weather(code):
    if code == 0:
        return "clear skies"
    if code in (1, 2):
        return "partly cloudy"
    if code == 3:
        return "overcast"
    if code in (45, 48):
        return "foggy"
    if 51 <= code <= 57:
        return "drizzling"
    if 61 <= code <= 67 or 80 <= code <= 82:
        return "rainy"
    if 71 <= code <= 77 or code in (85, 86):
        return "snowy"
    if code >= 95:
        return "stormy"
    return "unsettled"

def extract_city(text):
    match = re.search(r"weather\s+(?:in|for|at)\s+([a-zA-Z .'-]+)", text, re.IGNORECASE)
    if not match:
        return None
    city = match.group(1).strip()
    city = re.sub(r"\s+(today|now|tonight|please)$", "", city, flags=re.IGNORECASE)
    return city or None

def get_weather(city):
    try:
        geo_url = "https://geocoding-api.open-meteo.com/v1/search?" + urllib.parse.urlencode(
            {"name": city, "count": 1}
        )
        geo = fetch_json(geo_url)

        if not geo.get("results"):
            return "I couldn't find a place called " + city + "."
        place = geo["results"][0]

        # Step 2: coordinates -> current weather
        weather_url = "https://api.open-meteo.com/v1/forecast?" + urllib.parse.urlencode(
            {
                "latitude": place["latitude"],
                "longitude": place["longitude"],
                "current": "temperature_2m,weather_code",
                "temperature_unit": "fahrenheit",
            }
        )
        current = fetch_json(weather_url)["current"]

        temp = round(current["temperature_2m"])
        sky = describe_weather(current["weather_code"])
        where = place["name"]
        if place.get("country"):
            where += ", " + place["country"]
        return "It's " + str(temp) + "°F and " + sky + " in " + where + "."

    except (OSError, ValueError, KeyError):
        return "Sorry, I couldn't reach the weather service right now."



if __name__ == "__main__":
    while True:
        text = input("You: ")
        print("Bot:", reply(text))
        if is_goodbye(text):
            break
