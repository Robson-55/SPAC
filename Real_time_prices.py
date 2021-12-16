from tiingo import TiingoClient
import os
import pandas as pd
import openpyxl

#INTRODUCIR FECHA DE INICIO PARA PRECIOS HISTÓRICOS
#start_date="2021-11-03"

config = {}
# To reuse the same HTTP Session across API calls (and have better performance), include a session key.
config['session'] = True

# API key
config['api_key'] = "ccb1739190fa499e4415f1576d62f0464140d4bb"

#CSV
#fname = os.path.join("C:/Users/rober/Desktop/MIS COSAS/BUSINESS/TRADING/SPAC TRADING/Spacs-Knarias/Spacs Nombres.csv")
#x = pd.read_csv(fname)
#print(x)

# Initialize
client = TiingoClient(config)

#Get Historic Data
import requests
headers = {
    'Content-Type': 'application/json'
}




fname = os.path.join("C:/Users/rober/Desktop/MIS COSAS/BUSINESS/TRADING/SPAC TRADING/Spacs-Knarias/data.csv")
x = pd.read_csv(fname)
stocks=pd.read_csv(fname)
stock_newprices=[]
for index in stocks.values:
    stock_newprices.append(index)

prices = []

for name in stock_newprices:
    name=name[0]
    price = requests.get("https://api.tiingo.com/iex/?tickers="+name+"&token=ccb1739190fa499e4415f1576d62f0464140d4bb",headers=headers)
    print(price.json())
    prices.append(price.json())


d = {'Stock':stock_newprices,'Price':prices}
df = pd.DataFrame(d)
print(df)

df.to_excel("C:/Users/rober/Desktop/MIS COSAS/BUSINESS/TRADING/SPAC TRADING/Spacs-Knarias/Realtime_Prices.xlsx") #index? index=True en este caso
