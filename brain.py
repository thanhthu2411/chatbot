from datetime import datetime
from constant import GREETING_PROMPTS, EXIT_PROMPTS
import re

def get_words(text):
    return re.findall(r"[a-z0-9']+", text.strip().lower())


def is_goodbye(text):
    return bool(EXIT_PROMPTS & set(get_words(text)))


def reply(text):
    words = get_words(text) 

    # Handle goodbye before the other intents so every goodbye form gets
    # the goodbye response, even if it also contains another keyword.
    if is_goodbye(text):
        return "Goodbye! Come back any time."
    
    if set(GREETING_PROMPTS) & set(words):
        return "Hello! Ask me for the time or the weather."

    if "time" in words:
        now = datetime.now()
        return "It's " + now.strftime("%I:%M %p") + " on " + now.strftime("%A, %B %d.")

    if "weather" in words:
            return "Weather is coming soon."

    
    if "help" in words:
            return "I can say hello, tell you the time, and check the weather (try: weather in Rexburg)."
    

    return "Sorry, I don't understand that yet. Type 'help' to see what I can do."



if __name__ == "__main__":
    while True:
        text = input("You: ")
        print("Bot:", reply(text))
        if is_goodbye(text):
            break
