import configparser
import requests
import sys
import os
import pyowm
from inspect import signature
from selenium.webdriver.common.keys import Keys
import wikipedia
import json
import requests
import urllib.request
import random as rn
from bs4 import BeautifulSoup

bad_words = ('fuck', 'shit', 'خرا', 'cunt', 'cock', 'bitch', 'faggot', 'gay')

def fcommand(message):
    print("running")
    fcom = message.split(" ", 1)
    print(fcom)
    com = fcom[0][1:]
    if com in globals():
        methodToCall = globals()[com]
        params = signature(methodToCall).parameters
        print(len(params))
        print(params)
        if len(params) == 0 or len(fcom) == 1:
            return methodToCall()
        else:
            return methodToCall(fcom[1])


def weather(country="kuwait"):
    owm = pyowm.OWM('ea073e04bc85f31dab1408ad497f277f')
    obs = owm.weather_at_place(country)
    w = obs.get_weather()
    t = w.get_temperature(unit='celsius')["temp"]
    return f"The weather in {obs.get_location().get_name()} is\
     {w.get_detailed_status()}, it is {t} degrees outside.\n"


def echo(sent=''):
    sent = sent.split()
    for index, word in enumerate(sent):
        if any(badword in word for badword in bad_words):
            sent[index] = "".join(['*' if c.isalpha() else c for c in word])
    return " ".join(sent) + '\n'


hm = "Commands:\n*$echo:* Repeats what you say.\n*$weather [city]:* returns weather and temperature in given location.\n*$meme:* return random meme from reddit.\n*$youtube [subject]:* return first youtube search result on subject.\n*$wiki [topic]:* returns short summary on given topic _usually doesn't work well_.\n*$quote:* return famous quote.\n*$random:* return random useless fact.\n*$flip:* flips a coin.\n"


def help():
    return hm


def hi():
    return "Hello! Please use $help for command list :)\n"


def wiki(sub):
    return wikipedia.summary(sub, sentences=2) + '\n'


def quote():
    response = requests.get(
        'https://api.forismatic.com/api/1.0/?method=getQuote&format=json&lang=en')
    data = json.loads(response.text)
    a = '"' + data["quoteText"] + '" - ' + data["quoteAuthor"]
    return a + '\n'


def random():
    response = requests.get(
        "https://uselessfacts.jsph.pl/random.json?language=en")
    data = json.loads(response.text)
    return data["text"] + '\n'


def meme():
    response = requests.get(
        "https://meme-api.herokuapp.com/gimme/memes")
    data = json.loads(response.text)
    return data["url"]


def youtube(vide):
    print(vide)
    textToSearch = vide
    query = urllib.parse.quote(textToSearch)
    url = "https://www.youtube.com/results?search_query=" + query
    response = urllib.request.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    vids = soup.findAll(attrs={'class': 'yt-uix-tile-link'})
    return 'https://www.youtube.com' + vids[0]['href'] + '\n'


def flip():
    coin = bool(rn.getrandbits(1))
    if coin:
        return 'Coin flipped. You got Heads!\n'
    else:
        return 'Coin flipped. You got Tails!\n'
