import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://ap.louisvuitton.com/eng-sg/products/nice-nano-monogram-nvprod2320034v'

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15'}

def check_price():

     page = requests.get(URL, headers=headers)

     soup = BeautifulSoup(page.content, 'html.parser')

     # dispatchCountry = soup.find(id="dispatch-country")

     # title = soup.find(id="addToCartSubmit")

     price = soup.find(attrs={"class":"priceValuePurchaseLayer"}).get_text().strip()
     converted_price = "".join(num for num in price[4:] if num not in ("?", ";", ":", "!", ","))

     if(float(converted_price) < 1000):
          send_email()

     # print(converted_price)
     

def send_email():
     server = smtplib.SMTP('smtp.gmail.com', 587)
     server.ehlo()
     server.starttls()
     server.ehlo()

     server.login('answerforever.wang@gmail.com','qwawtbhkrydkwgcf')

     subject = 'Price down!'
     body = 'Check the site: https://ap.louisvuitton.com/eng-sg/products/nice-nano-monogram-nvprod2320034v'

     msg = f"Subject: {subject}\n\n{body}"

     server.sendmail(
          'answerforever.wang@gmail.com',
          'xiaofei.wang93@gmail.com',
          msg
     )

     print('email has been sent')

     server.quit()


while(True):
     check_price()
     time.sleep(3600)