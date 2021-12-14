# Online Operations
import requests  # allows sending HTTP/1.1 requests
import wikipedia  # retrieves info from Wikipedia
import pywhatkit as kit  # allows browser interactions
from email.message import EmailMessage
import smtplib
from decouple import config
import wolframalpha
import webbrowser

EMAIL = config('EMAIL')
PASSWORD = config('PASSWORD')
NEWS_API_KEY = config("NEWS_API_KEY")
OPENWEATHER_APP_ID = config("OPENWEATHER_APP_ID")
TMDB_API_KEY = config("TMDB_API_KEY")
WOLFRAMALPHA_API_ID = config("WOLFRAMALPHA_API_ID")


# make a GET request on the ipify url
def my_ip():  # returns json data of IP
    ip_address = requests.get('https://api64.ipify.org?format=json').json()
    return ip_address["ip"]


def search_wikipedia(statement):  # summary() accepts statement as args
    results = wikipedia.summary(statement, sentences=3)
    return results


# uses pywhatkit module
def play_youtube(video):  # playonyt() accepts topic as args
    kit.playonyt(video)  # search topic on YT and plays appropriate vid


# uses pywhatkit module
def search_google(statement):  # search() allows search on Google
    kit.search(statement)


# uses pywhatkit module
# should be logged into WhatsApp for Web
def whatsapp_message(number, message):  # two args: number, message
    kit.sendwhatmsg_instantly(f"+91{number}", message)


# uses smtplib
# args: receiver_email, subject, message
def send_email(receiver_email, subject, message):
    try:  # create an object of SMTP class from smtplib
        email = EmailMessage()
        email['To'] = receiver_email
        email['Subject'] = subject
        email['From'] = EMAIL
        email.set_content(message)
        s = smtplib.SMTP('smtp.gmail.com', 587)  # object params: host, port number
        s.starttls()
        s.login(EMAIL, PASSWORD)  # EMAIL & PASSWORD should be in .env file
        s.send_message(email)
        s.close()
        return True
    except Exception as e:
        print(e)
        return False


def get_news():
    news_headlines = []  # create empty list news_headlines
    res = requests.get(  # make GET request on API URL -> gives JSON response
        f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API_KEY}&category=general").json()
    articles = res['articles']  # list of articles with value res['articles']
    for article in articles:  # iterate over article list & append article['title']
        news_headlines.append(article['title'])  # to news_headlines list
    return news_headlines[:5]  # return first five news headlines from list


# make GET request from openweathermap api URL with city name
def weather_report(city):  # get JSON response
    response = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_APP_ID}&units=metric").json()
    weather = response['main']['weather']
    temperature = response['main']['temp']
    feels_like = response['main']['feels_like']
    return weather, f"{temperature}℃", f"{feels_like}℃"


# third party API Wolfram Alpha API to answer computational
def wolfram_alpha(question):
    client = wolframalpha.Client('WOLFRAMALPHA_API_ID')  # instance (class) created for wolfram alpha
    response = client.query(question)  # response variable stores response by WRA
    return next(response.results).text


# same as with news_headlines
def get_trending_movies():
    trending_movies = []  # create trending_movies list
    response = requests.get(  # make GET request on API URL -> gives JSON response
        f"https://api.themoviedb.org/3/trending/movie/day?api_key={TMDB_API_KEY}").json()
    results = response["results"]  # list of results
    for r in results:  # iterate over article list & append original_title
        trending_movies.append(r["original_title"])  # to trending_movies
    return trending_movies[:5]  # return first five titles from list


def random_space_fact():
    headers = {
        'Accept': 'application/json'
    }  # make a GET request on page URL
    response = requests.get("https://fungenerators.com/random/facts/space/", headers=headers).json()
    return response["space facts"]


def random_joke():
    # make a GET request on page URL
    response = requests.get("https://icanhazdadjoke.com/").json()
    return response["joke"]


def get_random_advice():
    # make a GET request on page URL
    response = requests.get("https://api.adviceslip.com/advice").json()
    return response['slip']['advice']  # return random advice slip as slip object


def google(statement):
    webbrowser.open_new_tab("https://www.google.com")
    search_google(statement)


def links():
    webbrowser.open_new_tab("https://www.dunyazatde.wordpress.com/")
    webbrowser.open_new_tab("https://www.simranfarrukh.com/")


def playlist():
    webbrowser.open_new_tab("https://www.youtube.com/watch?v=16hvzx8vjWI&list=PLUccfPy6p7tinPCCk5Cyntb7-OfykYRKa")


def dunyazatde():
    webbrowser.open_new_tab("https://dunyazatde.wordpress.com/category/short-stories/")


def scholar(search_scholar):
    webbrowser.open_new_tab("https://scholar.google.ca/scholar?hl=en&as_sdt=0%2C5&q=" + search_scholar)
