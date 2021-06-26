import pyttsx3 # pip install pyttsx3

engine = pyttsx3.init() # object creation

""" RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate, by default rate is 200
#engine.setProperty('rate', 125) # Setting up new voice rate

"""VOLUME"""
volume = engine.getProperty('volume')   # getting to know current volume level (min=0 and max=1)
engine.setProperty('volume',0.9)    # setting up volume level  between 0 and 1

"""VOICE"""
voices = engine.getProperty('voices')       # getting details of current voice
engine.setProperty('voice', voices[7].id)  # changing index, changes voices 7 for male EN
#engine.setProperty('voice', voices[20].id)   # changing index, changes voices. 20 for female IN Lekha

engine.say("Hello World!")
engine.say('My current speaking rate is ' + str(rate))
engine.runAndWait()
engine.stop()

"""Saving Voice to a file"""
# On linux make sure that 'espeak' and 'ffmpeg' are installed
engine.save_to_file('Hello World', 'test.mp3')
engine.runAndWait()

'''
voices = engine.getProperty('voices')
for voice in voices:
    print("Voice: %s" % voice.name)
    print(" - ID: %s" % voice.id)
    print(" - Languages: %s" % voice.languages)
    print(" - Gender: %s" % voice.gender)
    print(" - Age: %s" % voice.age)
    print("\n")

# https://pyttsx3.readthedocs.io/en/latest/
# https://pyttsx3.readthedocs.io/en/latest/engine.html#examples
'''
