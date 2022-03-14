import os
import time
import playsound
#import speech_recognition as sr
#from gtts import gTTS
import gtts
from playsound import playsound
tts = gtts.gTTS("hello how are you",lang="en")
tts.save("hello.mp3")
playsound("hello.mp3")
def speak(text):
    tts = gTTS(var=text, lang="en")
    filename = "voice.mp3"
    tts.save(filename)
    playsound(filename)

speak()