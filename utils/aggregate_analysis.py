import pandas as pd
import statistics

"""
functions to calculate the average and median price behavior around all unlocks in the dataset.
"""

def norm_windows(windows: list[list[float]], w: int) -> list[list[float]]:
    """normalizes windows of price data to percent difference from day of unlock (middle element of window).

    args: 
        windows (list[list[float]]) : list of intervals of price data, with unlock day being the middle day.
        w (int) : length of window

    returns:
        normed (list[list[float]]) : normalized price windows
    """
    normed = []
    for window in windows:
        norm = pd.Series(index=range(-w, w + 1), dtype='float64')
        for i in range(-w, w + 1):
            norm[i] = ((window[i] - window[0]) / window[0]) * 100

        normed.append(norm)
        
    return normed

def get_stat_lines(windows: list[list[float]], w: int) -> tuple[list[float], list[float]]:
    """calculates average and median of all windows

    args: 
        windows (list[list[float]]) : normalized windows of price data
        w (int) : length of window
    
    returns:
        avg_line (list[float]) : average of all windows
        median_line (list[float]) : median of all windows
    """
    indices = dict()

    for window in windows:
        for i in range(-w, w + 1):
            if i in indices:
                indices[i].append(window[i])
            else:
                indices[i] = [window[i]]
    
    avg_line = pd.Series(index=range(-w, w + 1), dtype='float64')
    median_line = pd.Series(index=range(-w, w + 1), dtype='float64')

    for i in range(-w, w + 1):
        avg = sum(indices[i]) / len(indices[i])
        median = statistics.median(indices[i])
        avg_line[i] = avg
        median_line[i] = median

    return avg_line, median_line

