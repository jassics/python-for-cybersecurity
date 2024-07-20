#!/usr/bin/python

# I ran this in MacOs and it is working for me. (python3.8.x and pip3. check if its pip or pip3 for you)
# If it's not working check below notes for troubleshooting
# 1. pip3 install SpeechRecognition
# 2. brew install portaudio
# 3. pip3 install pyaudio
# Note: As pyaudio has dependency on portaudio, install portaudio first in your machine.
# If you are getting error in MacOs. fatal error: 'portaudio.h' file not found. Run brew install portaudio

# import the module
import speech_recognition as sr
from pydub import AudioSegment

# files
src = "hin-audio.m4a"
dst = "hin-audio.wav"

# convert wav to mp3
audio = AudioSegment.from_file(src, format='m4a')
chunk = 49*1000 # 49 seconds chunk
audio = audio[:chunk]
audio.export(dst, format="wav")

# create the recognizer
r = sr.Recognizer()

file_audio = sr.AudioFile(dst)

with file_audio as source:
   audio_text = r.record(source)

try:
    print("Audio to text conversion started...")
    # You can read which languages it supports here: https://cloud.google.com/speech-to-text/docs/languages
    # change language="hi-IN" for Hindi text
    result = r.recognize_google(audio_text, language='en-EN')
    print("Final Text:")
    print(result)
except Exception as e:
    print(f"it broke, try smaller filei: {e}")

# export the result
with open('my_speech.txt', mode ='w') as file:
    file.write(result)

print("\nIt has stored speech into text in my_speech.txt file")
