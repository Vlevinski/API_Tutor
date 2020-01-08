from flask import Flask, flash, redirect, render_template, request, session, abort, url_for, jsonify
from flask_googlecharts import GoogleCharts, BarChart, MaterialLineChart
import json
import urllib3

app = Flask(__name__)
charts = GoogleCharts(app)

def getExchangeRates():
    rates = []
    ratesj = {}
    http = urllib3.PoolManager()
    response = http.request('GET', 'http://data.fixer.io/api/latest?access_key=????')
    rdata = response.data
    rdata = json.loads(rdata, parse_float=float)
    ratesj[ 'USD'] = rdata['rates']['USD']
    ratesj[ 'GBP'] = rdata['rates']['GBP']
    ratesj[ 'EUR'] = rdata['rates']['EUR']
    ratesj[ 'AUD'] = rdata['rates']['AUD']
    return ratesj

@app.route("/rates")
def today_rates():
    rates = getExchangeRates()
    currency = BarChart("currency", options={"title": "Currency rates",
                                                  "width": 500,
                                                  "height": 300})
    currency.add_column("string", "Currency")
    currency.add_column("number", "rates")
    for curr,vals in rates.items():
        currency.add_rows([[curr, vals]])

    charts.register(currency)
    return render_template("rates.html", rates = rates)

@app.route("/")
def hello():
    return "Hello API World! Use /rates endpoint to get today rates :-)"

if __name__ == "__main__":
    app.run()
