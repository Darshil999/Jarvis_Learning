import pyttsx3
import datetime as dt
import webbrowser as wb

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

    elif "youtube" in user_input:
        speak("Opening YouTube")
        wb.open("https://www.youtube.com/")

    elif "time" in user_input or "date" in user_input:
        current_date_time = dt.datetime.now().strftime('%I:%M %p, %A, %d %B %Y')
        speak(f"The current date and time is {current_date_time}")

    else:
        speak("I am sorry, I didn't understand that. Please try again.")

# Main program
if __name__ == "__main__":
    user_command = greet_and_get_input()
    process_command(user_command)