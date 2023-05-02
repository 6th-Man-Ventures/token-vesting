from datetime import datetime, timezone
import requests
import os
import pandas as pd

"""
functions to retrieve and process data from the CoinGecko API. 
"""

KEY = "CG-RVYAov5kke3A1guMmeG7nfYB"


def to_unix(date: datetime) -> int:
    """turn datetime object into unix"""
    
    return date.replace(tzinfo=timezone.utc).timestamp()

def to_date(unix: int) -> datetime:
    """turn unix timestamp into datetime object"""
    
    unix = unix / 10
    date = datetime.fromtimestamp(unix).strftime('%Y-%m-%d')
    return date

def get_historical_data(id: str, start: datetime, end: datetime) -> pd.DataFrame:
    """ method to retrieve historical price, supply, and eth price data for a given token
    
    args: 
        id (str) : CoinGecko id of token
        start (datetime) : start date for data
        end (datetime) : end date for data
    
    returns:
        DataFrame of prices for token, circulating supply, and eth prices
    
    """

    if KEY == None: 
        raise(Exception("No API Key Specified."))
    
    start, end = to_unix(start), to_unix(end)
    res = requests.get(f"https://pro-api.coingecko.com/api/v3/coins/{id}/market_chart/range?vs_currency=usd&from={start}&to={end}&x_cg_pro_api_key={KEY}")
    eth_res = requests.get(f"https://pro-api.coingecko.com/api/v3/coins/ethereum/market_chart/range?vs_currency=usd&from={start}&to={end}&x_cg_pro_api_key={KEY}")   
    
    if res.status_code == 404:
        return pd.DataFrame()
    
    prices = res.json()["prices"]
    mktcaps = res.json()["market_caps"]
    eth_prices = eth_res.json()["prices"]
    
    # turn json objects into columns for dataframe
    date_col, price_col, cap_col, eth_col = [], [], [], []
    for price, cap, eth in zip(prices, mktcaps, eth_prices):
        date = price[0]
        date_obj = datetime.fromtimestamp(date/1000.0).date()
        date_col.append(date_obj)
        cap_col.append(cap[1] / price[1])
        price_col.append(price[1])
        eth_col.append(eth[1])

    data_dict = {
        "date" : date_col,
        "price" : price_col,
        'circulating_supply': cap_col,
        'eth': eth_col
        
    }

    df = pd.DataFrame(data_dict)
    df = df.set_index('date')
    
    return df
