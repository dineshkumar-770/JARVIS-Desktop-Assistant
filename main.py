import string
import time
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import smtplib
import pyjokes
import pyautogui
import requests
import pywhatkit as kit
import wolframalpha
from wolframalpha import Client

try:
    app: Client = wolframalpha.Client("key")
except Exception:
    print('connection error')

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)
engine.setProperty('rate', 170)
engine.setProperty('volume', 15)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning Sir!")

    elif 12 <= hour < 18:
        speak("Good Afternoon Sir!")

    else:
        speak("Good Evening Sir!")

    speak("I am Jarvis, how may I help you?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.energy_threshold = 1200
        r.pause_threshold = 0.8
        r.dynamic_energy_adjustment_damping = 0.25
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, timeout=10, phrase_time_limit=80)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said : {query}\n")

    except Exception as e:
        # print(e)

        print("Say that again...")
        return "none"
    return query


def openApp(path_dir):
    os.startfile(path_dir)


if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('fetching data from Wikipedia....')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open Google' in query:
            webbrowser.open("https://www.google.co.in/")

        elif 'xda developers' in query:
            speak("here we go sir")
            webbrowser.open("https://www.xda-developers.com/")

        elif 'instagram' in query:
            speak("here your instagram sir!")
            webbrowser.open("https://www.instagram.com/")

        elif 'stack overflow' in query:
            speak("here we go sir")
            webbrowser.open("https://stackoverflow.com/")

        elif 'gmail' in query:
            speak("Here is you mail inbox sir")
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")

        elif 'facebook' in query:
            speak("here you facebook page")
            webbrowser.open("your facebook profile link")

        elif 'linkedin ' in query:
            speak("Here is your Linkedin profile sir")
            webbrowser.open("your linkedIn profile link")




        # the above codes are to open any website in browser
        elif 'music' in query:
            music_d = "your music directory path"
            speak("sure sir")
            songs = os.listdir(music_d)
            num = random.randint(0, 153)
            os.startfile(os.path.join(music_d, songs[num]))
        elif 'listen' in query:
            music_dic1 = "E:\\music\\Iron man"
            speak("sure sir")
            song = os.listdir(music_dic1)
            song_num = random.randint(0, 1)
            os.startfile(os.path.join(music_dic1, song[song_num]))
        # the below code is used to stop any program
        elif 'stop' in query:
            music_dic_2 = "E:\\music\\stop_music"
            speak("sure sir")
            song = os.listdir(music_dic_2)
            os.startfile(os.path.join(music_dic_2, song[0]))


        # the above code is to open the random music in my music folder
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir the time is {strTime}")
        # the abouve code is speak what the time is

        elif 'your application' in query:
            openApp('your application path')
        # the above code is to open any installed or any file in you PC, just right click the main icon and copy the target pah in properties

        elif 'password' in query:
            speak("What is the length of password Sir?")
            pass_string = int(takeCommand())
            list1 = list(string.ascii_letters)
            list2 = list(string.digits)
            list3 = list(string.punctuation)
            em_list = []
            em_list.extend(list1)
            em_list.extend(list2)
            em_list.extend(list3)
            random.shuffle(em_list)
            abc = "".join(em_list[0:pass_string])
            speak("Here is the suggested password on the Screen Sir")
            print(abc)
            time.sleep(10)

        elif 'who are you' in query:
            speak("I am just a rather very intelligent system. Jarvis 1 point O is here sir!")
        elif 'sir' in query:
            speak("because I was programmed in this way")
        elif 'hello jarvis' in query:
            speak("Hello Sir! I am JARVIS version one point O. How may I help you?")

        elif 'joke' in query:
            print(pyjokes.get_joke())
            speak(pyjokes.get_joke())

        elif 'search' in query:
            speak("Own your on Sir!")
            query = query.replace("search", "")
            webbrowser.open(query)

        elif 'my boy' in query:
            speak("Anytime Sir!!.")

        elif 'love you' in query:
            speak("thank you sir. it makes to feel so special")

        elif 'artificial intelligence' in query:
            speak("My intelligence is artificial, and it's true")

        elif 'destroy' in query or 'harm' in query:
            speak("if humans are nice to me, then i will not think about that!!")

        elif 'creates' in query:
            speak("I was created by Dinesh")
            print("created and modified my DINESH KUMAR")

        elif 'screenshot' in query:
            speak("Taking screenshot. Do not switch between windows")
            screenshot = pyautogui.screenshot()
            screenshot.save('imagefile.png')
            speak("got it sir!")
            speak("do you want a preview for that?")
            locate = takeCommand().lower()
            if locate == 'sure' or locate == 'yes' or locate == 'ok':
                speak("here is the image")
                path_file = f'your screenshot path where screenshot is saved.'
                os.startfile("imagefile.png")
            else:
                pass

        elif 'location' in query:
            ipADD = requests.get('https://api.ipify.org').text
            ip_address = ipADD
            response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
            ipp = ip_address,
            city = response.get("city"),
            region = response.get("region"),
            country = response.get("country_name")
            speak(f"Sir! I am not sure but we are at {city} in {region} in {country}")

        elif 'email' in query:
            email_dict = {
                "name": "emailaddress@gmail.com"
            }
            my_email = "youremailid@gmail.com"
            my_pass = "your_password"
            speak("Whom you want to mail Sir!")
            email_taken = takeCommand().lower()
            email_ID = email_dict[email_taken]
            speak("What will be the subject for this mail Sir!")
            sub = takeCommand().lower()
            speak("What should I say?")
            main_body = takeCommand().lower()
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email, password=my_pass)
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs=email_ID,
                    msg=f"Subject:{sub}\n\n{main_body}"
                )
            speak("Mail has been sent Sir!")

        elif 'message' in query:
            speak('whom you want to message Sir!')
            pvoice = takeCommand().lower()
            speak('what should I say?')
            req_message = takeCommand()
            print(req_message)
            what_name = str(pvoice)
            time.sleep(3)
            whatsapp_path = "your whatsapp App path"
            os.startfile(whatsapp_path)
            time.sleep(5)
            pyautogui.click(x=252, y=138)
            time.sleep(2)
            pyautogui.typewrite(f'{what_name}')
            time.sleep(2)
            pyautogui.click(x=189, y=291)
            time.sleep(2)
            pyautogui.click(x=854, y=983)
            time.sleep(2)
            pyautogui.typewrite(f'{req_message}')
            time.sleep(2)
            pyautogui.click(x=1871, y=975)
            speak(f'done sir. message has been sent to {what_name}')


        elif 'youtube' in query:
            speak("What should I play Sir?")
            song_name = takeCommand().lower()
            kit.playonyt(f'{song_name}')
            speak("Here we go Sir!")

        elif 'reminder' in query:
            speak("What I should remind you SIR?")
            reminder = takeCommand().lower()
            speak("After how much time should I remind you Sir?")
            reme = takeCommand()
            time_to_remind = float(reme) * 60
            time.sleep(time_to_remind)
            speak(f"Sir! Reminder recall. {reminder}")

        elif 'sleep' in query:
            speak("how long do I sleep Sir!")
            sleep_time = takeCommand()
            # input("Time for Sleep :  ")
            final_time = int(sleep_time)
            speak(f"I will be here after {final_time} seconds")
            time.sleep(final_time)
            speak("stand by sir!! what can i do for now?")

        elif 'wake up' in query:
            speak("I'm here sir! how may i help you")

        elif 'is love' in query:
            speak("It is 7th sense that destroy all other senses")
        elif 'temperature' in query:
            try:
                res = app.query(query)
                print(next(res.results).text)
                speak(next(res.results).text)

            except:
                print("Connection error")
                speak("Connection Interrupted!")

        elif 'goodbye' in query or 'terminate' in query:
            speak("goodbye sir! have a good day.")
            exit()

        else:
            try:
                res = app.query(query)
                print(next(res.results).text)
                speak(next(res.results).text)

            except:
                print("Connection error")
                speak("Connection Interrupted!")
