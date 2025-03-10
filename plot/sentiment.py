import matplotlib.pyplot as plt, mpld3
from matplotlib.pyplot import pie, axis, show
import io

def get_videoid(video_id):

    print("video_id", video_id)
    from plot import yt_connect
    pol_comments = yt_connect.generate(video_id)

    print("plot comments", len(pol_comments))
    neutral = 0;
    positive = 0;
    negative = 0;

    for com in pol_comments:
        # print(com[1])
        if (com[1] >= 0.01):
            positive = positive + 1;
        elif (com[1] <= -0.01):
            negative = negative + 1;
        else:
            neutral = neutral + 1;

    names = ["Neutral", "Negative", "Positive"]
    values = [neutral, negative, positive]

    # names = ["Positive", "Negative"]
    # values = [positive, negative]

    fig, ax = plt.subplots()
    explode = (0, 0, 0.01)
    ax.pie(values, labels=names, autopct='%1.0f%%', explode=explode,
           shadow=False, startangle=0, labeldistance=1.05)
    ax.axis('equal')
    return mpld3.fig_to_html(fig)
