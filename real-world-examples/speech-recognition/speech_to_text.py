# I ran this in MacOs and it is working for me. (python3.8.x and pip3. check if its pip or pip3 for you)
# If it's not working check below notes for troubleshooting
# 1. pip3 install SpeechRecognition
# 2. brew install portaudio
# 3. pip3 install pyaudio
# Note: As pyaudio has dependency on portaudio, install portaudio first in your machine.
# If you are getting error in MacOs. fatal error: 'portaudio.h' file not found. Run brew install portaudio
# You can read which languages it supports here: https://cloud.google.com/speech-to-text/docs/languages
# Use this if still you get portaudio.h error while installing pyaudio
# pip install --global-option='build_ext' --global-option='-I/usr/local/include' --global-option='-L/usr/local/lib' pyaudio

# import the module
import speech_recognition as sr

# create the recognizer
r = sr.Recognizer()

# List microphones
# for index, name in enumerate(sr.Microphone.list_microphone_names()):
#    print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))

# define the microphone
try:
    mic = sr.Microphone(device_index=0)
    print("Start speaking")
except Exception as e:
    exit(f"Some issue with mic {e}")

# record your speech
try:
    with mic as source:
        audio = r.listen(source)
except Exception as e:
    exit(f"Looks like mic is not instantiated {e}")

try:
    result = r.recognize_google(audio, language="hi-IN")
except sr.RequestError:
    # API was unreachable or unresponsive
    exit("API is unreachable")
except sr.UnknownValueError:
    # speech was unintelligible
    exit("Unable to recognize speech! Were you speaking")

# export the result
with open('my_speech.txt', mode ='w') as file:
    file.write(result)

print("It has stored speech into text in my_speech.txt file")
