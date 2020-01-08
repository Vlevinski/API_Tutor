#
#     requests by urllib3
###
import urllib3
import json
import logging
logging.getLogger("urllib3").setLevel(logging.WARNING)


http = urllib3.PoolManager()
r = http.request(
        'GET',
        'https://jsonvat.com/',
        fields={'arg': 'value'})
data = json.loads(r.data.decode('utf-8'))
print( len(data))
print ( data.keys())
#print ( json.dumps(data,indent=4))
#print (json.dumps(data,indent=4))
for item in data['rates']:
    print (item)
    print (" Country:", item["name"],"- ", item['country_code'])
