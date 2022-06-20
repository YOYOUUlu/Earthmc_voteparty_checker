import time
import os
import time
import requests
from cgitb import html
from bs4 import BeautifulSoup

url1 = "https://minecraftservers.org/server/383495"
url2 = 'https://servers-minecraft.net/server-earthmc.1042/vote'
sec = input("刷新频率 the speed you want to see the message： ")
  
print("--------------------------------------------------")
print("welcome to Earthmc voteparty checker")
print("made by YOYOUU")
print("beautify by Jackyfeng")
print("--------------------------------------------------")
try:
  while True:
      '''预留数组'''
      arr = []
      arr2 = []
  
      '''爬取url1数据'''
      req = requests.get(url1) # 访问网页
      req.encoding = "utf-8" # 指定编码
      # 解析结果
      html = req.text	
      soup = BeautifulSoup(req.text, 'html.parser')
      # 查找全部元素
      votes=soup.find_all('span')
      # 数据清洗
      for vote in votes:
          dd = vote.text.strip()
          arr.append(dd)
    
      '''爬取url2数据'''
      req2=requests.get(url2) # 访问网页
      req2.encoding = "utf-8" # 指定编码
      # 解析结果
      html2 = req2.text	
      soup2 = BeautifulSoup(req2.text, 'html.parser')
      # 查找全部元素
      votes2=soup2.find_all('td')
      # 数据清洗
      for vote2 in votes2:
          bb = vote2.text.strip()
          arr2.append(bb)

      '''数据计算与返回'''
      vote1 = 0
      vote2 = int(arr2[5])
      vp = (vote1+vote2)%5000
      print("==============================================")
      print("vote1:   "+str(vote1))
      print("vote2:   "+str(vote2))
      print("total vote:   "+str(vote1 + vote2))
      print("wait to vote party:   "+str(5000 - vp))
      time.sleep(int(sec)) # 延迟sec秒 可自行修改
      i = os.system("cls")

except(ValueError):
  print('\033[5;31m!!!请输入数字 例如：10!!!\033[0m')
  print('\033[5;31m!!!input number like:10!!!\033[0m')