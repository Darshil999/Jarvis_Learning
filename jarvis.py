import pyttsx3
import datetime as dt
import webbrowser as wb
import math
import requests  # For making HTTP requests

# Initialize the speech engine
engine = pyttsx3.init()



# Function to make Jarvis speak
def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()

# Function to handle greetings and user input
def greet_and_get_input():
    speak("Hello, I am Jarvis. How can I assist you?")
    user_input = input("How can I help you?\n").lower()
    return user_input

# Function to match user input with commands
def process_command(user_input):
    if "google" in user_input:
        speak("Opening Google")
        wb.open("https://www.google.com/")

    elif "cricbuzz" in user_input:
        speak("Opening Cricbuzz")
        wb.open("https://www.cricbuzz.com/")

    elif "wiki" in user_input or "wikipedia" in user_input:
        speak("Opening Wikipedia")
        wb.open("https://en.wikipedia.org/wiki/Wiki")

    elif "x" in user_input or "twitter" in user_input:
        speak("Opening X")
        wb.open("https://x.com/")

    elif "facebook" in user_input:
        speak("Opening Facebook")
        wb.open("https://www.facebook.com/")

    elif "youtube" in user_input:
        speak("Opening YouTube")
        wb.open("https://www.youtube.com/")

    elif "time" in user_input or "date" in user_input:
        current_date_time = dt.datetime.now().strftime('%I:%M %p, %A, %d %B %Y')
        speak(f"The current date and time is {current_date_time}")

    else:
        speak("I am sorry, I didn't understand that. Please try again.")

def process_math(user_input):
    # Dictionary for word-to-number mapping
    word_to_number = {
        "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
        "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
        "ten": 10
    }

    # Split user input into words
    words = user_input.split()

    # Extract numbers (both digits and words)
    numbers = []
    for word in words:
        if word.isdigit():  # Handle numeric digits
            numbers.append(int(word))
        elif word in word_to_number:  # Handle word numbers
            numbers.append(word_to_number[word])

    # Determine the operation and calculate
    if "add" in user_input:
        result = sum(numbers)
        return f"The answer is {result}"
    elif "subtract" in user_input and len(numbers) >= 2:
        result = numbers[0] - numbers[1]
        return f"The answer is {result}"
    else:
        return "I can only add or subtract for now."

# def fetch_weather(latitude, longitude):
#     try:
#         # Construct the API URL
#         url = f"https://api.weather.gov/points/{latitude},{longitude}/forecast"
        
#         # Make the request
#         response = requests.get(url)
#         response.raise_for_status()  # Raise exception for HTTP errors

#         # Parse the JSON response
#         weather_data = response.json()
#         forecast = weather_data["properties"]["periods"][0]  # Get the first forecast period
        
#         # Extract relevant details
#         weather_info = f"{forecast['name']} forecast: {forecast['shortForecast']}, " \
#                        f"temperature is {forecast['temperature']}°{forecast['temperatureUnit']}."
#         return weather_info

#     except Exception as e:
#         return f"Unable to fetch weather data. Error: {str(e)}"

# Main program
if __name__ == "__main__":
    user_command = greet_and_get_input()
    
    if "add" in user_command or "subtract" in user_command:
        result = process_math(user_command)
        speak(result)

    # elif "weather" in user_command:
    #     # Provide latitude and longitude of the desired location
    #     latitude = "39.7456"  # Replace with your latitude
    #     longitude = "-97.0892"  # Replace with your longitude
    #     weather_info = fetch_weather(latitude, longitude)
    #     speak(weather_info)

    else:
        process_command(user_command)
