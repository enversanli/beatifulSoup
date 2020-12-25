import requests
from bs4 import BeautifulSoup

import Tulpar

class Scrape:

        def myfunc():
            print("Hello my name is TULPAR and I'm Python developer from Turkey")
        
        def getContent(pageUrl):
            page = requests.get(pageUrl)
            soup = BeautifulSoup(page.content)
            return soup
            
        def findIn(key, content, className):
            return content.find_all(key, {"class":className})


url = "https://enversanli.com"
scr = Scrape()
content = Scrape.getContent(url)

result = Scrape.findIn("ul", content, "tag")
print("-----------------")
print(result)
print("-----------------")
tulpar = Tulpar()

print("done")



