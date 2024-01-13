# Amazon Price Tracker

This Python script allows you to track the price of a product on Amazon and receive email notifications when the price drops below a certain threshold. Simply set your target buy price and your Gmail credentials as environment variables, and the script will periodically check the product's price on Amazon and send you an email alert when the price meets your criteria.

## How it Works
1. The script sends a request to the Amazon product page.
2. It parses the HTML content using BeautifulSoup to extract the product's title and price.
3. The extracted price is compared to the target buy price you've set.
4. If the current price is lower than your desired price, the script sends an email notification to your Gmail address.

<img src="https://github.com/amansinghgill/Amazon-Price-Tracker/assets/90486946/d75d99f0-6498-4130-b094-aa2bc4efb3f8" alt="UI" width="800px" style="margin: 0 auto; display: block;">

## Setup Instructions
1. Clone this repository to your local machine.
2. Set your Gmail email and password as environment variables:
3. Modify the `url` variable in the script to point to the Amazon product you want to track.
4. Set your desired `BUY_PRICE` in the script to specify the price threshold for notifications.
5. Run the script using `python amazon_price_tracker.py`.

Now you will receive email alerts whenever the product's price drops below your specified threshold.

**Note:** Make sure to enable "Less secure apps" in your Gmail settings and allow access to your Google account to use this script.
