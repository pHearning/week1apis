import urllib.request
import urllib.parse
import json as m_json

def watson1(query):
    query = urllib.parse.urlencode ( { 'q' : query } )
    response = urllib.request.urlopen ( 'https://www.googleapis.com/customsearch/v1?key=<your-key>&cx=<your-cx>&' + query ).read()
    json = m_json.loads ( response.decode('utf8') )
    results = json['items']
    for result in results:
        title = result['title']
        url = result['link']   # was URL in the original and that threw a name error exception
        snippet = result['snippet']
        print("""{title} 
{snippet} 
{url}

""".format(title=title, snippet=snippet, url=url))

query = input ( 'Question: ' )
watson1(query)
