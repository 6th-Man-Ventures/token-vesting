"""
functions to generate price and supply metrics using filtering, outlier removal, and different time windows.

once tokens dictionary includes daily data tables (see daily_charts.py), that dictionary can be fed through 
process_price_supply_lists(). No other function here needs to be called directly.

"""

def process_price_supply_lists(tokens: dict, window: int, supply_threshold: tuple[float, float], adj_beta=False) -> tuple[list[float], list[float]]:
    """method to create aggregate list of all unlock events (supply change, price change) from a given
    dictionary of tokens. Removes overlapping events, filtering out unlocks with high frequency.

    args:
        tokens (dict) : dictionary of token daily table data 
        window (int) : number of days after unlock to calculate change in price for. for
                        days before, negative windows can be used.
        
        supply_threshold 
        (Tuple[float, float]) : threshold of supply change percentages to include. used to exclude 
                                outliers.
    returns:
        result_p (List[float]) : list of price change percentages corresponding to unlock events.
        result_s (List[float]) : list of supply changes percentages corresponding to unlock events.

    """

    # unpack threshold
    lower_s, upper_s = supply_threshold

    result_p, result_s = [], []
    for token in tokens:
        
        delta_supply= tokens[token]["p_change_supply"]
        circulating_supply = tokens[token]["circulating_supply"]
        prices = tokens[token]["price"]
        delta_price = tokens[token]["p_change_price"]
        unlock = tokens[token]["Daily Vest"]
        macro = tokens[token]["eth"]

        if adj_beta:
            beta = tokens[token]["beta"]
        else: 
            beta = None

        for i, (u, s) in enumerate(zip(unlock, delta_supply)):
            rules = [s < upper_s, s > lower_s, circulating_supply[i] > 0, 
                    u > 0]

            if all(rules):
                # retrieve price change percent for given window
                metric = get_window_metric(window, prices, delta_price, i, beta, macro)
                if metric:
                    result_p.append(metric)
                    result_s.append(s)
    
    print(f"prices: {len(result_p)}, supplies:  {len(result_s)}")
    return result_p, result_s

def get_window_metric(window: int, prices: list[float], d_price: list[float], i: int, beta: list[float], macro: list[float]) -> float:
    """given a day's price, calculates change in price during window surrounding it.

    args:
        window (int) : number of days after each day to calculate change for.
        prices (List[float]) : raw price data
        d_price: (List[float]) : percent change version of prices list.
        i (int) : index in list to calculate window for
    
    returns:

        change (float) : percent change in price during given window
    """
    if window == 0:
        return d_price[i]

    if i + window in range(len(prices)):
        comparison_index = window + i
        day_of = prices[i]
        before = prices[comparison_index]
        

        if comparison_index == i:
            change = d_price[i]
        else:
            if beta is not None:
                window_beta = beta[i]
                macro_change = (macro[comparison_index] - macro[i]) / macro[i] * 100
                actual_change = ((before - day_of) / day_of) * 100

                change = actual_change - (macro_change * window_beta)
            
            else:
                change = ((before - day_of) / day_of) * 100

        return change

    else:
        return None




def remove_outliers(data):
    
    q1 = data.quantile(.25)
    q3 = data.quantile(.75)
    IQR = q3 - q1
    pruned = data[~((data < (q1 - 1.5 * IQR)) | (data > (q3 + 1.5 * IQR)))]
    pruned = pruned.dropna().reset_index()

    return pruned

