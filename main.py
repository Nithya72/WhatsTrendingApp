from flask import Flask, send_file, render_template, request, redirect
from plot import usaTrending
from plot import showTrending
from plot import sentiment
from plot import loadCountry
from flask_bootstrap import Bootstrap
from plot import dataFormatter
import pandas as pd

app = Flask(__name__)

bootstrap = Bootstrap(app)

@app.route("/")
def home():
    return render_template("index.html", title='Home', noHomePageLink=True)


@app.route("/videoInput")
def getIdForSentimentAnalysis_func():
    return render_template("videoInput.html", title='Sentimental Analysis')


@app.route("/sentiment", methods=["POST"])
def sentimentAnalysis():
    videoId = request.form['videoId']
    html_text = [(sentiment.get_videoid(videoId), "senti")]
    return render_template("videoInput.html", title="Sentimental Analysis", graph=html_text)


@app.route("/countries")
def countries_func():
    return render_template("countries.html", title='Countries')


@app.route("/countries/<country>")
def load_country_func(country):
    return redirect('/countries/' + country + "/category")


@app.route("/countries/<country>/category")
def showCategory(country):
    df = loadCountry.getCountryData(country)
    desc = loadCountry.getCategoryDesc(country)
    if (country == "US" or country == "MX"):
        html_graph = [(showTrending.plot_title(df), "cat")]
    else:
        html_graph = [(showTrending.plot_category(df), "cat")]
    return render_template("category.html", title="Category", graph=html_graph, analysis=desc, country=country)


@app.route("/countries/<country>/wordTags")
def showWordTags(country):
    df = loadCountry.getCountryData(country)
    html_graph = [showTrending.plot_tags_word_cloud(df)]
    return render_template("tagword.html", title=country, graph=html_graph, country=country)


@app.route("/countries/<country>/publishHour")
def showPublishHour(country):
    df = loadCountry.getCountryData(country)
    desc = loadCountry.getPublishHour(country)
    html_graph = [showTrending.plot_publish_hours(df)]
    return render_template("publishHour.html", title="Publish Hour", graph=html_graph, analysis=desc, country=country)


@app.route("/countries/<country>/tagCount")
def showTagCount(country):
    df = loadCountry.getCountryData(country)
    html_graph = [showTrending.plot_tags(df)]
    return render_template("tagCount.html", title="Tag count", graph=html_graph, analysis='', country=country)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8000)
    app.jinja_env.auto_reload = True
    app.run(debug=True)
    app.config(TEMPLATES_AUTO_RELOAD=True)
