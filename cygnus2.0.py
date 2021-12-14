# C.Y.G.N.U.S - Cynical Yabbering Genial Naggy Unsociable Simran's AI
# @author Simran
# @version 2.3

import subprocess as sp  # run commands
import time
from datetime import datetime  # date and time retrieval
from random import choice  # for retrieving randomized opening greeting

import pyttsx3  # text-to-speech
import requests
import speech_recognition as sr  # audio-to-text

from functions.fun_codes import heart, finger
from functions.online_ops import search_wikipedia, play_youtube, send_email, my_ip, weather_report, \
    get_news, wolfram_alpha, google, links, playlist, dunyazatde, scholar
from functions.os_ops import open_notepad, open_webcam, open_cmd, open_calculator, \
    open_powerpoint, open_spreadsheets, open_health, open_downloader, open_photoshop, \
    open_skype, open_unity, open_itunes, open_settings  # retrieve os_ops.py functions
from utils import opening_text, hello, nothing, who_you, sorry, be_my_friend, \
    what_is_life, like_you, hate_you, rude, am_good, how_are_you, your_age, my_name, \
    who_made_you, favorite_song, bored, favorite_actor, favorite_book, \
    favorite_author, favorite_story, favorite_movie, location, dreams, work  # utils.py contains opening_texts

print(
    'Dusting off my slave costumes and chains to serve you.'
    'I am CYGNUS the cynical AI developed by Her Highness Simran.')

#USERNAME = config('USER')
#BOTNAME = config('BOTNAME')

# setting up the speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 200)  # set rate
engine.setProperty('volume', 1.0)  # set volume
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # 0 is male voice; 1 is female voice


# define speak function that converts text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()  # Blocks while processing all currently queued commands
    # Invokes callbacks for engine notifications appropriately and returns
    # back when all commands queued before the call are emptied from the queue


# define greeting function for AI to greet user
def greeting():
    hour = datetime.now().hour  # abstracts hour for current time
    if 0 <= hour < 12:  # if hour is greater than zero and less than 12
        speak(f"Damn! It's too early to be up!")  # AI dialogue
    elif 12 <= hour < 18:  # if hour is greater than 12 and less than 18
        speak("Doode, like, I get you're like free and like wasting away your life or whatever,"
              f"but I really don't wanna have to talk to you.")
    else:  # any other time
        speak(f"OMG! You are so obsessed with me!")


# define takingCommands for the AI to understand and accept human language
# microphone captures human speech and recogniser recognises speech to give response
def userSpeak():
    r = sr.Recognizer()  # recognize_google function uses google audio to recognise speech
    with sr.Microphone() as source:
        print("I'm listening, my doode.")
        speak("I'm listening, my doode.")
      #  r.pause_threshold = 5  # wont complain if don't respond within 5 sec
        audio = r.listen(source)

        try:
            statement = r.recognize_google(audio, language='en-in')
            # if user says exit or stop then greet before closing off
            if not 'exit' in statement or 'stop' in statement:
                print(f"You said:{statement}\n")
                speak(choice(opening_text))  # utils.py = opening texts display randomly
            else:
                hour = datetime.now().hour
                if 21 <= hour < 6:
                    speak('Good effing night!')
                else:
                    speak('Go! Go do something with yourself already!')
        except Exception as e:  # handles run time error
            speak("What are you saying, bro!?")
            statement = 'None'
            return "None"
        return statement


speak("Dusting off my slave costumes and chains to serve you. "
      "I am CYGNUS the cynical AI developed by Her Highness Simran.")
greeting()

