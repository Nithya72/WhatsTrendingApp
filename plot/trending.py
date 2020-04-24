import warnings

warnings.filterwarnings('always')
warnings.filterwarnings('ignore')

from pandas import read_csv
import matplotlib.pyplot as plt, mpld3
from matplotlib.pyplot import axis
import seaborn as sb

df = read_csv("USA_trending_videos.csv")


def plot_category():
    fig, output = sb.factorplot(data=df, kind='count', size=2, aspect=1, x='title_y')
    output.set_xticklabels(rotation=90)
    return mpld3.fig_to_html(fig)


def plot_publish_hours():
    fig = plt.figure()
    sb.distplot(df['publish_hour'])
    plt.ylabel("Trending Level")
    return mpld3.fig_to_html(fig)


def plot_tags():
    fig = plt.figure()
    sb.distplot(df['tags_count'], color="maroon")
    plt.ylabel("Trending Level")
    return mpld3.fig_to_html(fig)


def plot_subscribers():
    fig = plt.figure()
    sums = df.groupby(df["title_y"])["subscriber"].sum()
    axis('equal')
    plt.pie(sums, autopct='%.2f')
    return mpld3.fig_to_html(fig)
