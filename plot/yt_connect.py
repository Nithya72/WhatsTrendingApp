# Reference from - https://medium.com/@yuhuiluo/automating-youtube-comment-sentiment-analysis-b4e2969eb62f

import httplib2
import os

# nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from apiclient.discovery import build_from_document
# from googleapiclient.discovery import build_from_document
from apiclient.errors import HttpError
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import argparser, run_flow

CLIENT_SECRETS_FILE = "client_secrets.json"

YOUTUBE_READ_WRITE_SSL_SCOPE = "https://www.googleapis.com/auth/youtube.force-ssl"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

MISSING_CLIENT_SECRETS_MESSAGE = """
WARNING: Please configure OAuth 2.0
To make this sample run you will need to populate the client_secrets.json file
found at:
   %s
with information from the APIs Console
https://console.developers.google.com
For more information about the client_secrets.json file format, please visit:
https://developers.google.com/api-client-library/python/guide/aaa_client_secrets
""" % os.path.abspath(os.path.join(os.path.dirname(__file__),
                                   CLIENT_SECRETS_FILE))

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

    # print("Comments length - ", len(comments))

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

def generate(video_id):

    youtube = get_authenticated_service(video_id)
    video_comment_threads = get_comment_threads(youtube, video_id, [])
    sia = SentimentIntensityAnalyzer()

    pol_comments = []
    for comments in video_comment_threads:
        score = sia.polarity_scores(comments)['compound']
        pol_comments.append((comments, score))

    return pol_comments


# def main():
#     generate("0mlNzVSJrT0")

# main()