import speech_recognition as sr
import win32com.client
def take_command():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold=1
        audio=r.listen(source)
        try:
            print("listening.....")
            query=r.recognize_google(audio,language='en-in')
            print(f"User said: {query}")
        except:
            print("finding trouble in Recognizing....")

take_command()
