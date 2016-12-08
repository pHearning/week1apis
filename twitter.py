import base64
import json
import urllib2

### Setup access credentials

consumer_key = "<key>"
consumer_secret = "<secret>"

### Get the Access Token

bearer_token = "%s:%s" % (consumer_key, consumer_secret)
bearer_token_64 = base64.b64encode(bearer_token)

token_request = urllib2.Request("https://api.twitter.com/oauth2/token") 
token_request.add_header("Content-Type", "application/x-www-form-urlencoded;charset=UTF-8")
token_request.add_header("Authorization", "Basic %s" % bearer_token_64)
token_request.data = "grant_type=client_credentials"

token_response = urllib2.urlopen(token_request)
token_contents = token_response.read()
token_data = json.loads(token_contents)
access_token = token_data["access_token"]

### Use the Access Token to make an API request

timeline_request = urllib2.Request("https://api.twitter.com/1.1/users/show.json?screen_name=elonmusk")
timeline_request.add_header("Authorization", "Bearer %s" % access_token)

timeline_response = urllib2.urlopen(timeline_request)
timeline_contents = timeline_response.read()
timeline_data = json.loads(timeline_contents)

print(timeline_contents)
print(timeline_data['name']+' said '+timeline_data['status']['text'])
