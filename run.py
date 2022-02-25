import requests
import urllib
from bs4 import BeautifulSoup
class SearchCard:
    # This project created by Kc (https://github.com/scarletkc)
    # These codes are written by Kc (https://github.com/scarletkc)
    def __init__(self): 
        requestCard = input("请输入要查询的卡包含的关键字") 
        target = requests.get('https://www.ourocg.cn/search/'+urllib.parse.quote(requestCard)).text
        soup = BeautifulSoup(target, "html.parser")
        self.firstTarget = soup.find_all("script")[2].get_text()
    def GetFirstCardDetails(self):
        #得到匹配的第一张卡的信息
        strBegin = self.firstTarget.find(r"https:\/\/www.ourocg.cn\/card\/")
        theValue = ""
        for i in [1,2,3,4,5,6]:
            theValue = theValue + self.firstTarget[strBegin+30+i] 
            pass
        self.cardUrl = "https://www.ourocg.cn/card/"+theValue
    def GetTheCardDetails(self):
        self.GetFirstCardDetails()
        target = requests.get(self.cardUrl).text
        soup = BeautifulSoup(target, "html.parser")
        cardDetails =  soup.find("article").get_text()
        outputCard = cardDetails.replace('\n', '').replace('\r', '')

useSearchCard = SearchCard()
useSearchCard.GetTheCardDetails()


