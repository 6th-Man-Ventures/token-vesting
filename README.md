This repository includes the data, data processing pipeline, analysis notebook, and utility functions used in 6MVs piece on token unlocks. 

We encourage contributions from the token engineering community. 

### Running Analysis

To run analysis, simply run analysis.ipynb. 

### Adding New Data

To add new tokens to our dataset, just provide a dictionary of metadata in vesting_data.py. The following example of NYM exhibits the structure:

```
"nym": {
        "total_supply": 1000000000,
        "vesting": [
            {
                "group": "Backers",
                "allocation": 365000000,
                "cliff": 0,
                "cliff_amt": 0,
                "vesting_frequency": "quarterly",
                "start": "05-02-2022",
                "end": "05-02-2024"
            },
            {
                "group": "Team",
                "allocation": 200000000,
                "cliff": 0,
                "cliff_amt": 0,
                "vesting_frequency": "quarterly",
                "start": "05-02-2022",
                "end": "05-02-2024"
            }
        ]
    }
```

The above would correspond to the following vesting schedule:

| Group            | Allocation  | Cliff | Cliff Amount | Vesting Frequency | Start      | End        |
|------------------|-------------|-------|--------------|-------------------|------------|------------|
| Backers          | 100,000,000 | 0     | 0            | quarterly         | 05-02-2022 | 05-02-2024 |
| Team             | 100,000,000 | 0     | 0            | quarterly             | 05-02-2022 | 05-02-2024 |

Once added, run data_processing.ipynb before running analysis. Our tooling is built to use the CoinGecko API. The free version will work, but may throttle if ran too frequently. To use your API Key, change `KEY` in `api.py`. 

#### Additional Notes

* `cliff` is in days
* `cliff_amt` is the amount that vests on the day of the cliff. If the default behavior (fractional vest) is desired, this should be left as 0. 
* `vesting_frequency` can be "daily", "weekly", "monthly", or "annually"
* in our example, "nym" is the coingecko ID for NYM. The key for every token entry in dictionaries should be coingecko IDs. 


Please don't hesitate to reach out with suggestions or feedback. 


