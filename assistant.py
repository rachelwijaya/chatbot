import pyttsx3  # text to speech recognition package
import datetime
import speech_recognition as sr 

machine = pyttsx3.init()  # initialisation of the module, variable machine refers to the assistant


def speech(audio):
    machine.say(audio)  # adds an utterance to speak to the event queue
    machine.runAndWait()


def time():
    currentTime = datetime.datetime.now().strftime("%I:%M:%S")
    speech("the current time is" + currentTime)


def year():
    currentYear = str(datetime.datetime.now().year)
    speech("The year is" + currentYear)


def date():
    currentYear = str(datetime.datetime.now().year)
    currentMonth = datetime.datetime.now().month
    switcher = {
        1: 'January',
        2: 'February',
        3: 'March',
        4: 'April',
        5: 'May',
        6: 'June',
        7: 'July',
        8: 'August',
        9: 'September',
        10: 'October',
        11: 'November',
        12: 'December'
    }
    currentDate = str(datetime.datetime.now().day)
    speech("today's date is" + currentDate + switcher.get(currentMonth) + currentYear)

def greetme():
    speech("Welcome back!")
    time()
    date()
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour <12:
        speech("Good morning!")
    elif hour >=12 and hour <18:
        speech("Good afternoon!")
    elif hour >=18 and hour <24:
        speech("Good evening!")
    else:
        speech("Good night!")

    speech("Bambang at your service, how can I help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(query)
    
    except Exception as e:
        print(e)
        speech("Say that again please")
        return "None"
    return query

takeCommand()