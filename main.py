from bs4 import BeautifulSoup
import requests
import smtplib
from dotenv import load_dotenv
import os


def send_email(product_name  , price):
    load_dotenv()
    with smtplib.SMTP(os.getenv("SMTP_SERVER"),587) as connection:
        connection.starttls()
        connection.login(user=os.getenv("EMAIL_ADDRESS"),password=os.getenv("EMAIL_PASSWORD"))
        connection.sendmail(
            from_addr=os.getenv("EMAIL_ADDRESS"),
            to_addrs=os.getenv("RECIPIENT_EMAIL"),
            msg=f"Subject:Price Alert for {product_name}\n\nThe price of {product_name} is now {price} EUR."
        )

 

#get the price of a product from the amazon product page
def send_request():
    headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36",
        "Accept-Language":"en-US,en;q=0.9"
    } 
    response=requests.get("https://www.amazon.de/EK251QG-Monitor-Screen-120Hz-AdaptiveSync/dp/B0BDCVNFBY/ref=sr_1_2_sspa?crid=V7C5QCWND2J4&dib=eyJ2IjoiMSJ9.b7h09nZXp8JONIrq15Z2NPnArIc209BG2zKeYTn7SLdC7tkfu2sHr8Bjh3zv4jVbNN8To7pzyTSKYFjluttvcXTMdZYO939Oebis4fBzYnB6OGR4km6V7FhqnArJSN9FudeMhnGdyVpzl2qnd0foERh0BcvVbR-Fc8NyX5AEobsdUUlnq6LpoLpquKqASxenzzcsQ3_FuQcDdjDjCX-P5BIMltBQ7Sp5OqGEunA70us.iXc9QqNNBAXz0xQW8qCfKw0dQJyvcxyhZzi3mdiBlGM&dib_tag=se&keywords=monitor&qid=1762949755&sprefix=monit%2Caps%2C105&sr=8-2-spons&aref=u4BuskArve&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1", headers=headers)
    soup=BeautifulSoup(response.content,"html.parser")
   
    #get the price of the product from the html content
    price_whole=soup.find("span",{"class":"a-price-whole"}).get_text().split(",")[0]
    price_fraction=soup.find("span",{"class":"a-price-fraction"}).get_text()
    price=float(price_whole) + float(price_fraction)*0.01
    print(f"Price: {price} EUR")
    if(price<=70.99):
        product_name=soup.find("span",{"id":"productTitle"}).get_text().strip()
        send_email(product_name,price)
        print("Email sent!")
    else:
        print("Price is too high, no email sent.")
send_request()