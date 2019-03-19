from urllib.request import urlopen
from bs4 import BeautifulSoup
import matplotlib as plt
import numpy as np
from urllib.error import HTTPError
from urllib.error import URLError
from fastnumbers import isfloat
from fastnumbers import fast_float
import pandas as pd
import re
import datetime

class stock:
    def __init__(self, symbol):
        self.symbol = symbol # stock symbol as a string
        if self.finvizURLExist()[0]:
            self.quote = self.finvizTableTags()
        else:
            print(self.finvizURLExist()[1])
            print('Above error occured for symbol: ' + self.symbol)
            self.quote = []
            for i in range(144):
                self.quote.append('0.000000')

    def getName(self):
        # input: self
        # output: the name of the company as a string
        if self.finvizURLExist()[0]:
            html = urlopen(self.finvizUrl())
            bs = BeautifulSoup(html, 'html.parser')
            nameWords = bs.find('title').text.split()
            name = ''
            for i in range(1, len(nameWords) - 2):
                name = name + nameWords[i] + ' '
            return name
        else:
            return self.symbol + '(ERROR)'


    def getPrice(self):
        # input: self
        # output: the stock's closing price as a float
        return float(self.quote[131])

    def finvizTable(self):
        # input: self
        # output: the stock's quote table from finviz.com as a BeautifulSoup object
        """try:
            html = urlopen(self.finvizUrl())
        except HTTPError as e:
            print(e)
            print('WARNING! ' + self.symbol + ' is not available at finviz.com')
        except URLError as e:
            print(e)
            print('The finviz.com server could not be found')
        else:
            bs = BeautifulSoup(html, 'html.parser')
            return bs.find('table',{'class':'snapshot-table2'}).find_all('td')"""

    def finvizUrl(self):
        # input: self
        # output: finviz URL for the particular stock as a string
        return 'https://finviz.com/quote.ashx?t={}'.format(self.symbol)

    def getBeta(self):
        # input: self
        # output: the stock's beta
        return float(self.quote[83])

    def getPE(self):
        # input: self
        # output: the stock's P/E ratio
        return float(self.quote[3])

    def getEPS(self):
        # input: self
        # output: the stock's EPS as a float
        return float(self.quote[5])

    def getDividend(self):
        # input: self
        # output: the stock's dividend as a float
        return float(self.quote[73])

    def getDividendYield(self):
        # input: self
        # output: the stock's yield as a float
        return float(self.quote[85][:-1])

    def getDividendPayoutRatio(self):
        # input: self
        # output: the stock's dividend payout ratio as a float
        return float(self.quote[127][:-1])

    def get52WeekHigh(self):
        # input: self
        # output: the stock's 52 week high as a float
        return float(self.quote[69].split('-')[1])

    def get52WeekLow(self):
        # input: self
        # output: the stock's 52 week low as a float
        return float(self.quote[69].split('-')[0])

    def getDebtToEquity(self):
        # input: self
        # output: the stock's Debt-to-Equity ratio as a float
        return float(self.quote[111])

    def getPriceToBook(self):
        # input: self
        # output: the stock's Price-to-Book ratio as a float
        return float(self.quote[51])

    def plotPriceHistory(self, numberYears):
        # input: self, number of years as int
        # output: plot of stock price history going back numberYears (in years)

        return 0

    def getYTDGrowth(self):
        # input: self
        # output: the stock's YTD growth as a float
        return float(self.quote[71][:-1])

    def get3yrGrowth(self):
        # input: self
        # output: the stock's 3 year growth as a float
        return 0

    def get5yrGrowth(self):
        # input: self
        # output: the stock's 5 year growth as a float
        return 0

    def get10yrGrowth(self):
        # input: self
        # output: the stock's 10 year growth as a float
        return 0

    def getTargetPrice(self):
        # input: self
        # output: the stock's average analysts' price target as a float
        return float(self.quote[57])

    def getAnalystRecommendation(self):
        # input: self
        # output: the stock's analysis buy/sell recommendation as a float (1=buy, 5=sell)
        return float(self.quote[133])

    def printStockData(self):
        # input: self
        # output: print the stocks data
        dataTable = self.finvizTable()
        for entry in finvizTable():
            print(entry)
        return 0

    def priceVsTargetPrice(self):
        # input: self
        # output: price-to-target-price ratio as a float
        return self.getPrice()/self.getTargetPrice()

    def priceVs52WeekLow(self):
        # input: self
        # output: price-to-52-week-low ratio as a float
        return self.getPrice()/self.get52WeekLow()

    def priceVs52WeekHigh(self):
        # input: self
        # output: price-to-52-week-high ratio as a float
        return self.getPrice()/self.get52WeekHigh()

    def finvizTableTags(self):
        # input: self
        # output: the stock's quote table from finviz.com as a BeautifulSoup object
        html = urlopen(self.finvizUrl())
        bs = BeautifulSoup(html, 'html.parser')
        tdTags = bs.find('table',{'class':'snapshot-table2'}).find_all('td')
        tdText = []
        for tag in tdTags:
            tdText.append(tag.text)
        return tdText

    def finvizURLExist(self):
        # input: self
        # output: True if no errors arise when checking finviz for a stock symbol, else return False
        try:
            html = urlopen(self.finvizUrl())
        except HTTPError as e:
            return (False, e)
        except URLError as e:
            return (False, e)
        else:
            return (True, '')


class stockList:
    def __init__(self, filename):
        self.filename = filename
        # the filename of the file with the list of stock symbols as a string with stocks separated by commas
        self.stocksList = self.getStockList()
        self.stocksListQuote = self.stockListQuote()

    def getStockList(self):
        # input: self
        # output: array of strings of stock symbols
        file = self.filename
        f = open(file, "r").read().split(',')
        return f

    def stockListQuote(self):
        # input: self
        # output: array of stocks
        quoteList = []
        for security in self.stocksList:
            quoteList.append(stock(security))
        return quoteList






#***********************************************************************************************************************
# create stocks test
aapl = stock('AAPL')
googl = stock('GOOGL')
att = stock('T')
cci = stock('CCI')
mmm = stock('MMM')

"""print(aapl.getYTDGrowth())
print(aapl.getName())
print(aapl.getDividendYield())
print(aapl.getDividendPayoutRatio())
print(aapl.get52WeekHigh())
tableInfo = cci.finvizTableTags()
for n, i in enumerate(tableInfo):
    print(n, i)"""

print(aapl.getName() + ', ' + aapl.symbol + ': $' + str(aapl.getPrice()))
print(googl.getName() + ', ' + googl.symbol + ': $' + str(googl.getPrice()))
print(att.getName() + ', ' + att.symbol + ': $' + str(att.getPrice()))
print(cci.getName() + ', ' + cci.symbol + ': $' + str(cci.getPrice()))
print(mmm.getName() + ', ' + mmm.symbol + ': $' + str(mmm.getPrice()))

# error handling check
xxxx = stock('XXXX')
print(xxxx.getName() + ', ' + xxxx.symbol + ' dividend : $' + str(xxxx.getDividendYield()))

# create stock list
"""myList = stockList('Stock_Watchlist.txt')
print(myList.stocksList)
print(len(myList.stocksList))
myList.stocksList.stockListQuote()"""