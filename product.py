import json
import urllib

url = "http://octopart.com/api/v3/categories/search"
url += "?apikey=42a364b98a6361cc27cc"

args = [
   ('q', 'semiconductors'),
   ('start', 0),
   ('limit', 10)
   ]

url += '&' + urllib.urlencode(args)

data = urllib.urlopen(url).read()
search_response = json.loads(data)

# print number of hits
print search_response['hits']

# print results
for result in search_response['results']:
   # print matched category
   print result['item']['name']
