from flask import Flask, send_file, render_template

from plot import trending

app = Flask(__name__)



@app.route("/")
def home():
    return render_template("index.html", title='Home Page', noHomePageLink=True)


@app.route("/usTrend")
def usTrend_func():
    # trending.plot_category()
    html_text = [trending.plot_tags(), trending.plot_publish_hours(), trending.plot_subscribers()]
    return render_template("US.html", title="United States", graph=html_text)


@app.route("/canadaTrend")
def canadaTrend_func():
    return render_template("Canada.html", title="Canada")


if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.run(debug=True)
    app.config(TEMPLATES_AUTO_RELOAD=True)
