from flask import Flask
from flask import render_template
import feedparser
from flask import request
import json
import urllib.request as urllib2
import urllib.parse
import datetime
from flask import make_response

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile("config.py")

RSS_FEEDS = {
    "bbc": "http://feeds.bbci.co.uk/news/rss.xml",
    "cnn": "http://rss.cnn.com/rss/edition.rss",
    "fox": "http://feeds.foxnews.com/foxnews/latest",
    "iol": "http://www.iol.co.za/cmlink/1.640"
}
DEFAULTS = {
    "publication": "bbc",
    "city":"Nairobi,Kenya",
    "currency_from": "GBP",
    "currency_to": "USD"
}

WEATHER_API = app.config["WEATHER_API_KEY"]
CURRENCY_API = app.config["CURRENCY_API_KEY"]

WEATHER_URL =  "http://api.openweathermap.org/data/2.5/weather?q={0}&units=metric&appid={1}"
CURRENCY_URL = "https://openexchangerates.org//api/latest.json?app_id={}"

def get_value_with_fallback(key):
    if request.args.get(key):
        return request.args.get(key)
    if request.cookies.get(key):
        return request.cookies.get(key)
    
    return DEFAULTS[key]


@app.route("/")
def home():
    # get customized headlines, based on user input or default
    publication = get_value_with_fallback("publication")
    articles = get_news(publication)

    # get customized weather based on user input or default
    city = get_value_with_fallback("city")
    weather = get_weather(city)

    # get customized currency based on user input or default
    currency_from = get_value_with_fallback("currency_from")
    currency_to = get_value_with_fallback("currency_to")    
    rate, currencies = get_rates(currency_from, currency_to)

    response = make_response(
        render_template(
            "home.html",
            articles=articles,
            weather=weather,
            currency_from=currency_from,
            currency_to=currency_to,
            rate=rate,
            currencies = sorted(currencies)
        )
    )
    expires = datetime.datetime.now() + datetime.timedelta(days=365)
    response.set_cookie("publication", publication, expires=expires)
    response.set_cookie("city", city, expires=expires)
    response.set_cookie("currency_from", currency_from, expires=expires)
    response.set_cookie("currency_to", currency_to, expires=expires)
    return response

def get_news(query):
    if not query or query.lower() not in RSS_FEEDS:
        publication = DEFAULTS["publication"]
    else:
        publication = query.lower()
    feed = feedparser.parse(RSS_FEEDS[publication])
    return feed["entries"]

def get_weather(query):
    query = urllib.parse.quote(query)
    url = WEATHER_URL.format(query, WEATHER_API)
    data = urllib2.urlopen(url).read()
    parsed = json.loads(data)
    weather = None
    if parsed.get("weather"):
        weather = {
            "description": parsed["weather"][0]["description"],
            "temperature": parsed["main"]["temp"],
            "city": parsed["name"],
            "country": parsed["sys"]["country"]
        }
    return weather

def get_rates(frm, to):
    url = CURRENCY_URL.format(CURRENCY_API)
    all_currrency = urllib2.urlopen(url).read()
    parsed = json.loads(all_currrency).get("rates")
    frm_rate = parsed.get(frm.upper())
    to_rate = parsed.get(to.upper())
    return (to_rate/frm_rate, parsed.keys())


if __name__ == "__main__":
    app.run(port=5000, debug=True)