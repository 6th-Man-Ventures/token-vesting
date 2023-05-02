import logging
import pandas as pd
from monthdelta import monthdelta
from datetime import datetime, timedelta
from typing import List

"""
Utility functions to help process descriptive vest schedule data into daily charts with unlocks by group.

Given an example dictionary as specified in the README, we run the following:

        example["start"] = df_column_to_datetime(example['start'])
        example["end"] = df_column_to_datetime(example['end'])
        vest_schedule = create_empty_vest_schedule(example, 'group', 'start', 'end')
        vest_schedule = populate_vest_schedule(data, vest_schedule)
    
Where vest_schedule is a daily table DataFrame for the period of vesting. 
"""

def df_column_to_datetime(col: pd.DataFrame, date_type: str = None, date_only: bool = False) -> pd.DataFrame:
    """Converts single dataframe column to type datetime.
    
    Args:
        col: REQUIRED. Dataframe column.
        date_type (STRING): OPTIONAL. Valid inputs are 'day_first' or 'year_first'
        date_only (BOOL): OPTIONAL. If true, removes times from dateTime object.
    
    Returns:
        col: DateTime object. 
    """
    

    if date_type == None:
        col = pd.to_datetime(col)
    elif date_type == 'day_first':
        col = pd.to_datetime(col, dayfirst=True)
    elif date_type == 'year_first':
        col = pd.to_datetime(col, yearfirst=True)
    else:
        logging.error(f'{date_type} is invalid input. Did not convert to type datetime', exc_info=True)

    if date_only == True:
        col = col.dt.normalize()

    
    return col


def create_empty_vest_schedule(df: pd.DataFrame, vest_recipients_col_name: str, vest_start_col_name: str, vest_end_col_name: str, fill: str ='zeros') -> pd.DataFrame:
    """ From list of vest events Create dataframe of date index and columns Allocation groups
    
    From a dataFrame consisting of vest events, creates a DF indexed on all dates between the first and last vest event.
    Column names are derived from all token recipient groups.
    
    Args:
        df (pd.DataFrame): REQUIRED. DataFrame of all vest events.
        vest_recipients_col_name (str): REQUIRED. Column name of token vest recipient groups.
        vest_start_col_name (str): REQUIRED. Column name of vest start date data
        vest_end_col_name (str): REQUIRED. Column name of vest end data data
        fill (str): OPTIONAL. What data dataframe should be filled with. STRING. Values = ['zeros','empty']. Default is Zeros. 
    
    Returns:
        df (pd.DataFrame): Dataframe of size date_index x unique recipient groups.
    """
    # Build full date index
    min_date = min(df[vest_start_col_name])
    max_date = max(df[vest_end_col_name])
    date_list = pd.date_range(start=min_date, end=max_date)
    
    # Build column names based on token recipient groups
    column_names = df[vest_recipients_col_name].unique()

    if fill == 'zeros':
        vest_table = pd.DataFrame(0,index=date_list, columns=column_names)
    elif fill == 'empty':
        vest_table = pd.DataFrame(0,index=date_list, columns=column_names).empty #TODO check this
    else:
        logging.error(f'{fill} is invalid input. Did not create vest table', exc_info=True)
    
    vest_table.index.name = 'Date'
    
    return vest_table

def populate_vest_schedule(df: pd.DataFrame, vest_schedule: pd.DataFrame, sum: bool = True) -> pd.DataFrame:
    """Iterates over vest events in df to populate vest_schedule 
    
    Args:
        df (pd.DataFrame): Dataframe of individual vest events
        vest_schedule (pd.DataFrame): DF of zeros, index being total dates between earlier and last vest and columns vest recipients
        sum (BOOL): OPTIONAL. If False, does not sum vests across each row
    
    Returns:
        vest_schedule: populated vest schedule.
    """

    date_list = vest_schedule.index

    # create booleans indicating cliff or frequency data
    cliff_exists = 'cliff' in df.columns
    freq_exists = 'vesting_frequency' in df.columns
    cliff_amt_exists = 'cliff_amt' in df.columns

    # Iterate over df of individual vest events
    for row in df.itertuples(index=False):

        # set optional cliff and frequency vars
        cliff = row.cliff if cliff_exists else 0
        frequency = row.vesting_frequency if freq_exists else 'daily'
        cliff_amt = row.cliff_amt if cliff_amt_exists else 0
        
        date_index = pd.date_range(row.start, row.end, inclusive='left')
        allocation_schedule = build_token_vest(row.start, row.end, row.allocation, frequency, cliff_amt, cliff)
        
        # Build individual vest df & expand to full range
        specific_vest_df = pd.DataFrame(allocation_schedule, index=date_index, columns=[row.group])
        specific_vest_df = specific_vest_df.reindex(date_list,fill_value=0)

        # Add vest df to overall vest table
        vest_schedule[row.group] = vest_schedule[row.group] + specific_vest_df[row.group]
    
    if sum == True:
        vest_schedule['Daily Vest'] = vest_schedule.sum(axis=1)
    
    return vest_schedule

