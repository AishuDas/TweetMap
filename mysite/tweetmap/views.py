from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from elasticsearch import Elasticsearch
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
from elasticsearch import Elasticsearch, RequestsHttpConnection
import time
import geocoder
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.views.decorators.cache import cache_page
from textwrap import TextWrapper
import requests
from django.template import*
from django.template import Context
from django.template.loader import get_template


def index(request):
    return render(request, 'tweetmap/header.html')

# authentication details for AWS Elasticsearch
host = "http://search-tweetmap-3irxvi2quadmyikuw2vh6227rq.us-east-1.es.amazonaws.com/test-index/tweet/_search?size=10000&q="


def gettweet(request):
    string = request.GET.get("abc")

    def search(link, key):
        final_link = link + key
        response = requests.get(final_link)
        results = json.loads(response.text)
        return results

    r = search(host, string)

    coordinate1 = []
    data = r['hits']['hits']

    for i in data:
        coordinate1.append(i['_source']['coordinates']['coordinates'])

    list = Context({'coordinatelist': coordinate1})

    return render(request, "tweetmap/index.html", {"coordinatelist": coordinate1})
