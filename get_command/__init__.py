import speech_recognition as sr
from talk import talk
from assistant import assistant


def get_command():
    r = sr.Recognizer()
    command = ''

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
        command = input('Type it out?')
        assistant(get_command())
    finally:
        return command
