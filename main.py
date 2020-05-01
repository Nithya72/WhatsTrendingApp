from flask import Flask, send_file, render_template
from plot import usaTrending
from plot import indTrending
from flask_bootstrap import Bootstrap

app = Flask(__name__)

bootstrap = Bootstrap(app)

@app.route("/")
def home():
    return render_template("index.html", title='Home', noHomePageLink=True)


@app.route("/usTrend")
def usTrend_func():
    html_text = [[usaTrending.plot_category(), "cat"],
                 [usaTrending.plot_publish_hours(), "hrs"],
                 [usaTrending.plot_tags(), "tag"],
                 [usaTrending.plot_tags_word_cloud(), "cloud"]]
    return render_template("US.html", title="United States", graph=html_text)

@app.route("/canadaTrend")
def canadaTrend_func():
    return render_template("Canada.html", title="Canada")


@app.route("/indiaTrend")
def indiaTrend_func():
    html_text = [indTrending.plot_senti()]
    return render_template("India.html", title="India", graph=html_text)


@app.route("/mexicoTrend")
def mexicoTrend_func():
    return render_template("Mexico.html", title="Mexico")


@app.route("/koreaTrend")
def koreaTrend_func():
    return render_template("Korea.html", title="Korea")



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=80)
    app.jinja_env.auto_reload = True
    app.run(debug=True)
    app.config(TEMPLATES_AUTO_RELOAD=True)
