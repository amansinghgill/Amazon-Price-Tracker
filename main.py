import requests
import lxml
import smtplib
import os
from bs4 import BeautifulSoup

# Use environment variables for email and password
YOUR_EMAIL = os.getenv('MY_EMAIL')
YOUR_PASSWORD = os.getenv('MY_PASSWORD')

# URL of the product
url = "https://www.amazon.ca/dp/B07D13QGXM?ref_=cm_sw_r_cp_ud_dp_P2J0ESVY922Y956ZMKG9"
# Request headers
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

# Sending a request to the URL
response = requests.get(url, headers=header)

# Parsing the HTML content
soup = BeautifulSoup(response.content, "lxml")
# print(soup.prettify())

# Extracting the price
price = soup.find(class_="a-price-whole").get_text()
price_without_currency = price.split(".")[0]
price_as_float = float(price_without_currency)
# print(price_as_float)

# Extracting the product title
title = soup.find(id="productTitle").get_text().strip()
# print(title)

# Set a target buy price
BUY_PRICE = 40.00

# Check if the current price is less than the buy price
if price_as_float < BUY_PRICE:
    message = f"{title} is now ${price}"

    # Sending an email if the condition is met
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()  # Secure the connection
        result = connection.login(YOUR_EMAIL, YOUR_PASSWORD)  # Login
        # Send the email
        connection.sendmail(
            from_addr=YOUR_EMAIL,
            to_addrs=YOUR_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}"
        )