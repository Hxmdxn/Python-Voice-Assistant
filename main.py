import pyttsx3 as p  # text to speech
import speech_recognition as sr
import webbrowser
import subprocess
import datetime
import os


def speaktx():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # adjust for ambient noise
        audio = recognizer.listen(source, timeout=8, phrase_time_limit=5)

        try:
            print("Recognizing...")
            data = recognizer.recognize_google(audio)
            print(data)
            return data.lower()

        except sr.UnknownValueError:
            print("Could not recognize audio")


def speechtx(x):
    engine = p.init()
    voices = engine.getProperty("voices")
    engine.setProperty('voice', voices[1].id)  # female voice
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 160)  # speed
    engine.say(x)
    engine.runAndWait()


speechtx(" Hello, I'm Raspberry. What can I do for you today?")

if __name__ == '__main__':
    
    if "hello" in speaktx():
        while True:
            data1 = speaktx()
            if "your name" in data1:
                
                name = "My name is Raspberry"
                print(data1)
                speechtx(name)
            
            elif "old are you" in data1 or "age" in data1:
                age = "I am a python program created by Hamdhan, and I don't have an age. I don't possess personal experiences or a physical form. If you have any questions or need assistance, feel free to ask!"
                speechtx(age)
            
            elif 'time' in data1:
                time=datetime.datetime.now().strftime("It is %I:%M%p right now")
                speechtx(time)
            
            elif 'youtube' in data1:
                browser = webbrowser.get()
                browser.open("https://www.youtube.com/")
                youtubeprompt="opening Youtube..."
                speechtx(youtubeprompt)
                
            elif "WhatsApp" in data1:
               subprocess.run(['start', 'whatsapp://'], shell=True, check=True)
               whatsappprompt="Opening whats app.."
               speechtx(whatsappprompt)
                
            elif "discord" in data1:
                os.system("start C:\\Users\\91860\\AppData\\Local\\Discord\\app-1.0.9032\\Discord.exe")
                disordprompt="opening discord..."
                speechtx(disordprompt)
            
            elif 'instagram' in data1:
                webbrowser.open("https://www.instagram.com/?hl=en")
                instagramprompt="Opening Instagram..."
                speechtx(instagramprompt)
                
            elif 'Google' in data1:
                webbrowser.open("https://www.google.com/")
                googleprompt="opening google..."
                speechtx(googleprompt)
                
            elif "chat gpt" in data1:
                webbrowser.open("https://chat.openai.com/")
                gptprompt="opening chat GPT..."
                speechtx(gptprompt)
                
            elif "flipkart" in data1:
                webbrowser.open("https://www.flipkart.com/")
                flipkartprompt="opening flipkart..."
                speechtx(flipkartprompt)
            
            elif "mail" in data1 or "g mail" in data1:
                webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
                mailprompt="opening mail..."
                speechtx(mailprompt)
                
            elif 'play song'in data1:
                address="C:\\Users\\91860\\Songs"
                listsong = os.listdir(address)
                print(listsong)
                os.startfile(os.path.join(address,listsong[0]))
                songprompt="playing Skyfall by Adele"
                speechtx(songprompt)
                
            elif 'play music'in data1:
                address="C:\\Users\\91860\\Songs"
                listsong = os.listdir(address)
                print(listsong)
                os.startfile(os.path.join(address,listsong[1]))
                songprompt2="playing Never let go of me by Baltra"
                speechtx(songprompt2)
                
            elif "thanks" in data1 or "thank you" in data1:
                speechtx("You're welcome! If you have any more questions or if there's anything else I can help you with, feel free to ask")
                break
            
            elif "exit" in data1:
                speechtx("Bye, hoping to see you soon")
                break
                      
    else:
            
            print("Bye, hoping to see you soon")
                
                
                
                
            

                
            
        
                
                
