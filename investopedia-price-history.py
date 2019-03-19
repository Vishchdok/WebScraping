from urllib.request import urlopen
from bs4 import BeautifulSoup

#https://www.investopedia.com/markets/api/partial/historical/?Symbol=AAPL&Type=%20Historical+Prices&Timeframe=Daily&StartDate=Nov+28%2C+2017&EndDate=Dec+05%2C+2017

stock = 'AAPL'
startDate = "Nov+28%2C+2017"
endDate = "Dec+05%2C+2017"

url = 'https://www.investopedia.com/markets/api/partial/historical/?Symbol{}&Type=%20Historical+Prices&Timeframe=Daily&StartDate={}&EndDate={}'.format(stock, startDate, endDate)
print(url)
html = urlopen(url)
bs = BeautifulSoup(html, 'html.parser')