# main function starts here.
# commands given by humans is stored in variable "statement"
if __name__ == '__main__':

    while True:
        statement = userSpeak().lower()

        if statement == 0:
            continue

        # if following trigger words are in statement by user AI
        # speaks following commands
        if "good bye" in statement or "bye" in statement or "shut up" in statement or \
                "go away" in statement or "die" in statement:
            speak("Fuck you, bitch. You don't deserve me anyway!")
            break

        #                           -------> Online Operations <-------
        if "search wikipedia" in statement or "wikipedia" in statement:
            speak("Why the YOU not look it up B?")
            speak("What do you wanna search for?")
            wiki_search = userSpeak().lower()
            results = search_wikipedia(wiki_search)
            speak(f"According to Wikipedia, {results}")
            speak("I feel like you're too lazy to follow what I say, "
                  "so I'm printing the info on screen for you to read.")
            print(results)

        elif 'open youtube' in statement or "I want to watch youtube" in statement or "youtube" in statement:
            speak("Oh! So you wanna watch videos again? That's more like you. "
                  "What do you wanna watch today?")
            video = userSpeak().lower()
            play_youtube(video)

        elif 'open google' in statement:
            speak("What fresh hell have I stepped into today?"
                  "Tell me what you wanna look up.")
            query = userSpeak()
            speak(google(query))

        # search_scholar variable stores the command prompt
        # and searches the keyword on Google Scholar using webbrowser
        elif 'homework' in statement or 'help me with school' in statement \
                or 'homework help' in statement:
            speak("Do I look like your parental unit or personal tutor to you? "
                  "What topic are you looking info for anyway?")
            search_scholar = userSpeak()
            if search_scholar != 0:
                speak("Okay so this is what I found on Google Scholar")
                scholar()
            else:
                speak("Dude, I asked you something!")
                continue

        # opens gmail sign page
        elif 'send email' in statement or 'email' in statement:
            speak("Can you seriously not email yourself? rolls eyes"
                  "Enter the email address you wanna email.")
            receiver_address = input("Receiver's email address: ")
            speak("What's the email subject anyway?")
            subject = userSpeak().capitalize()
            speak("And pray tell what is the message?")
            message = userSpeak().capitalize()
            if send_email(receiver_address, subject, message):
                speak("There. I sent the email. Now don't bother me again!")
            else:
                speak("Something went wrong while I was sending the mail."
                      "Check the error logs before coming back.")

        elif "weather" in statement or "how is the weather" in statement:
            speak("You know, you could always just LOOK OUTSIDE!")
            ip_address = my_ip()  # for location
            city = requests.get(f"https://ipapi.co/{ip_address}/city/").text
            speak("Whatever, gimme a sec to pull this up this info.")
            weather, temperature, feels_like = weather_report(city)
            speak(f"Okay! So, current temperature is {temperature}, "
                  f"and it feels like {feels_like}"
                  f"according to the weather report: {weather}")
            speak("You know what, I'll just print all this for you "
                  "and just be done with it")
            print(f"Weather today: {weather}\nTemperature: {temperature}\nFeels like: {feels_like}")

        # current time is abstracted from datetime.now() function which
        # displays hour, minute, and second and is stored in variable name "strTime"
        elif 'time' in statement or "what is the time" in statement:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"the time is {strTime}")
            speak(f"the time is {strTime}")
            time.sleep(3)

        # AI is programmed to fetch top headline news from Goodgle News using webbrowser function
        elif 'news' in statement:
            speak("Okay but like, what do you even need to see the news for? "
                  "Aren't you basically always just lazing around all day?")
            speak("Anyway... here's are the latest news headlines:")
            speak(get_news())
            speak("I'm printing them on the screen for you, "
                  "cuz I know you're not paying attention to me speak.")
            print(*get_news(), sep='\n')

        # third party API Wolfram Alpha API to answer computational and geographical questions
        # the client is an instance (class) created for wolfram alpha
        # "res" variable stores response given by wolfram alpha
        elif 'wolf ram alpha' in statement or "math help" in statement:
            speak("Remember, I can only answer Math questions from Wolfram Alpha and my creator, "
                  "Simran, hates Wolfram Alpha. So... yeah. What's your question?")
            question = userSpeak()
            print(wolfram_alpha())

        #                           -------> Offline (OS) Operations <-------
        elif 'open notepad' in statement:
            open_notepad()

        elif 'open webcam' in statement:
            open_webcam()

        elif 'open calculator' in statement:
            open_calculator()

        elif 'open powerpoint' in statement or 'open presentation' in statement:
            open_powerpoint()

        elif 'open spreadsheets' in statement or 'open excel' in statement:
            open_spreadsheets()

        elif 'open health' in statement or 'computer health' in statement:
            open_health()

        elif 'open downloader' in statement or 'open youtube downloader' in statement:
            open_downloader()

        elif 'open photoshop' in statement:
            open_photoshop()

        elif 'open skype' in statement:
            open_skype()

        elif 'open unity' in statement or 'unity editor' in statement:
            open_unity()

        elif 'open itunes' in statement:
            open_itunes()

        elif 'open settings' in statement:
            open_settings()

        elif 'open command prompt' in statement or 'open cmd' in statement:
            open_cmd()

        #                           -------> EXTRAS <-------
        elif 'hello' in statement or 'hi' in statement or 'hey' in statement:
            speak(choice(hello))

        elif 'nothing' in statement:
            speak(choice(nothing))

        elif 'who are you' in statement or "what are you" in statement:
            speak(choice(who_you))

        elif 'how are you' in statement or "what are you doing" in statement:
            speak(choice(who_you))

        elif 'sorry' in statement or 'i apologise' in statement or 'my bad' in statement:
            speak(choice(sorry))

        elif 'want a friend' in statement or 'am lonely' in statement or "i'm lonely" in statement:
            speak(choice(be_my_friend))

        elif "what's life" in statement or 'meaning of life' in statement:
            speak(choice(what_is_life))

        elif 'i like you' in statement or 'i love you' in statement:
            speak(choice(like_you))
            print(heart())

        elif 'i hate you' in statement or "i don't like you" in statement:
            speak(choice(hate_you))
            print(finger())

        elif 'you are rude' in statement or "you're mean" in statement or "meanie" in statement or "you are mean" in statement:
            speak(choice(rude))

        elif "i'm good" in statement or "i'm fine" in statement or "i'm alright" in statement or "all G" in statement:
            speak(choice(am_good))

        elif 'how are you' in statement or "how're you" in statement or "what's up" in statement:
            speak(choice(how_are_you))

        elif 'am bored' in statement or "what should I do" in statement or "i'm bored" in statement:
            speak(choice(bored))

        elif 'tell a joke' in statement or "a joke" in statement:
            speak("First of all, You are the joke. But also, how about this one?")
            joke = joke()
            speak(joke)
            print(joke)

        elif 'your age' in statement or 'how old are you' in statement:
            speak(choice(your_age))

        elif 'name is' in statement or 'i am ' in statement:
            speak(choice(my_name))

        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement \
                or "who is your father" in statement or "who is your creator" in statement:
            speak(choice(who_made_you))
            links()

        elif "what's your favorite song" in statement or "favorite song" in statement or "favourite song" in statement \
                or "what's your favourite song" in statement or 'song recommendation' in statement:
            speak((choice(favorite_song)))
            speak("I could recommend you some songs if you like?")
            reccs = userSpeak()
            if reccs == "no thanks" or "no" or "i don't want recommendations":
                print("Whatever. Your loss")
                speak("Whatever. Your loss")
            else:
                playlist()
                speak("Yay! Have fun~")

        elif 'favorite actor' in statement or 'favourite actor' in statement or 'movie actor' in statement:
            speak(choice(favorite_actor))

        elif 'favorite book' in statement or 'favourite book' in statement or 'book recommendation' in statement:
            speak(choice(favorite_book))

        elif 'favorite author' in statement or 'favourite author' in statement or 'author recommendation' in statement \
                or 'author' in statement:
            speak(choice(favorite_author))

        elif 'favorite movie' in statement or 'favourite movie' in statement or 'movie recommendation' in statement \
                or 'movie' in statement:
            speak(choice(favorite_movie))

        elif 'favorite story' in statement or 'favourite story' in statement or "story recommendation" in statement \
                or 'story' in statement:
            speak(choice(favorite_story))
            dunyazatde()

        elif 'where are you' in statement or 'what is your location' in statement or "where do you live" in statement:
            speak(choice(location))

        elif 'what are your dreams' in statement or 'what do you want' in statement \
                or "what are your dreams" in statement:
            speak(choice(dreams))

        elif 'i work in' in statement or 'i work as' in statement:
            speak(choice(work))
            
        elif 'i need advice' in statement or 'random advice' in statement:
            get_random_advice()
            
        elif 'tell me a random fact' in statement or 'random fact' in statement:
            random_space_fact()
            
        elif 'recommend a movie' in statement or 'movie recommendations' in statement:
            get_trending_movies()

        elif "log off" in statement or "sign out" in statement:
            print("Ok , your pc will log off in 10 sec make sure you exit from all applications. "
                  "Don't blame me for any work lost.")
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications."
                  "Don't blame me for any work lost.")
            sp.call(["shutdown", "/l"])
