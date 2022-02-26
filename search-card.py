import requests
import urllib
import random
from bs4 import BeautifulSoup

class SearchCard:
    # This project created by Kc (https://github.com/scarletkc)
    # These codes are written by Kc (https://github.com/scarletkc)
    a = 7

    def __init__(self):         
        requestCard = input("请输入要查询的卡片信息包含的关键字: ") 
        #从(ourocg.cn)获得卡片数据初始化
        target = requests.get('https://www.ourocg.cn/search/'+urllib.parse.quote(requestCard)).text
        soup = BeautifulSoup(target, "html.parser")
        self.firstTarget = soup.find_all("script")[2].get_text()
        self.cardUrl = ""

    def GetFirstCardDetails(self):
        #得到匹配的第一张卡片的数据
        strBegin = self.firstTarget.find(r"https:\/\/www.ourocg.cn\/card\/")
        if strBegin >100 :
            theValue = ""
            for i in range(1,self.a):
                theValue = theValue + self.firstTarget[strBegin+30+i] 
                pass
            self.cardUrl = "https://www.ourocg.cn/card/"+theValue
        else:
            print("您请求的卡片不存在！")

    def GetTheCardDetails(self):
        #得到并输出这张卡片的具体信息
        self.GetFirstCardDetails()
        if self.cardUrl != "":
            target = requests.get(self.cardUrl).text
            soup = BeautifulSoup(target, "html.parser")
            try:
                cardDetails =  soup.find("article").get_text()
            except:
                self.a = random.choice([5,6,8,9])
                self.GetTheCardDetails()
            else:        
                outputCard = cardDetails.replace('\n', '').replace('\r', '')
                print(outputCard + "Please email to kc@fog.moe")  

#执行
useSearchCard = SearchCard()
useSearchCard.GetTheCardDetails()


