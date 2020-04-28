import warnings

warnings.filterwarnings('always')
warnings.filterwarnings('ignore')

from pandas import read_csv
import matplotlib.pyplot as plt, mpld3
from matplotlib.pyplot import axis
import seaborn as sb
import matplotlib
matplotlib.use('Agg')
from wordcloud import WordCloud, STOPWORDS

df = read_csv("usa_trending_videos.csv")


def plot_category():
    fig = plt.figure(figsize=(10, 4))
    output = sb.countplot(x='title_id', data=df, palette="Blues_d", order=df['title_id'].value_counts().index)
    output.set_xticklabels(output.get_xticklabels(), rotation=45, ha="right")
    plt.tick_params(rotation=45)
    plt.xticks(rotation=45)
    output.set_title("Trending Video Categories", fontsize=20)
    output.set_ylabel("Trending Videos Count", fontsize=12)
    plt.subplots_adjust(wspace=0.9, hspace=0.9, top=0.9)
    return mpld3.fig_to_html(fig)

def plot_publish_hours():
    fig = plt.figure()
    output = sb.distplot(df['publish_hour'], color="maroon")
    output.set_xlabel("Publish Hour", fontsize=12)
    output.set_ylabel("Trending Level", fontsize=12)
    # plt.ylabel("Trending Level")
    return mpld3.fig_to_html(fig)

def plot_tags():
    fig = plt.figure()
    sb.distplot(df['tags_count'], color="teal")
    plt.ylabel("Trending Level")
    return mpld3.fig_to_html(fig)

# def plot_subscribers():
#     fig = plt.figure()
#     sums = df.groupby(df["title_y"])["subscriber"].sum()
#     axis('equal')
#     plt.pie(sums, autopct='%.2f')
#     return mpld3.fig_to_html(fig)

def plot_tags_word_cloud():
    plt.axis('off')
    fig = plt.figure(figsize=(8, 8))
    # fig = plt.subplots(subplot_kw={'xticks': [], 'yticks': [-1]})
    stopwords = set(STOPWORDS)
    wordcloud = WordCloud( background_color= 'black', stopwords = stopwords, max_words = 1000, max_font_size = 120, random_state = 42).generate(str(df['tags']))
    plt.imshow(wordcloud)
    plt.title('Word Cloud for Tags', fontsize = 20)
    return mpld3.fig_to_html(fig)
