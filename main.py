import requests
import lxml
from bs4 import BeautifulSoup
import smtplib
MY_EMAIL = MY_EMAIL
PASSWORD = PASSWORD
YOUR_EMAIL = YOUR_EMAIL

url = 'https://www.amazon.com/dp/B075CYMYK6'
header = {
    'Accept-Language': 'en-US',
    'User-Agent': 'Chrome/117.0.0.0',
}
response = requests.get(url=url, headers=header)
webpage = response.content
soup = BeautifulSoup(webpage, 'lxml')
price_tag = soup.find(class_="a-offscreen").get_text()
price = float(price_tag.split("$")[1])
if price < 100:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL, to_addrs=YOUR_EMAIL,
            msg=f"Subject:Price dropped\n\nPrice dropped below $100. Now the price is {price}. Buy Now!!"
        )
