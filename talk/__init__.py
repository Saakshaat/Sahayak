from gtts import gTTS
import time
from playsound import playsound
import os


def talk(audio):
    tts = gTTS(audio, lang='en-ca', slow=False)
    print('>', audio)
    file = str(time.time()) + "audio.mp3"
    tts.save('Audios/' + file)
    playsound('Audios/' + file, True)
    os.remove('Audios/' + file)
