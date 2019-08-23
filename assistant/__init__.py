from talk import talk
from main import thank_you_replies, hello, how_are_you, fortune_cookie, roll_a_dice, bye
from search_web import search_web
from selenium import webdriver
import random
from youtube import youtube
from calculate import calculate
from open_application import open_application
import send_mail
import speech_recognition as sr
import os


def assistant(command):
    try:
        if 'hello' in command.lower() or 'hi' in command.lower():
            talk(random.choice(hello))

        elif 'who are you' in command.lower() or 'what is your name' in command.lower() or 'what\'s your name' in command.lower() \
                or 'who\'re you' in command.lower():
            talk('My name is Sahayak')

        elif 'thank you' in command.lower() or 'thanks' in command.lower() or 'arigato' in command.lower():
            talk(random.choice(thank_you_replies))

        elif 'created you' in command.lower() or 'who made you' in command.lower() or 'who\'s your creator' in \
                command.lower() or 'who is your creator' in command.lower():
            talk('Saakshaat is my Lord and Saviour')
            talk('Check him out')
            webdriver.Chrome(executable_path=os.path.abspath('chromedriver')).get('https://saakshaat.github.io')

        elif 'what\'s up' in command.lower() or 'how are you' in command.lower() or 'what is up' in command.lower():
            talk(random.choice(how_are_you))

        elif 'play' in command.lower() or 'youtube' in command.lower():
            youtube(command)

        elif 'calculate' in command.lower() or 'do some math' in command.lower():
            calculate(command)

        elif 'send mail' in command.lower() or 'email' in command.lower():
            send_mail.send_mail(command)

        elif 'roll a dice' in command.lower() or 'roll dice' in command.lower():
            talk('Rolling')
            talk(str(random.choice(roll_a_dice)))

        elif 'open fortune cookie' in command.lower() or 'fortune cookie' in command.lower() or 'my fortune' in \
                command.lower() or 'I going ' in command.lower():
            talk('The almighty fortune cookie says')
            talk(random.choice(fortune_cookie))

        elif 'open' in command.lower() or 'start' in command.lower():
            open_application(command)

        elif 'bye' in command.lower() or 'goodbye' in command.lower() or 'so long' in command.lower() or 'see you later' \
                in command.lower() or 'i have to go' in command.lower():
            talk(random.choice(bye))
            import sys
            sys.exit()
        elif 'search' in command.lower() or 'google' in command.lower():
            search_web(command)
        else:
            search_web(command)

    except sr.UnknownValueError:
        talk('I\'m not sure if I got that. Could you repeat that, please?')
