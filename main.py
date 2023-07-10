import requests

money = "KRW-BTC"
url = "https://api.upbit.com/v1/market/all"
params = {
    "isDetail" : False
    }

repo = requests.get(url)
data = repo.json()

krw_coin = []
for coin in data:
    ticker = coin["market"]
    if ticker.startswith("KRW"):
        krw_coin.append(coin)
print(krw_coin)