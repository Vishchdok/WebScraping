import requests
from lxml import html

pageContent = requests.get('https://en.wikipedia.org/wiki/List_of_Olympic_medalists_in_judo')
tree = html.fromstring(pageContent.content)

goldWinners = tree.xpath('//*[@id="mw-content-text"]/table/tr/td[2]/a[1]/text()')

silverWinners = tree.xpath('//*[@id="mw-content-text"]/table/tr/td[3]/a[1]/text()')

bronzeWinners = tree.xpath('//*[@id="mw-content-text"]/table/tr/td[not(@rowspan=2)]/a[1]/text()')

medalWinners = goldWinners + silverWinners + bronzeWinners

medalTotals = {}
for name in medalWinners:
    if medalTotals.has_key(name):
        medalTotals[name] = medalTotals[name] + 1
    else:
        medalTotals[name] = 1

for result in sorted(medalTotals.items(), key=lambda x: x[1], reverse=True):
    print('%s:%s' % result)