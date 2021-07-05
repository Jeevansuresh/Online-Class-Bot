import pyttsx3 #download the module using python -m pip install pyttsx3
engine = pyttsx3.init()


voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id) #change the number to 0 if u want male voice or keep it just like that for female voice

def speak(audio):
    print(audio)
    engine.say(audio)
    engine.runAndWait()

speak("surprise it works !!!! ")
#this will speak out whatever you input in
