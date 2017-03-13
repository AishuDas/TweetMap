from django.shortcuts import render
from django.http import HttpResponse, request, JsonResponse
# from .forms import MyForm
import requests
import json

# Create your views here.
words=['elections','trump','modi','logan','football','facebook','india','news','oscars','acchedin']


def Index(Request):
    return render(Request, 'googleMapsTweet/base.html')


def Post(Request):
    if Request.method == "POST":
        msg = Request.POST.get('Search', None)

        #Give your Domain Host Address
        host = 'http://search-tweetmap-3irxvi2quadmyikuw2vh6227rq.us-east-1.es.amazonaws.com/test-index/tweet/_search?size=10000&q='

        def search(link, key):
            final_link = link + key
            response = requests.get(final_link)
            results = json.loads(response.text)
            return results

        if msg == 'elections':
            s = 0
        elif msg == 'trump':
            s = 1
        elif msg == 'modi':
            s = 2
        elif msg == 'logan':
            s = 3
        elif msg == 'football':
            s = 4
        elif msg == 'facebook':
            s = 5
        elif msg == 'india':
            s = 6
        elif msg == 'news':
            s = 7
        elif msg == 'oscars':
            s = 8
        elif msg == 'acchedin':
            s = 9

        r = search(host, words[s])
        data = [res['_source']['coordinates']['coordinates'] for res in r['hits']['hits']]
        print (data)
        hits = len(data)
        print (hits)
        length = {'hits': hits}
        coordinates = {}
        for i in range(hits):
            coordinates[i] = {'lat': data[i][0], 'lng': data[i][1]}

        data = {'coordinates': coordinates, 'length': length}
        print (data)
        return JsonResponse(data)