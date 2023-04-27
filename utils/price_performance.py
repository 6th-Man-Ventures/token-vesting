from .api import get_historical_data
from datetime import datetime

def get_token_price_stats(first: list[str], second: list[str], tokens: dict, start_date: datetime, end_date: datetime) -> tuple[dict, dict]:
    """given two sets of token ids, calculate their price performance and volatility over a 
        time period.
    
    args:
        first (list[str]) : first set of token ids
        second (list[str]) : second set of token ids
        tokens (dict) : dictionary of all token data
        start_date (datetime) : start date for resultant data
        end_date (datetime) : end date for resultant data
    
    returns:
        first_results (dict) : dictionary of price performance and volatility for each token
                                in first set of tokens.
        second_results (dict) : dictionary of price performance and volatility for each token
                                in second set of tokens.
    """

    first_results = dict()
    second_results = dict()

    for token in first:
        t = tokens[token]
        prices = get_historical_data(token, start_date, end_date)['price']
        start, end = prices.iloc[0], prices.iloc[-1]
        variance = (prices.std() / prices.mean()) * 100
        change = (end - start) / start

        first_results[token] = {
            'variance': variance,
            'price_change': change
        }

    for token in second:
        t = tokens[token]
        prices = get_historical_data(token, start_date, end_date)['price']
        start, end = prices.iloc[0], prices.iloc[-1]
        variance = (prices.std() / prices.mean()) * 100
        change = (end - start) / start

        second_results[token] = {
            'variance': variance,
            'price_change': change
        }
    
    return first_results, second_results


def aggregrate_price_stats(first: list[str], second: list[str], macro: dict) -> dict:
    """ get averages of all tokens in a set once price performance metrics have been calculated

    args:
        first (list[str]): list of token ids in first set
        second (list[str]): list of token ids in second set
        macro (dict) : pre-processed baseline stats for macro tokens during time period
    
    returns:
        results (dict): full summary stats of each set of tokens
    """
    first_variances, first_changes = [], []
    second_variances, second_changes = [], []

    for token in first:
        change = first[token]["price_change"]
        variance = first[token]["variance"]

        first_variances.append(variance)
        first_changes.append(change)

    for token in second:
        change = second[token]["price_change"]
        variance = second[token]["variance"]

        second_variances.append(variance)
        second_changes.append(change)
    
    results = {
        "1": {
            "variance": sum(first_variances) / len(first_variances),
            "change": sum(first_changes) / len(first_changes)
        },
        "2": {
            "variance": sum(second_variances) / len(second_variances),
            "change": sum(second_changes) / len(second_changes)
        },
        "macro": macro
    }

    return results


def get_macro_stats(start: datetime, end:datetime) -> dict:
    """ Get ETH and BTC performance stats for given time period

    args:
        start (datetime) : beginning date
        end (datetime) : end date
    
    returns:
        results (dict) : summary stats of ETH and BTC
    """
    eth_prices = get_historical_data('ethereum', start, end)['price']
    btc_prices = get_historical_data('bitcoin', start, end)['price']

    eth_variance = (eth_prices.std() / eth_prices.mean()) * 100
    eth_start, eth_end = eth_prices.iloc[0], eth_prices.iloc[-1]
    eth_change = (eth_end - eth_start) / eth_start

    btc_variance = (btc_prices.std() / btc_prices.mean()) * 100
    btc_start, btc_end = btc_prices.iloc[0], btc_prices.iloc[-1]
    btc_change = (btc_end - btc_start) / btc_start

    results = {
        "eth_variance": eth_variance,
        "eth_change": eth_change,
        "btc_variance": btc_variance,
        "btc_change": btc_change
    }

    return results