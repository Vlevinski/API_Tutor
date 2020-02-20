from flask import Flask, render_template
from flask_googlecharts import GoogleCharts, BubbleChart
import json
import urllib3

app = Flask(__name__)
charts = GoogleCharts(app)


def getExchangeRates():
    # get exchage rates
    ratesj = {}
    http = urllib3.PoolManager()
    response = http.request('GET', 'http://data.fixer.io/api/latest?access_key=??????????')
    rdata = response.data
    rdata = json.loads(rdata, parse_float=float)
    ratesj['USD'] = rdata['rates']['USD']
    ratesj['GBP'] = rdata['rates']['GBP']
    ratesj['EUR'] = rdata['rates']['EUR']
    ratesj['AUD'] = rdata['rates']['AUD']
    ratesj['CHF'] = rdata['rates']['CHF']
    ratesj['SGD'] = rdata['rates']['SGD']
    ratesj['CAD'] = rdata['rates']['CAD']
    ratesj['GEL'] = rdata['rates']['GEL']
    ratesj['BZD'] = rdata['rates']['BZD']
    return ratesj


@app.route("/rates")
def hotdogs():
    # get rates and plot charts
    rates = getExchangeRates()
    currency = BubbleChart("currency", options={"title": "Currency rates",
                                                "hAxis": {"title": 'Currency'},
                                                "vAxis": {"title": 'Rates'},
                                                "width": 1000,
                                                "height": 600})
    currency.add_column("string", "Currency")
    currency.add_column("number", "rates")
    currency.add_column("number", "id")
    currency.add_column("number", "color")
    currency.add_column("number", "value")
    ident = 0.5
    for curr, vals in rates.items():
        currency.add_rows([[curr, ident, vals, vals, vals]])
        ident += 1
    charts.register(currency)
    return render_template("rates.html", rates=rates)


@app.route("/pie")
def pie_chart():
    # pie chart in html
    return render_template("pie_chart.html")

@app.route("/")
def hello():
    return "Hello API World!  try /rates, /pie"


if __name__ == "__main__":
    app.run()
