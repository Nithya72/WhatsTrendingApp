# **What's Trending?**
## **Abstract**
What's trending is intended to help Youtubers from different countries to visualize what type of video content is the most popular in their country. Our team acquired data from the top trending YouTube videos from different countries and formed visual statistics of popular video categories, popular video tags, favorable hours to publish videos and relevance between number of tags and trending level. Users can make use of this information to make their YouTube videos trend in a country.

This application has an added functionality that projects the sentiment of a video based on the viewer comments. User can use this sentimental analysis result to find out how exactly is the video received by the viewers. This information will be helpful to the youtubers to create contents in a more responsible way.

## **Practical scenarios on how this tool can be used:**

### **Use case 1:** 
A user based in USA wants to create a YouTube video and make it trend.

Based on the statistics projected in US trending videos page, the user can infer the following:<br>
•	 Creating an Entertainment specific contents has higher chance of making their video trend in YouTube.<br>
•	 The user should publish the video around 4 – 5 PM to get more views.<br>
•	 There is no significant relation found between the number of tags and the video becoming popular. So, the user can use any number of tags related to their video content.<br>
•	 Suggested tags to trend the video - #FoodASMR, #breaking, #movies etc.

### **Use case 2:**
A youtuber saw a trending video of a man mocking specially challenged people. The user finds the video funny and wants to create similar contents and make it trend. 

**Sentiment Analysis report:**
More than half of the viewers (54%) found the video to be very offensive to specially challenged people and not funny. So, the youtuber can possibly avoid posting such objectionable contents.

**Negativity projected in the comments:**
insensitive, obnoxious, unacceptable, mad, awful, harassment etc.,


### **Use case 3:**
A YouTube viewer wants to see how people felt after the latest coronavirus update provided by New York state Governor

**Sentiment Analysis report:**
People were having mixed emotions – 35% of the people were staying positive and 42% were losing hopes.

**Emotions projected in the comments:**
Good, aggressive, vulnerable, responsible, careful, healthy,  etc.


## **Architecture Diagram**
![Architecture Diagram](https://github.com/SJSUSpring2020-CMPE272/Whats-Trending/blob/develop/Final%20Architecture.png)


## **Technology Stack**
Github, Flask, AWS, Docker, Nginx, Youtube Data API v3, Machine Learning algorithm (NLTK Vader SentimentIntensityAnalyzer), Python, Matplotlib, Seaborn, HTML/CSS, Bootstrap


## **View website**
The docker daemon is running the website on the AWS EC2 Instance. The webpage will be viewable at the Elastic IP 52.88.197.158:80 
```
52.88.197.158:80
```

# **Notes To Run The Application**

## **Set up virtual environment**
This contains all the packages and dependencies used. 
```
source venv/bin/activate
venv\Scripts\activate
```

If you don't need view website on localhost anymore, deactivate the virtual environment. 
```
deactivate
```

## Build & Run Docker Image 
This step is helpful if you want to save multiple versions of your project and share them with others. Make sure to [install
Docker](https://www.docker.com/products/docker-desktop) first! The key resource used here is the [uWSGI-Nginx-Flask](https://hub.docker.com/r/tiangolo/uwsgi-nginx-flask/)
container-- it combines all 3 applications into one container simpliying the process. We only needed to pull the tag and copy our files into the our
project's container.

We can start by building the image. Make sure to name and tag it so it's easy to reference back to (here the name is *myapp* with *tag* 1.0). When building the image, specify the path or directory that the *Dockerfile*
is located in. In this case, we are already in the same directory as the Dockerfile so we use ' . ' to indicate the current directory. 
```
docker build -t myapp:1.0 .
```

Once complete, you can view your image in your repository. 
```
docker images
```

Now run the image! Use ' -p ' to publish container's port to your host machine. The value on the left side of the colon
means host's port and the right value is the container's port. By default, the container's port is on 80. 
```
docker run -p 80:80 myapp
```

The docker image is also available on our [Docker Hub](https://hub.docker.com/repository/docker/lindatvy/whatstrendingapp).

## To get the client_secrets.json
1. Go to [Google Cloud Console](https://console.cloud.google.com) and create a new project. 
2. Enable the YouTube Data API v3.
3. Create credentials (OAuth client ID, Application Type: Other) and download them to `client_secrets.json`.
4. Place the downloaded `client_secrets.json` under the main package WhatsTrendingApp

## **References:**
1. [Modify & Redeploy Cloud Foundry App](https://cloud.ibm.com/docs/starters?topic=starters-download-modify-and-redeploy-your-cloud-foundry-app-with-the-command-line-interface)
2. [Johnafish/senticomment](https://github.com/johnafish/senticomment)
3. [Webpage Icons](https://www.flaticon.com/packs/survey-feedback-2)
4. [uWSGI-Nginx-Flask Docker Image](https://hub.docker.com/r/tiangolo/uwsgi-nginx-flask/)
