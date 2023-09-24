import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 185)
engine.setProperty('volume', 0.9)

def say_and_save(text, filename):
    engine.save_to_file(text, filename)
    engine.runAndWait()
