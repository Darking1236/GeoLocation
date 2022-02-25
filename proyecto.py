from warnings import catch_warnings
import speech_recognition as sr
import pyttsx3


listener= sr.Recognizer()
name='alexa'
engine = pyttsx3.init()

def hablar(text):   
    engine.say(text)
    engine.runAndWait()

def listen():
    try: 
        with sr.Microphone() as source:
            print("escuchando...")
            voice= listener.listen(source)
            rec=listener.recognize_google(voice)
            record= rec.lower()
            if name in record:
                print(record)
            
    except:
        pass
    return record

def run():
    recording=listen()
    if 'ejecuta' in recording:
        hablar('Analizando')
    else:
        hablar('no te entiendo')

run()