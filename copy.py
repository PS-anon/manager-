import speech_recognition as sr
import webbrowser
from datetime import datetime
import os

r = sr.Recognizer()
intrebari = 'ce faci'
raspunsuri_ok = 'sunt ok'
raspunsuri_grs = 'rau'
with sr.Microphone() as source:
    os.system("say -v Ioana 'Salut, cu ce te pot ajuta ?'")
    audioinput = r.listen(source)
    os.system("say -v Ioana 'Ok, am priceput !'")
    try:
        print("Text: "+r.recognize_google(audioinput, language = "ro-RO"))
        voicee = r.recognize_google(audioinput, language = "ro-RO")
    except:
         os.system("say -v Ioana 'Ok am o problema , incerc sa o repar , reincearca in 10 minute !'")

if "deschide Facebook" in voicee :
    os.system("say -v Ioana 'Deschid Facebook'")
    webbrowser.open('https://www.facebook.com')
elif "deschide Google" in voicee :
    os.system("say -v Ioana 'Deschid google'")
    webbrowser.open('https://google.com')
elif "Vreau să ascult piesa favorită" in voicee :
    os.system("say -v Ioana 'Niste Ombladon e  pe drum hehe'")
    webbrowser.open('https://www.youtube.com/watch?v=ektftzuw91A')
elif "Cât e ceasul" in voicee :
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Timp :", current_time)
elif intrebari in voicee :
    os.system("say -v Ioana 'Eh , ok presupun , tu ?'")
elif raspunsuri_ok in voicee :
    os.system("say -v Ioana 'Blana'")
elif raspunsuri_grs in voicee:
    os.system("say -v Ioana 'Hmm nu e ok '")
else :
    os.system("say -v Ioana 'Nu am inteles'")
    
