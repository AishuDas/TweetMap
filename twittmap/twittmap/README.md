# twittmap
First-Phase-TwitterMap

Front End: Ajax, Jquery

Back End: Django

Database: ElasticSearch

Deployed on: Amazon AWS ELastic BeanStalk

Link: http://tweetygooglemap-dev.us-west-2.elasticbeanstalk.com

This web app is dedicated to displaying the location of keyword based tweets on Google map. 
Tweets were collected using the twitter streaming API and stored on the ElasticSearch. 
Based on what option(keyword) user chooses from the drop down menu, the app retreives the tweets related to that keywords 
from the ElasticSearch and displays the location from where it was tweeted on Google Maps.

To use, clone the project and enter the required keys for Twitter and Google API and host name of your ElasticSearch. Install dependencies and in the terminal enter "pyhton manage.py runserver".

Dependencies: Requests, Tweepy and Elasticsearch. To install dependencies install pip and run "pip install 'name of dependency'" on terminal.
![capture](https://cloud.githubusercontent.com/assets/16929465/19770582/cd242d5c-9c2d-11e6-857e-8261c6e22b38.PNG)
![zoomed](https://cloud.githubusercontent.com/assets/16929465/19770586/d0fb7142-9c2d-11e6-8f27-f070e38844e8.PNG)

