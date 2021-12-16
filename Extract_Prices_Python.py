from tiingo import TiingoClient
import os
import pandas as pd
import openpyxl

#INTRODUCIR FECHA DE INICIO PARA PRECIOS HISTÓRICOS
start_date="2021-10-01"

config = {}
# To reuse the same HTTP Session across API calls (and have better performance), include a session key.
config['session'] = True

# API key
config['api_key'] = "ccb1739190fa499e4415f1576d62f0464140d4bb"

#CSV
#XLSX
fname = os.path.join("C:/Users/rober/Desktop/MIS COSAS/BUSINESS/TRADING/SPAC TRADING/Spacs-Knarias/data.csv")
x = pd.read_csv(fname)
#print(x)

# Initialize
client = TiingoClient(config)

#Get Historic Data
import requests
headers = {
    'Content-Type': 'application/json'
}

stocks=pd.read_csv(fname)
stock_historic_names=[]

for index in stocks.values:
    stock_historic_names.append(index)

prices=[]

for name in stock_historic_names:
    name=name[0]
    price = requests.get("https://api.tiingo.com/tiingo/daily/"+name+"/prices?startDate="+start_date+"&token=16776197cfb8a3666d11ae8a747f070c9ec665b6", headers=headers)
    prices.append(price.json())
    print(price.json())
    print(type(price))
print("-------------------------PRICES--------------------------------")
print(prices)
print("-------------------------NAMES-PRICES--------------------------------")
d = {'Stock':stock_historic_names,'Price':prices}
df = pd.DataFrame(d)
print(df)
#print("-------------------------PRICES-EXTRACT_DICT--------------------------------")
#df2=pd.DataFrame.from_dict(prices)
#print(df2)
#print("---------------------------------------------------------")
#print("D2")
#d2={'Stock':stock_historic_names,'Price':prices}
#print(d2)
df.to_excel("C:/Users/rober/Desktop/MIS COSAS/BUSINESS/TRADING/SPAC TRADING/Spacs-Knarias/Historic_Prices.xlsx") #index? index=True en este caso
