import pyttsx3 #pip install pyttsx3
import fitz # pip install pymupdf

doc = fitz.open('startup-secrets.pdf')     # or fitz.Document(filename)
page = doc.loadPage(24)  # loads page number 'pno' of the document (0-based)
text = page.getText()

# reading the text
speak = pyttsx3.init() # object creation
speak.setProperty('rate', 165) # setting rate to moderate pace
voices = speak.getProperty('voices')
speak.setProperty('voice', voices[7].id) # for male EN voice
speak.say(text)

# Save the text in mp3 format
try:
    speak.save_to_file(text, 'page25.mp3')
    speak.runAndWait()
    speak.stop()
except KeyboardInterrupt:
    print("Good Bye. Happy Listening!")
