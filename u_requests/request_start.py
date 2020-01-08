#
#
###

import urllib3
import json
import io

uri = 'http://httpbin.org/ip'
http = urllib3.PoolManager()
r= http.request('GET',uri)
print(r.status)
print(json.loads(r.data.decode('utf-8')))
