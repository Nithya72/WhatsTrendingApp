import pandas as pd

def getCountryData(country):
    if (country == "US"):
        return pd.read_csv("usa_trending_videos.csv")
    elif (country == "CA"):
        return pd.read_csv("./transformed/CA_trending_videos.csv")
    elif (country == "UK"):
        return pd.read_csv("./transformed/GB_trending_videos.csv")
    elif (country == "FR"):
        return pd.read_csv("./transformed/FR_trending_videos.csv")
    elif (country == "DE"):
        return pd.read_csv("./transformed/DE_trending_videos.csv")
    elif (country == "MX"):
        return pd.read_csv("./dataset/MX_trending1.csv")


def getCategoryDesc(country):
    description = ''
    if (country == "US"):
        description = 'Videos of category Entertainment are the most trending in US'
    elif (country == "CA"):
        description = 'Videos of category Entertainment are the most trending in CA'
    elif (country == "UK"):
        description = 'Videos of category Entertainment are the most trending in UK'
    elif (country == "FR"):
        description = 'Videos of category Entertainment are the most trending in FR'
    elif (country == "DE"):
        description = 'Videos of category Entertainment are the most trending in DE'
    elif (country == "MX"):
        description = 'Videos of category Entertainment are the most trending in MX'
    return description


def getPublishHour(country):
    description = ''
    if (country == "US"):
        description = 'Videos published in this hour are the most trending in US'
    elif (country == "CA"):
        description = 'Videos of category Entertainment are the most trending in CA'
    elif (country == "UK"):
        description = 'Videos of category Entertainment are the most trending in UK'
    elif (country == "FR"):
        description = 'Videos of category Entertainment are the most trending in FR'
    elif (country == "DE"):
        description = 'Videos of category Entertainment are the most trending in DE'
    elif (country == "MX"):
        description = 'Videos of category Entertainment are the most trending in MX'
    return description





