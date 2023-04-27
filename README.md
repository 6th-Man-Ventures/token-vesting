This repository includes the data, data processing pipeline, analysis notebook, and utility functions used in 6MVs piece on token unlocks. 

We encourage those interested to fork this repository and expand or refine our analysis. 

### Running Analysis

To run analysis, simply run analysis.ipynb. All of the utility functions can be found in the 'utils' folder. 

### Adding New Data

To add new tokens to our dataset, just provide a dictionary of metadata in vesting_data.py. The format is as follows:

```
"token-coingecko-id" : {
        "total_supply": 1_000_000,
        "vesting": pd.DataFrame({
            "group": ["Example Group I", "Example Group II"],
            "allocation": [500_000, 500_000],
            "cliff": [0, 90],
            "cliff_amt": [0, 0],
            "vesting_frequency": ["monthly", "daily"],
            "start": ["01-01-2022", "05-01-2022"],
            "end": ["01-01-2023, "05-01-2023"]
        })
    }
```

The above would correspond to the following vesting schedule:

| Group            | Allocation | Cliff | Cliff Amount | Vesting Frequency | Start      | End        |
|------------------|------------|-------|--------------|-------------------|------------|------------|
| Example Group I  | 500,000    | 0     | 0            | monthly           | 01-01-2022 | 01-01-2023 |
| Example Group II | 500,000    | 90    | 0            | daily             | 05-01-2022 | 05-01-2023 |

Once added, run data_processing.ipynb before running analysis. Our tooling is built to use the CoinGecko API. The free version will work, but may throttle if ran too frequently. To change this tooling, we recommend modifying api.py, specifically `get_historical_data()`. 

#### Additional Notes

* `cliff` is in days
* `cliff_amt` is the amount that vests on the day of the cliff. If the default behavior (fractional vest) is desired, this should be left as 0. 
* `vesting_frequency` can be "daily", "weekly", "monthly", or "annually"

Please don't hesitate to reach out with suggestions or feedback. 