def build_token_vest(start_date: datetime, end_date: datetime, allocation: float, frequency="daily", cliff_amt=0, cliff=0):
    """Distribute vest allocation equally between start and end dates. 

    Args:
        start_date(datetime): First date of vest
        end_date(datetime): Last date of vest. Inclusive "left" by default.
                            If single vest, set end date equal to start date. 
        allocation: Number of tokens
        frequency : one of ['daily', 'weekly', 'monthly', 'annually']
        cliff : cliff, in days
    
    Returns:
        allocation_list: List of dates
    """
    if start_date == end_date:
        allocation_list = allocation
    else:
        allocation_list = get_allocation_list(frequency, allocation, start_date, end_date, cliff, cliff_amt)

    return allocation_list    


def get_allocation_list(frequency: str, allocation: float, start: datetime, end: datetime, cliff: float, cliff_amt: float, chart=False) -> List[float]:
    """Create allocation list, handling frequencies and cliffs
    
    Args: 
        frequency (str) : how often vest occurs
        allocation (float) : tokens allocated 
        start (DateTime) : start date
        end (DateTime) : end date
        cliff (float) : durationg in days of cliff
    
    Returns:
        allocation_list List[float]
    """
    if start == end:
        return [allocation]

    # create dictionaries of time deltas
    deltas = {
        "daily" : timedelta(days=1),
        "weekly": timedelta(weeks=1),
        "monthly": monthdelta(1),
        "quarterly": monthdelta(3),
        "annually": monthdelta(12)
    }
    
    vest_length = (end - start).days
    cliff_amt = allocation * (cliff_amt / 100) 
    

    # adjust real start date for cliff
    start = start + timedelta(days=cliff)

    TGE_adjustment = 0
    if cliff_amt and cliff == 0:
        TGE_adjustment = 1
    
    # loop through vest period and mark days that vest
    vest_dates =[]
    current_date = start
    while current_date <= end:
        vest_dates.append(current_date)
        current_date += deltas[frequency]

    # create allocation list, filling when dates in vest_dates
    cliff_list, cliff_amt = get_cliff_list(start, cliff, allocation, chart, vest_length, len(vest_dates), cliff_amt)
    vest_amount = (allocation - cliff_amt) / (len(vest_dates) - 1) if len(vest_dates) > 1 else 0
    
    # get monthly list with no zeros for preview chart, else include zeros
    if chart:
        allocation_list = [vest_amount for i in range(vest_length-cliff - TGE_adjustment) if (start + timedelta(days=i)) in vest_dates]
    else:
        allocation_list = [vest_amount if (start + timedelta(days=i)) in vest_dates else 0 for i in range(vest_length-cliff - TGE_adjustment)]

    # add cliff days
    allocation_list = cliff_list + allocation_list

    return allocation_list

def get_cliff_list(start: datetime, cliff, allocation, chart, vest_length, vest_dates_len, cliff_amt):
    """Create separate lists to handle cliffs

    Args: 
    start (datetime) : date of cliff
    cliff (float) : length of cliff in days
    allocation (float) : amount allocated for group 
    vest_length (float) : durationg in days of cliff
    vest_dates_len (float) : durationg in days of cliff
    cliff_amt (float) : amount unlocked at cliff. 0 if default even split.
    """
    cliff_list = []
    
    if (cliff or cliff_amt) and vest_length:
        cliff_amt = (cliff / vest_length) * allocation if cliff_amt == 0 else cliff_amt
        if chart:
            cliff_end = start + timedelta(days=cliff)
            months = (cliff_end.year - start.year) * 12 + cliff_end.month - start.month
            cliff_list = [0 for i in range(months)] + [cliff_amt]
        else:
            cliff_list = [0 for i in range(cliff - 1)] + [cliff_amt]

    return cliff_list, cliff_amt


def total_vested_to_date(df, col_names:list[str] = None) -> pd.DataFrame:
    '''Calculates cumulative vest for selection and returns df
    
    Args: 
        df (pd.DataFrame): REQUIRED.  
        col_names (list[str]): OPTIONAL. Specify column names.
    
    Returns:
        col (pd.DataFrame): Column of cumulative sum.
    '''
    if col_names == None:
        col_names = df.columns
    
    sum_df = df[col_names].sum(axis=1)

    daily_sum_df = sum_df.cumsum()
    daily_sum_df = daily_sum_df.to_frame()
    
    return daily_sum_df

