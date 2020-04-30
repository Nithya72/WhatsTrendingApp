import warnings

warnings.filterwarnings('always')
warnings.filterwarnings('ignore')

import pandas as pd
from pandas import read_csv
import matplotlib.pyplot as plt, mpld3
from matplotlib.pyplot import axis
import seaborn as sb
import os
from os import path 
import sys 
import time 
import numpy as np

df = read_csv("dataset/USA_trending_videos.csv")

# def read_file(csv_name: str):
#     file_path = os.path.join("dataset", csv_name)  # concat path name
#     if path.exists(file_path):
#         print("filepath:", file_path)
#         global df
#         df = read_csv(file_path)
#         plot_tags()
#     else: 
#         sys.stdout.write("File doesn't exist!")
#         exit() 

# def create_plot(csv_name: str): 
#     read_file(csv_name)
#     time.sleep(1)
#     #plot_category()
#     #plot_publish_hours()
#     plot_tags()
#     #plot_subscribers()

def plot_category():
    print("plot_category")
    fig, output = sb.factorplot(data=df, kind='count', size=2, aspect=1, x='title_y')
    output.set_xticklabels(rotation=90)
    return mpld3.fig_to_html(fig)


def plot_publish_hours():
    print("publish_hours")
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

# def heatmap():
#     fig = plt.figure()
#     df = pd.DataFrame(np.random.random((10,10)), columns=["a","b","c","d","e","f","g","h","i","j"])
#     sb.heatmap(df, cmap="YlGnBu")
#     return mpld3.fig_to_html(fig)


def heatmap():
    fig = plt.figure()
    corrolation_list = ['views', 'likes', 'dislikes', 'comment_count']
    hm_data = df[corrolation_list].corr()
    fig.savefig(sb.pairplot(df[['views', 'likes']], kind='reg'))
    fig = plt.show()
    return mpld3.fig_to_html(fig)
