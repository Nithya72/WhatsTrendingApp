
import warnings

import matplotlib
import mpld3

warnings.filterwarnings('always')
warnings.filterwarnings('ignore')

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import pie, axis, show
import seaborn as sb
import io
from wordcloud import WordCloud, STOPWORDS

df = pd.read_csv("USA_trending_videos.csv")

def convertToBytesImage(output):
    bytes_image = io.BytesIO()
    plt.savefig(bytes_image, format='png', bbox_inches="tight")
    bytes_image.seek(0)
    show(bytes_image)
    return bytes_image

def plot_category():
    fig = plt.figure()
    output = sb.distplot(df['publish_hour'], color="maroon")

    output.set_xlabel("Publish Hour", fontsize=12)
    output.set_ylabel("Trending Level", fontsize=12)
    byte_op = convertToBytesImage(fig)
    return byte_op

# plot_category()

def plot_tags():
    plt.figure(figsize=(8, 8), )
    fig = plt.subplots(subplot_kw={'xticks': [], 'yticks': [-1]})
    stopwords = set(STOPWORDS)
    wordcloud = WordCloud( background_color= 'black', stopwords = stopwords, max_words = 500, max_font_size = 120, random_state = 42).generate(str(df['tags']))
    plt.imshow(wordcloud)
    plt.title('Word Cloud for Tags', fontsize = 20)
    # plt.axis('off')
    # plt.show()

    byte_op = convertToBytesImage(fig)
    return byte_op

def scatterplot():
    fig = plt.figure()
    corrolation_list = ['views', 'likes', 'dislikes', 'comment_count']
    hm_data = df[corrolation_list].corr()
    matplotlib.pyplot.figure(figsize=(5,5))
    sb.scatterplot(x=df['views'], y=df['likes'])
    byte_op = convertToBytesImage(fig)
    # return byte_op

scatterplot()


