from flask import Flask, send_file, render_template, request
from plot import usaTrending
from plot import showTrending
from plot import sentiment
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
    return render_template("videoInput.html", title='Analyze your data set')


@app.route("/sentiment", methods=["POST"])
def sentimentAnalysis():
    videoId = request.form['videoId']
    html_text = [sentiment.get_videoid(videoId)]
    return render_template("videoInput.html", title="Sentimental Analysis", graph=html_text)


@app.route("/countries")
def countries_func():
    return render_template("countries.html", title='Countries')


@app.route("/usTrend")
def usTrend_func():
    html_text = [usaTrending.plot_category(),
                 usaTrending.plot_publish_hours(),
                 usaTrending.plot_tags(),
                 usaTrending.plot_tags_word_cloud(), "cloud"]
    return render_template("US.html", title="United States", graph=html_text)

@app.route("/canadaTrend")
def canadaTrend_func():
    return render_template("Canada.html", title="Canada")


@app.route("/indiaTrend")
def indiaTrend_func():
    dataFormatter.processData("./dataset/INvideos.csv", './dataset/IN_category_id.json', 'IN')
    df = pd.read_csv("./transformed/IN_trending_videos.csv")
    html_text = [showTrending.plot_category(df), showTrending.plot_publish_hours(df),
                 showTrending.plot_tags_word_cloud(df)]
    return render_template("India.html", title="India")


@app.route("/mexicoTrend")
def mexicoTrend_func():
    dataFormatter.processData("./dataset/MX_trending.csv", './dataset/MX_category_id.json', 'MX')
    df = pd.read_csv("./transformed/MX_trending_videos.csv")
    html_text = [showTrending.plot_category(df), showTrending.plot_publish_hours(df),
                 showTrending.plot_tags_word_cloud(df)]
    return render_template("Mexico.html", title="Mexico", graph=html_text)


@app.route("/koreaTrend")
def koreaTrend_func():
    dataFormatter.processData("./dataset/KRvideos.csv", './dataset/KR_category_id.json', 'KR')
    df = pd.read_csv("./transformed/KR_trending_videos.csv")
    html_text = [showTrending.plot_category(df), showTrending.plot_publish_hours(df),
                 showTrending.plot_tags_word_cloud(df)]
    return render_template("Korea.html", title="Korea")


@app.route("/franceTrend")
def franceTrend_func():
    dataFormatter.processData("./dataset/FRvideos.csv", './dataset/FR_category_id.json', 'FR')
    df = pd.read_csv("./transformed/FR_trending_videos.csv")
    html_text = [showTrending.plot_category(df), showTrending.plot_publish_hours(df), showTrending.plot_tags_word_cloud(df)]
    return render_template("Mexico.html", title="Mexico", graph=html_text)

@app.route("/gbTrend")
def gbTrend_func():
    dataFormatter.processData("./dataset/GBvideos.csv", './dataset/GB_category_id.json', 'GB')
    df = pd.read_csv("./transformed/GB_trending_videos.csv")
    html_text = [showTrending.plot_category(df), showTrending.plot_tags_word_cloud(df)]
    return render_template("gb.html", title="Great Britain", graph=html_text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=80)
    app.jinja_env.auto_reload = True
    app.run(debug=True)
    app.config(TEMPLATES_AUTO_RELOAD=True)