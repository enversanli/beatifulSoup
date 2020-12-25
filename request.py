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
            
        def findbyClass(key, content, className):
            return content.find_all(key, {"class":className})
        
        def findById(key, content, id):
            return content.find_all(key, {"id":id})

url = "https://enversanli.com"
scr = Scrape()
content = Scrape.getContent(url)
getWithId = Scrape.findById("ul", content, "demo1")
result = Scrape.findbyClass("ul", content, "tag")
print("-----------------")
print(result)
print("-----------------")

print(getWithId)

tulpar = Tulpar()

print("done")



