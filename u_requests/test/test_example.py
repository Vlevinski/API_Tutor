#
#     requests by urllib3
###
import urllib3
import json
import logging
logging.getLogger("urllib3").setLevel(logging.WARNING)


http = urllib3.PoolManager()
data = {
  "links": {
    "self": "http://example.com/articles/1"
  },
  "data": {
    "type": "articles",
    "id": "1",
    "attributes": {
      "title": "JSON:API paints my bikeshed!"
    },
    "relationships": {
      "author": {
        "links": {
          "related": "http://example.com/articles/1/author"
        }
      }
    }
  }
}
encoded_data = json.dumps(data).encode('utf-8')
def bnm_request():
    #   You can specify headers as a dictionary in the headers argument
    r = http.request('GET', 'http://example.com/articles/1',
                             body=encoded_data,
                             headers={ 'Content-Type: application/vnd.api+json'})
    print(json.loads(r.data.decode('utf-8'))['headers'])

bnm_request()
