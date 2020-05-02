# **What's Trending?**
## **Description**
What's Trending is intended to help Youtubers from different regions visualize what type of content is the most popular in their country. Our application is using the data set from the ["Trending Youtube Video Statistics"](https://www.kaggle.com/datasnaek/youtube-new) Kaggle competition that has scraped data from several countries across the span of 6 months with 200 listings of trending videos daily. All data was captured in the same time frame. In our application, we analyzed the data sets from the USA, India, Mexico and Korea. 


## **Set up virtual environment**
This contains all the packages and dependencies used. 
```
source venv/bin/activate
```

If you don't need view website on localhost anymore, deactivate the virtual environment. 
```
deactivate
```


## **View website**
Now that the virtual environment is activated, you can run view the website on localhost:5000. 
```
python3 main.py
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

## **Resources**
[Modify & Redeploy Cloud Foundry App](https://cloud.ibm.com/docs/starters?topic=starters-download-modify-and-redeploy-your-cloud-foundry-app-with-the-command-line-interface)
