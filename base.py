import speech_recognition as sr
import sys
from argparse import ArgumentParser



filename = sys.argv[1]

#initialize the recognizer
r = sr.Recognizer()

#open file
with sr.AudioFile(filename) as source:
    #listen for the data (load audio to memory)
    audio_data = r.record(source)
    #recognize (convert from speech to text)
    text = r.recognize_google(audio_data)
    print(text)
