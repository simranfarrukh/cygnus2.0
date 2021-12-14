# C.Y.G.N.U.S AI

CYGNUS, the Cynical AI, combines snarky responses with uncanny aggression. (because JARVIS as a little piece of shit is the best headcanon ever!) Using Speech Recognition as user input, Cygnus can perform several simple tasks with a voice feedback.

Some things Cygnus can do:
```bash
Online Operations
# get my IP
# search Wikipedia
# play Youtube Videos
# search Google Web & Google Scholar
# send Whatsapp Message (as long as logged into Whatsapp for Web)
# send Email
# get News (latest headlines)
# predict Weather & Time
# perform calculations through Wolfram Alpha
# get Trending Movies through TMDB
# get Random Space Facts from: fungenerators.com (for fun & because I love Space)
# get Random Jokes from: icanhazdadjoke.com (again, for fun)
# get Random Advice from: api.adviceslip.com (again, for fun purposes)

Offline Operations
# open Webcam Notepad, Calculator, 
# open Microsoft Word, Powerpoint, Spreedsheets
# open Computer Health, Settings, CMD
# open 4K Downloader, Photoshop, Skype, Unity Editor, iTunes 
# Be a Snarky, Witty Talk-back AI Bot
```


## System Requirements (install using pip)
CYGNUS works primarily on Python for now and requires the below mentioned imports to work:
```python
import speech_recognition as sr
import pyttsx3
import wikipedia
import wikipediaapi
import time
import wolframalpha
import json
import requests
from newsapi import NewsApiClient
import pywhatkit as kit
from turtle import *
```
## In-built libraries:
Below mentioned libraries are pre-installed with Python but still need to be imported:
```python
import os
import datetime
import webbrowser
import subprocess
from decouple import config  
from datetime import datetime
from random import choice 
from email.message import EmailMessage
import smtplib
```
## Project Specific Imports:
Below mentioned imports are project specific files that contain the online and offline functions that make CYNUS work.
```python
# imports from fun_codes.py file in the functions folder
from functions.fun_codes import heart, finger   

# imports from the online_ops.py file in the functions folder 
from functions.online_ops import search_wikipedia, play_youtube, search_google, send_email, my_ip, weather_report, \
    get_news, wolfram_alpha, google, links, playlist, dunyazatde, scholar  

# imports from the os_ops.py file in the functions folder
from functions.os_ops import paths, open_notepad, open_webcam, open_cmd, open_calculator, \
    open_powerpoint, open_spreadsheets, open_health, open_downloader, open_photoshop, \
    open_skype, open_unity, open_itunes, open_settings

# imports from the utils.py file
from utils import opening_text, hello, nothing, who_you, sorry, be_my_friend, \
    what_is_life, like_you, hate_you, rude, am_good, how_are_you, your_age, my_name, \
    who_made_you, favorite_song, bored, favorite_actor, favorite_book, \
    favorite_author, favorite_story, favorite_movie, location, dreams, work
```

## Commands
Below is a list of some of the commands you can try giving the AI:

```bash
"search Wikipedia" or "Wikipedia" to open Wikipedia API

"open YouTube" or "i want to watch YouTube" or "YouTube" to play YouTube Video

"open Google" to open Google in the browser

"search google" to open search keyword in Google browser

"homework help" or "homework" or "help me with school" to open Google Scholar

"weather" or "how is the weather" to open Weather predictions for your city

"time" or "what is the time" to open time prediction

"news" to open Latest Trending News stories in NewsApi

"calculate" or "math help" to open Wolfram Alpha for calculations

"log off" or "sign out" to shut down the program

```
Please also try talking to the AI, asking random questions beyond the normal tasks listed above.


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
Copyright Exclusive to Simran Farrukh
