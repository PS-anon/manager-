import speech_recognition as sr
import webbrowser
from datetime import datetime
import os
import pyaudio

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
elif "caută pe Facebook" in voicee :
    os.system("say -v Ioana 'ce vrei sa cauti ?'")
    with sr.Microphone() as source:
        fb = r.listen(source)
        os.system("say -v Ioana 'Am priceput'")
        try:
            fac = r.recognize_google(fb, language = "ro-RO")
            webbrowser.open("https://www.facebook.com/search/top/?q=" + fac)
        except:
             os.system("say -v Ioana 'Ok am o problema , incerc sa o repar , reincearca in 10 minute !'")
elif "caută pe Google" in voicee :
    os.system("say -v Ioana 'ce vrei sa cauti ?'")
    with sr.Microphone() as source:
        gog = r.listen(source)
        os.system("say -v Ioana 'Am priceput'")
        try:
            gooogle = r.recognize_google(gog, language = "ro-RO")
            webbrowser.open("https://www.google.com/" + gooogle)
        except:
             os.system("say -v Ioana 'Ok am o problema , incerc sa o repar , reincearca in 10 minute !'")
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
elif "deschide Atom" in voicee :
    os.system("say -v Ioana 'Ok deschid atom'")
    os.system("atom")
elif "deschide website" in voicee :
    os.system("say -v Ioana 'Ok, scrie denumirea website-tului'")
    inp = input("-> ")
    os.system("say -v Ioana 'Acum se deschide'")
elif "deschide Youtube" in voicee :
    os.system("say -v Ioana deschid youtube")
    webbrowser.open("https://www.youtube.com")
elif "caută pe Youtube" in voicee :
    os.system("say -v Ioana 'ce vrei sa cauti ?'")
    with sr.Microphone() as source:
        yt = r.listen(source)
        os.system("say -v Ioana 'Am priceput'")
        try:
            yut = r.recognize_google(yt, language = "ro-RO")
            webbrowser.open("https://www.youtube.com/results?search_query=" + yut)
        except:
             os.system("say -v Ioana 'Ok am o problema , incerc sa o repar , reincearca in 10 minute !'")
elif "caută pe Wikipedia" in voicee :
    os.system("say -v Ioana 'ce vrei sa cauti ?'")
    with sr.Microphone() as source:
        wik = r.listen(source)
        os.system("say -v Ioana 'Am priceput'")
        try:
            wikkk = r.recognize_google(wik, language = "ro-RO")
            webbrowser.open("https://en.wikipedia.org/wiki/" + wikkk)
        except:
             os.system("say -v Ioana 'Ok am o problema , incerc sa o repar , reincearca in 10 minute !'")

elif "pune muzică" in voicee :
    os.system("say -v Ioana 'Ce vrei sa asculti ? '")
    with sr.Microphone() as source:
        muz = r.listen(source)
        os.system("say -v Ioana 'Am priceput'")
        try:
            muzi = r.recognize_google(muz, language = "ro-RO")
            os.system(f"youtube-dl -o 'muzica.%(ext)s' 'ytsearch1:{muzi}'")
            os.system("open muzica.mp4")
        except:
             os.system("say -v Ioana 'Ok am o problema , incerc sa o repar , reincearca in 10 minute !'")
    
else :
    os.system("say -v Ioana 'Nu am inteles'")
   
