from bs4 import BeautifulSoup as bs
import urllib.request
import smtplib
import time

source = urllib.request.urlopen("https://www.gamestop.ie/PlayStation%205/Games/72504/playstation-5-console").read()

x = bs(source,"lxml")
# print(x.prettify())
myUserAgent={"header": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"}


print("Product Info")
print("---------------")
for i in x.find_all("div","prodTitle"):
  b = i.h1.text.strip()
  print("Product Name:",b)


for i in x.find_all("div","pricetext"):
  a = i.span.next_sibling.previous_sibling.text
  a = i.span.next_sibling.previous_sibling.text[1:8]
  a = float(a)
  print("Price:",a)



def checkPrice():
  if a<499.99:
    decrease_email()
  elif a>499.99:
    increase_price() 
  else:
    stayed_The_Same()
  
  
def decrease_email():
  sender_email = "Jamaa061.309@gmail.com"
  rec_email = "jamaa019.309@gmail.com"
  password = "ronaldo81"
  message = "Hey, the product you wanted has decreased in price\nLink: https://www.gamestop.ie/PlayStation%205/Games/72504/playstation-5-console"
  print("Done")

  ## initialise server

  server = smtplib.SMTP("smtp.gmail.com",587)
  server.starttls()
  server.login(sender_email,password)
  server.sendmail(sender_email,rec_email, message)
  print("Success!")
 
def increase_price():
  sender_email = "Jamaa061.309@gmail.com"
  rec_email = "jamaa019.309@gmail.com"
  password = "ronaldo81"
  message = "Hey, the product you wanted has unfortunately increased in price\nLink: https://www.gamestop.ie/PlayStation%205/Games/72504/playstation-5-console"

  ## initialise server

  server = smtplib.SMTP("smtp.gmail.com",587)
  server.starttls()
  server.login(sender_email,password)
  server.sendmail(sender_email,rec_email, message)
  print("Success!")
  
def stayed_The_Same():
  sender_email = "Jamaa061.309@gmail.com"
  rec_email = "jamaa061.309@gmail.com"
  password = "ronaldo81"
  message = "Hey, the product you wanted has STAYED the same in price, here is the link to check it out\nLink: https://www.gamestop.ie/PlayStation%205/Games/72504/playstation-5-console"
  print("Done")

  ## initialise server

  server = smtplib.SMTP("smtp.gmail.com",587)
  server.starttls()
  server.login(sender_email,password)
  server.sendmail(sender_email,sender_email, message)
  print("Success!")
    
def main():
  while True:
    checkPrice()
    time.sleep(24*60*60)
    print("Running")
    
  
main()





    


      
    

    
    

    
    

    
    
    
    
    

    




























  





  

  
  
  
  
  
  
  


  















