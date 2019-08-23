import os
import smtplib
from selenium import webdriver
from gtts import gTTS
import speech_recognition as sr
from playsound import playsound
import wolframalpha
import subprocess
import time
import random

bye = ['See you later, alligator', 'Goodbye', 'Yeah, I have to go too', 'Until Next Time']
hello = ['Hello there!', 'Howdy!', 'Welcome', 'Good to see you', 'Hi', 'Hello']
how_are_you = ['I\'ll live', 'Do you really care?', 'Like you, but better.', 'Somewhere between better and best',
               'If I were any better, I\'d be you.', 'I can\'t complain! It\'s against the Company Policy.',
               'Better now that I\'m talking to you.']
roll_a_dice = [1, 2, 3, 4, 5, 6]
fortune_cookie = ['The fortune you seek is in another cookie.',
                  'A closed mouth gathers no feet.', 'If you look back, you\'ll soon be going that way.',
                  'You will live long enough to open many fortune cookies', 'He who laughs last is laughing at you.',
                  'We don\'t know the future, but here\'s a cookie.', 'The road to riches is paved with homework.',
                  'Fortune not found? Abort, Retry, Ignore',
                  'Help! I am being held prisoner in a fortune cookie factory.',
                  'All fortunes are wrong except this one.', 'All fortunes are wrong except this one.',
                  'You love Chinese food.', 'You are not illiterate.', 'Don\'t let statistics do a number on you.',
                  'Change is inevitable, except for vending machines.', 'If a turtle doesn\'t have a shell, is it'
                                                                        ' naked or homeless?',
                  'Ask your mom instead of a cookie.', 'This cookie contains 117 calories in kilobytes.']
thank_you_replies = ['It is my pleasure.', 'You\'re welcome *blushes*', 'No problemo', 'I\'m here for you', 'Sure!']


def talk(audio):
    tts = gTTS(audio, lang='en-us', slow=False)
    print('>', audio)
    file = str(time.time()) + "audio.mp3"
    tts.save('Audios/' + file)
    playsound('Audios/' + file, True)
    os.remove('Audios/' + file)


def assistant(command):
    try:
        if 'hello' in command.lower() or 'hi' in command.lower():
            talk(random.choice(hello))

        elif 'who are you' in command.lower() or 'what is your name' in command.lower() or 'what\'s your name' in command.lower() \
                or 'who\'re you' in command.lower():
            talk('My name is Sahayak')

        elif 'thank you' in command.lower() or 'thanks' in command.lower() or 'arigato' in command.lower():
            talk(random.choice(thank_you_replies))

        elif 'created you' in command.lower() or 'who made you' in command.lower():
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
            send_mail()

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
            quit()
        elif 'search' in command.lower() or 'google' in command.lower():
            search_web(command)
        else:
            search_web(command)

    except sr.UnknownValueError:
        talk('I\'m not sure if I got that. Could you repeat that, please?')
        return


def get_command():
    r = sr.Recognizer()
    command = 'who are you'

    with sr.Microphone() as source:
        print('>Say Something?')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio)
        print(">", command)

    except sr.UnknownValueError:
        talk('I\'m sorry. I could\'nt catch that. Come again?')
        assistant(get_command())
    finally:
        return command


def search_web(inp):
    driver = webdriver.Chrome(executable_path=os.path.abspath('chromedriver'))
    driver.implicitly_wait(1)
    driver.maximize_window()

    if 'youtube' in inp.lower():
        talk('Opening Youtube')
        indx = inp.lower().split().index('youtube')
        query = inp.split()[indx + 1:]
        driver.get("http://youtube.com/results?search_query=" + '+'.join(query))
        return

    if 'wikipedia' in inp.lower():
        talk('Opening Wikipedia')
        indx = inp.lower().split().index('wikipedia')
        query = inp.split()[indx + 1:]
        driver.get("https://en.wikipedia.org/wiki/" + '_'.join(query))
        return
    if 'google' in inp.lower():
        indx = inp.lower().split().index('google')
        query = inp.split()[indx + 1:]
        driver.get("https://www.google.com/search?q=" + '+'.join(query))
    if 'search' in inp.lower():
        indx = inp.lower().split().index('search')
        query = inp.split()[indx + 1:]
        driver.get("https://www.google.com/search?q=" + '+'.join(query))
    else:
        driver.get("https://www.google.com/search?q=" + '+'.join(inp))
        print("https://www.google.com/search?q=" + '+'.join(inp))


def youtube(inp):
    driver = webdriver.Chrome(executable_path=os.path.abspath('chromedriver'))
    talk('Opening Youtube')
    indx = inp.lower().split().index('youtube')
    query = inp.split()[indx + 1:]
    driver.get("http://youtube.com/results?search_query=" + '+'.join(query))
    return


def calculate(inp):
    app_id = 'W4PGT4-6EL82797RH'
    client = wolframalpha.Client(app_id)
    indx = inp.lower().split().index('calculate')
    query = inp.split()[indx + 1:]
    res = client.query(' '.join(query))
    answer = next(res.results).text
    talk("The answer is " + answer)


def send_mail():
    username = input("What is your Google Email address?")
    password = input("What is your password?")
    name = input('What is your name?')
    try:
        server = smtplib.SMTP(host='smtp.gmail.com', port=587)
        server.starttls()
        server.login(username, password)
        recep = []
        not_done = True
        while not_done:
            recep.append(input("Enter Recipient's Email Address: \t"))
            sat = input("Done?")
            if sat == 'y':
                not_done = False
        sure = 'yes'
        while sure == 'yes':
            talk('What is the subject?')
            subject = get_command()
            talk('What should I tell them?')
            message = get_command()
            content = """Subject: {}\n\n{}\n\nRegards,\n{}""".format(subject.capitalize(),
                                                                     message.capitalize(),
                                                                     name.capitalize())  # The subject goes as the email subject if there are 2 blank
            # lines between it and the email content
            print(content)
            talk('Should I send this?')
            sure = get_command()
            if 'yes' in sure.lower() or 'yeah' in sure.lower() or 'yep' in sure.lower():
                server.sendmail(username, recep, content)
                talk('Sent Mail')
                break
            else:
                # repeat send_mail() from asking for the subject
                talk('What would you like to send instead?')
                continue
        server.quit()
    except ConnectionError:
        talk('Could\'nt connect to server because of {}'.format(ConnectionError))


def open_application(inp):
    d = '/Applications'
    apps = list(map(lambda x: x.split('.app')[0], os.listdir(d)))
    indx = inp.lower().split().index('open')
    app = inp.lower()[indx + 4:]
    os.system('open ' + d + '/%s.app' % app.replace(' ', '\\ '))
    return


def intro():
    talk('I can do the following and much more')
    print("""
        * Just talk to you >_<
        * Search stuff on the web :D
        * Look for stuff on Youtube
        * Send Emails .-.
        * Open Applications on your system :)
        * Roll a dice *probability noises*
        * Open a Fortune Cookie :p
        * Be a good friend
    """)


def init():
    talk(random.choice(hello))
    intro()
    while True:
        assistant(get_command())


if __name__ == "__main__":
    try:
        init()
    except KeyboardInterrupt:
        talk('Oh, alright then. {}'.format(random.choice(bye)))
        quit()
