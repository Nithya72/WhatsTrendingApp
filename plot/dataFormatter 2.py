#Lets load the necessary libraries using
import pandas as pd
import numpy as np
import seaborn as sns
import json
from matplotlib import cm
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

#read our dataset
def processData(csvFile, jsonFile, countryName):
    videos_df = pd.read_csv(csvFile, index_col='video_id')
    print(videos_df.head())
    #delete unnecessary columns
    del_cols = ['thumbnail_link', 'comments_disabled', 'ratings_disabled', 'video_error_or_removed', 'description']
    videos_df = videos_df.drop(del_cols, axis=1)
    #delete duplicates
    videos_df = videos_df.drop_duplicates(keep="first")
    #format trending date and publish time
    videos_df['trending_date'] = pd.to_datetime(videos_df['trending_date'], format='%y.%d.%m')
    videos_df['publish_time'] = pd.to_datetime(videos_df['publish_time'], format='%Y-%m-%dT%H:%M:%S.%fZ')
    # separate publish_time column into publish date and publish time columns
    videos_df.insert(4, 'publish_date', videos_df['publish_time'].dt.date)
    videos_df.insert(4,'publish_hour', videos_df['publish_time'].dt.hour)
    videos_df['publish_time'] = videos_df['publish_time'].dt.time
    #format category id
    videos_df['category_id'] = videos_df['category_id'].astype(str)
    #read json file and process it
    categories_df = pd.read_json(jsonFile)
    id_to_category = {}
    for category in categories_df['items']:
        id_to_category[category['id']] = category['snippet']['title']
    #add json data to csv data
    videos_df.insert(4, 'category', videos_df['category_id'].map(id_to_category))
    name = "./transformed/" +countryName + "_trending_videos.csv"
    videos_df.to_csv(name)

