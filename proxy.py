from os import write
from bs4.builder import HTML
import requests
import csv
from bs4 import BeautifulSoup as bs

with open('RotatingProxy.csv.txt','w',newline='') as f:
  write = csv.writer(f)
  write.writerow(['Ip','Port','Anon','Country'])
URL = 'https://free-proxy-list.net/'
r = requests.get(URL)
# print(r.status_code)

soup = bs(r.text,'html.parser')

table = soup.find_all('table') # finda all table within html and stores within a list
table = table[0] # Turns out the table element we want is the first item in the list, hence index [0]
tbody = table.find('tbody') # we get the tbody within table element
content = tbody.find_all('tr') # we then use the find_all method to get all tr elements within tbody in a list

for i in content: # we then iterate through each tr element which has its list stored to the variable content
  data = i.find_all('td') # through tr element iteration we find_all the td elements within which returns all the td elements in a list
  # We then index the td list to get nessecary data then use the .text to get the text within the elements
  ip = data[0].text 
  port = data[1].text
  country = data[3].text
  anon = data[4].text
  print(ip,port,country,anon)
  with open('RotatingProxy.csv.txt','a',newline='') as f: # We then open the csv file on each iteration and append data [ip,port,anon,country] to the file
    write = csv.writer(f)
    write.writerow([ip,port,anon,country])
    
  
  
  
















