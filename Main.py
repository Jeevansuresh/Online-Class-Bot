import pyttsx3 
import time 
import os 
from datetime import datetime
import webbrowser
current_time = datetime.now() 
t = current_time.hour
d = datetime.today().isoweekday()

engine = pyttsx3.init()
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)

def speak(audio):
    print(audio)
    engine.say(audio)
    engine.runAndWait()







def Welcome():
    currentH = int(datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning Sir ')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon Sir')

    if currentH >= 18 and currentH !=0:
        speak('Good Evening Sir ')

print(d,t)
Welcome()

if (d==1 and t==9) :
    speak("Its 9'o clock")
    webbrowser.open("https://zoom.us/j/94051714670?pwd=STU5U2lrdFBWVGJhZG1iN0FOQTB2dz09")
elif (d==1 and t==10): 
    speak("Its 10'o Clock")
    webbrowser.open("Your Class Link Here")
elif (d==1 and t==11):
    speak("Its 11'o Clock")
    webbrowser.open("Your Class Link Here")
elif (d==1 and t==12):
    speak("Its 12'o clock")
    webbrowser.open("https://zoom.us/j/97479787188?pwd=RnN0RkJhVW5qVmlrWTdJdmRpUVFaZz09")
elif (d==1 and t==13):
    speak("its 1'o clock ")
    webbrowser.open("Your Class Link Here")
    
elif (d==3 and t==9) : 
    speak("Its 9'o clock")
    webbrowser.open("https://zoom.us/j/94051714670?pwd=STU5U2lrdFBWVGJhZG1iN0FOQTB2dz09")
elif (d==3 and t==10): 
    speak("Its 10'o Clock")
    webbrowser.open("Your Class Link Here")
elif (d==3 and t==11):
    speak("Its 11'o Clock")
    webbrowser.open("Your Class Link Here")
elif (d==3 and t==12):
    speak("Its 12'o clock")
    webbrowser.open("https://zoom.us/j/97479787188?pwd=RnN0RkJhVW5qVmlrWTdJdmRpUVFaZz09")
elif (d==3 and t==13):
    speak("its 1'o clock ")
    webbrowser.open("Your Class Link Here")

elif (d==5 and t==9) : 
    speak("Its 9'o clock")
    webbrowser.open("https://zoom.us/j/94051714670?pwd=STU5U2lrdFBWVGJhZG1iN0FOQTB2dz09")
elif (d==5 and t==10): 
    speak("Its 10'o Clock")
    webbrowser.open("Your Class Link Here")
elif (d==5 and t==11):
    speak("Its 11'o Clock")
    webbrowser.open("Your Class Link Here")
elif (d==5 and t==12):
    speak("Its 12'o clock")
    webbrowser.open("https://zoom.us/j/97479787188?pwd=RnN0RkJhVW5qVmlrWTdJdmRpUVFaZz09")
elif (d==5 and t==13):
    speak("its 1'o clock ")
    webbrowser.open("Your Class Link Here")
    
elif(d==2and t==9) :
    speak("Its 9'o clock")
    webbrowser.open("Your Class Link Here")
elif(d==2 and t==10): 
    speak("Its 10'o Clock")
    webbrowser.open("Your Class Link Here")
elif (d==2 and t==11):
    speak("Its 11'o Clock")
    webbrowser.open("Your Class Link Here")
elif (d==2 and t==12):
    speak("Its 12'o clock")
    webbrowser.open("https://zoom.us/j/97479787188?pwd=RnN0RkJhVW5qVmlrWTdJdmRpUVFaZz09")
elif (d==2  and t==13):
    speak("its 1'o clock ")
    webbrowser.open("Your Class Link Here")

elif(d==4and t==9) :
    speak("Its 9'o clock")
    webbrowser.open("Your Class Link Here")
elif(d==4 and t==10): 
    speak("Its 10'o Clock")
    webbrowser.open("Your Class Link Here")
elif (d==4 and t==11):
    speak("Its 11'o Clock")
    webbrowser.open("Your Class Link Here")
elif (d==4 and t==12):
    speak("Its 12'o clock")
    webbrowser.open("https://zoom.us/j/97479787188?pwd=RnN0RkJhVW5qVmlrWTdJdmRpUVFaZz09")
elif (d==4  and t==13):
    speak("its 1'o clock ")
    webbrowser.open("Your Class Link Here")

elif(d==6and t==9) :
    speak("Its 9'o clock")
    webbrowser.open("Your Class Link Here")
elif(d==6 and t==10): 
    speak("Its 10'o Clock")
    webbrowser.open("Your Class Link Here")
elif (d==6 and t==11):
    speak("Its 11'o Clock")
    webbrowser.open("Your Class Link Here")
elif (d==6 and t==12):
    speak("Its 12'o clock")
    webbrowser.open("https://zoom.us/j/97479787188?pwd=RnN0RkJhVW5qVmlrWTdJdmRpUVFaZz09")
elif (d==6  and t==13):
    speak("its 1'o clock ")
    webbrowser.open("Your Class Link Here")
    
else:
    speak("You Dont Have Any Class Now")


