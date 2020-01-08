import json
import urllib3

def getExchangeRates():
    rates = []
    http = urllib3.PoolManager()
    response = http.request('GET', 'http://data.fixer.io/api/latest?access_key=???????')
    rdata = response.data
    rdata = json.loads(rdata, parse_float=float)
    print (json.dumps(rdata,indent=4))
    rates.append( rdata['rates']['USD'] )
    rates.append( rdata['rates']['GBP'] )
    rates.append( rdata['rates']['JPY'] )
    rates.append( rdata['rates']['AUD'] )
    return rates

rates = getExchangeRates()
print (rates)
