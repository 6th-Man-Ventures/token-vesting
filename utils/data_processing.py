import pandas as pd

"""
tools to help process input data into usable dataframe format.
"""

def convert_vesting_data_to_df(tokens: dict) -> dict:
    """convert list of vesting events into dataframe for further analysis

    args:
        tokens (dict): list of tokens to be converted
    
    returns:
        result (dict): converted list
    """
    result = dict()

    for token in tokens:
        t = tokens[token]

        new_token = {
            "total_supply": t["total_supply"],
            "vesting": convert_vest(t["vesting"])
        }

        result[token] = new_token
    
    return result


def convert_vest(data: list) -> pd.DataFrame:
    """loops through events and aggregates into dataframe with columns for each datapoint

    args:
        data (dict): vesting events list
    
    returns:
        result (pd.DataFrame): converted dataframe
    """
    depth = len(data)

    group = []
    allocation = []
    cliff = []
    cliff_amt = []
    vesting_frequency = []
    start = []
    end =[]


    for i in range(depth):
        event = data[i]

        group.append(event["group"])
        allocation.append(event["allocation"])
        cliff.append(event["cliff"])
        cliff_amt.append(event["cliff_amt"])
        vesting_frequency.append(event["vesting_frequency"])
        start.append(event["start"])
        end.append(event["end"])

    result =  pd.DataFrame({
        "group": group,
        "allocation": allocation,
        "cliff": cliff,
        "cliff_amt": cliff_amt,
        "vesting_frequency": vesting_frequency,
        "start": start,
        "end": end
    })

    return result


