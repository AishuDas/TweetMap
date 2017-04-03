import json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from geopy.geocoders import Nominatim
from elasticsearch import Elasticsearch, RequestsHttpConnection
from requests_aws4auth import AWS4Auth
from textwrap import TextWrapper
import cgi
import sys


ckey=""  
csecret=""

atoken=""  
atoken_secret=""



class SListener(StreamListener):  
   
    def on_data(self, data):
	twitt_data = json.loads(data)
        try:
            status_wrapper = TextWrapper(width=60, initial_indent='    ', subsequent_indent='    ')
			
            if ('coordinates' in twitt_data.keys()):
				print data
				if (twitt_data['coordinates'] is not None):
					res = es.index(index="test-index", doc_type='tweet', body=twitt_data)
        except Exception, e:
			pass
			
	return True
		
		
	
	def on_error(self, status):
		print status
		exit()


if __name__ == '__main__':

    #This handles AWS ES authentication
    host = 'search-tweetmap-3irxvi2quadmyikuw2vh6227rq.us-east-1.es.amazonaws.com'
    awsauthentication = AWS4Auth('', '', 'us-east-1', 'es')



    es = Elasticsearch(
		hosts=[{'host': host, 'port': 443}],
		http_auth=awsauthentication,
		use_ssl=True,
		verify_certs=True,
		connection_class=RequestsHttpConnection
		)
		
print(es.info())
m = SListener()
auth = OAuthHandler(ckey, csecret)  
auth.set_access_token(atoken, atoken_secret)
stream = Stream(auth, m)

try:
	stream.filter(track=['trump','usa','football','india','modi','logan','facebook','elections','india','news','messi','money','food','car'])
except Exception, e:
	pass
