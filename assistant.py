import pyttsx3  # text to speech recognition package
import datetime
import speech_recognition as sr

machine = pyttsx3.init()  # initialisation of the module, variable machine refers to the assistant


def speech(audio):
    machine.say(audio)  # adds an utterance to speak to the event queue
    machine.runAndWait()


def time():
    currentTime = datetime.datetime.now().strftime("%I:%M:%S")
    speech("the time is" + currentTime)


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
    speech(currentDate + switcher.get(currentMonth) + currentYear)


date()
