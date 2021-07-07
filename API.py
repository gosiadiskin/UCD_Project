import requests
data=requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=Ebay&interval=5min&apikey=ES1AY6YOZU33WUST')
parsed_data=data.json()
print(parsed_data)
