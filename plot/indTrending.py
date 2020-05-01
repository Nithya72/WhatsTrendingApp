import matplotlib.pyplot as plt, mpld3
from matplotlib.pyplot import pie, axis, show
import io

def plot_senti():

    # video_id = "hPmBSTgBmes" - positive
    video_id1 = "DQDj074iEuM" #mocking negtaive

    from plot import yt_connect
    pol_comments = yt_connect.generate(video_id1)

    print("plot comments", len(pol_comments))
    neutral = 0;
    positive = 0;
    negative = 0;

    for com in pol_comments:
        # print(com[1])
        if (com[1] >= 0.05):
            positive = positive + 1;
        elif (com[1] <= -0.05):
            negative = negative + 1;
        else:
            neutral = neutral + 1;

    names = ["positive", "negtaive", "neutral"]
    values = [positive, negative, neutral]

    fig, ax = plt.subplots()
    explode = (0.1, 0, 1)
    ax.pie(values, labels=names, autopct='%1.0f%%', explode=explode,
           shadow=False, startangle=0,
           pctdistance=1.2, labeldistance=1.4)
    ax.axis('equal')
    return mpld3.fig_to_html(fig)
#
# def plot_senti1():
#     video_id1 = "DQDj074iEuM"
#
#     pol_comments = []
#     from plot import main2
#     pol_comments = main2.generate(video_id1)
#
#     print("plot 1 comments", len(pol_comments))
#     neutral = 0;
#     positive = 0;
#     negative = 0;
#
#     for com in pol_comments:
#         # print(com[1])
#         if (com[1] >= 0.05):
#             positive = positive + 1;
#         elif (com[1] <= -0.05):
#             negative = negative + 1;
#         else:
#             neutral = neutral + 1;
#
#     # if(negative > positive):
#     #     negative = negative+neutral
#     # elif(positive < negative):
#     #     positive = positive+neutral
#
#     names = ["positive", "negtaive", "neutral"]
#     values = [positive, negative, neutral]
#
#     fig = plt.figure(figsize=(3,3))
#     plt.bar(names, values)
#     return mpld3.fig_to_html(fig)
#
#
# def plot_senti2():
#     video_id1 = "DQDj074iEuM"
#
#     pol_comments = []
#     from plot import main2
#     pol_comments = main2.generate(video_id1)
#
#     print("plot 2 comments", len(pol_comments))
#     neutral = 0;
#     positive = 0;
#     negative = 0;
#
#     for com in pol_comments:
#         # print(com[1])
#         if (com[1] >= 0.05):
#             positive = positive + 1;
#         elif (com[1] <= -0.05):
#             negative = negative + 1;
#         else:
#             neutral = neutral + 1;
#
#     names = ["positive", "negtaive", "neutral"]
#     values = [positive, negative, neutral]
#
#     fig = plt.figure(figsize=(3, 3))
#     plt.bar(names, values)
#     return mpld3.fig_to_html(fig)
