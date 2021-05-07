import time
from datetime import date,datetime
from bs4 import BeautifulSoup as bs 
import urllib.request
import csv

z = datetime.today()
day = z.strftime("%A")
hour = z.strftime("%H")
min = z.strftime("%M")
sec = z.strftime("%S")
print(sec)

print(z)


## This script will scrape the UK music charts every week it is updated. 
## We can then implement an improvement ranking how many times a song is at number one
# Chart will update every friday at 5
# Write chart into csv

source = urllib.request.urlopen("https://www.officialcharts.com/charts/singles-chart/").read()
page_html = bs(source,"lxml")
x = page_html.find_all("div", class_ = "track")



while True:
  z = datetime.today()
  day = z.strftime("%A")
  hour = z.strftime("%H")
  min = z.strftime("%M")
  sec = z.strftime("%S")
  j = 1
  if day == "Friday" and hour == "17" and min == "45" and sec == "30":
    for i in x:
      print(j,i.find("div",class_ = "artist").text.strip())
      print("Name-->",i.find("div",class_ = "title").text.strip())
      print("----------")
      j+=1
      
      
  else:
    pass
  
  
  
  
  
    

  

  
  


  


  
  

  
  
  
  
  
  
  
  





