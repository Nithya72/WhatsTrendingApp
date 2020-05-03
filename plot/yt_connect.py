# Reference from - https://medium.com/@yuhuiluo/automating-youtube-comment-sentiment-analysis-b4e2969eb62f

import httplib2
import re

import nltk
from nltk.tokenize import word_tokenize

from nltk.corpus import stopwords
# from nltk.sentiment.vader import SentimentIntensityAnalyzer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from apiclient.discovery import build_from_document
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import argparser, run_flow

CLIENT_SECRETS_FILE = "client_secrets.json"

YOUTUBE_READ_WRITE_SSL_SCOPE = "https://www.googleapis.com/auth/youtube.force-ssl"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

MISSING_CLIENT_SECRETS_MESSAGE = """WARNING: Please configure OAuth 2.0
To make this sample run you will need to populate the client_secrets.json file"""

def get_authenticated_service(args):
    flow = flow_from_clientsecrets(CLIENT_SECRETS_FILE, scope=YOUTUBE_READ_WRITE_SSL_SCOPE, message=MISSING_CLIENT_SECRETS_MESSAGE)

    storage = Storage("main.py-oauth2.json")
    credentials = storage.get()

    if credentials is None or credentials.invalid:
        credentials = run_flow(flow, storage, args)

    with open("youtube-v3-discoverydocument.json", "r") as f:
        doc = f.read()
        return build_from_document(doc, http=credentials.authorize(httplib2.Http()))


def get_comment_threads(youtube, video_id, comments=[], token=""):
    results = youtube.commentThreads().list(
        part="snippet",
        pageToken=token,
        videoId=video_id,
        textFormat="plainText"
    ).execute()

    for item in results["items"]:
        comment = item["snippet"]["topLevelComment"]
        text = comment["snippet"]["textDisplay"]
        comments.append(text)

    if "nextPageToken" in results:
        print("nextPageToken - comments", len(comments))
        return get_comment_threads(youtube, video_id, comments, results["nextPageToken"])
    else:
        return comments

def process_comments(video_comment_threads):

    comments = []
    for comment in video_comment_threads:
        stop_words = list(set(stopwords.words('english')))
        allowed_word_types = ["JJ"]

        cleaned = re.sub(r'[^(a-zA-Z)\s]', '', str(comment))

        tokenized = word_tokenize(cleaned)
        print(tokenized)
        stopped = [w for w in tokenized if not w in stop_words]

        pos = nltk.pos_tag(stopped)
        # print(pos)
        for words in pos:
            if words[1] in allowed_word_types:
                comments.append(words[0].lower())
    return comments


def generate(video_id):
    youtube = get_authenticated_service(video_id)
    video_comment_threads = get_comment_threads(youtube, video_id, [])
    # comments = process_comments(video_comment_threads)
    sia = SentimentIntensityAnalyzer()

    pol_comments = []
    for c in video_comment_threads:
        score = sia.polarity_scores(c)['compound']
        pol_comments.append((c, score))

    # for comment in pol_comments:
    #     print(comment)

    return pol_comments
