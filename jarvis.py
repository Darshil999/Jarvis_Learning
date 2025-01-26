import pyttsx3
import datetime as dt
import webbrowser as wb


engine = pyttsx3.init()

print("Hello, I am Jarvis, How can I assist you?")
engine.say("Hello, I am Jarvis, How can I assist you?")
engine.runAndWait()


print("How can I help you?")
engine.say("How can I help you?")
engine.runAndWait()
user_inp= input()


print(f"Ok so you want me to do is {user_inp}")
engine.say(f"Ok so you want me to do is {user_inp}")
engine.runAndWait()


commands = ['open google','open cricbuzz','open youtube',"what's the time"]

if(commands[0] == user_inp.lower()):
    engine.say("Opening Google")
    engine.runAndWait()
    wb.open("https://www.google.com/")

elif(commands[1] == user_inp.lower()):
    engine.say("Opening Cricbuzz")
    engine.runAndWait()
    wb.open("https://www.cricbuzz.com/")

elif(commands[2] == user_inp.lower()):
    engine.say("Opening youtube")
    engine.runAndWait()
    wb.open("https://www.youtube.com/")

elif(commands[3] == user_inp.lower()) :
    current_date_time = dt.datetime.now()
    print(current_date_time)
    engine.say(f"The current date and time is {current_date_time}")
    engine.runAndWait()