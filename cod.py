import requests
from bs4 import BeautifulSoup


session = requests.Session()
hdr = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
url = "https://cod-esports.gamepedia.com/CWL/2019_Season/Pro_League/Team_Rosters"
req = session.get(url, headers=hdr)
bsObj = BeautifulSoup(req.text, 'html.parser')
a_list = []
game = bsObj.find('table',{'class':'prettytable'})
for play in game.find_all('tbody'):
    print(play.get('a'))
#for a in a.list:
    #print(a.get('href'))
    #time.sleep(3)
