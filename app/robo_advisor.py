print("To do: make a web request for some stock market data")


# https://www.alphavantage.co/documentation/#dailyadj

# setup
import os
from dotenv import load_dotenv
import requests



# read env variables
load_dotenv() # go get env vars from the .env file
ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")

# make a request
symbol = "MSFT" # ask for user input

request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={ALPHAVANTAGE_API_KEY}"

print("TEST TEST")


response = requests.get(request_url)
print(type(response))
print(response.text)
