import pandas as pd

"""
To add data to our dataset, one only needs to add a new dictionary entry with metadata on the different
groups, allocations, dates, etc. Once run through the pipeline, this metadata becomes detailed price and supply data 
for each tokens vesting period.
"""

private_allocations = {
    "nym" : {
        "total_supply": 1_000_000_000,
        "vesting": pd.DataFrame({
            "group": ["Backers", "Team"],
            "allocation": [365_000_000, 200_000_000],
            "cliff": [0, 0],
            "cliff_amt": [0, 0],
            "vesting_frequency": ["quarterly", "quarterly"],
            "start": ["05-02-2022", "05-02-2022"],
            "end": ["05-02-2024", "05-02-2024"]
        })
    },
    "uniswap": {
        "total_supply": 1_000_000_000,
        "vesting": pd.DataFrame({
            "group": ["Team and Investors"],
            "allocation": [400_000_000],
            "cliff": [0],
            "cliff_amt": [0],
            "vesting_frequency": ["daily"],
            "start": ["09-01-2020"],
            "end": ["09-01-2024"]
        })
    },
    "euler": {
        "total_supply": 27_182_818,
        "vesting": pd.DataFrame({
            "group": ["Investors"],
            "allocation": [7_026_759],
            "cliff": [0],
            "cliff_amt": [0],
            "vesting_frequency": ["daily"],
            "start": ["12-31-2021"],
            "end": ["06-24-2023"]
        })
    },
    "project-galaxy": {
        "total_supply": 200_000_000,
        "vesting": pd.DataFrame({
            "group": ["Investors I", "Investors II"],
            "allocation": [21_260_000, 20_280_000],
            "cliff": [90, 0],
            "cliff_amt": [12, 12],
            "vesting_frequency": ["quarterly", "quarterly"],
            "start": ["05-09-2022", "05-09-2022"],
            "end": ["05-09-2025", "05-09-2025"]
        })
    },
    "bitdao": {
        "total_supply": 9_610_239_403,
        "vesting": pd.DataFrame({
            "group": ["Investors"],
            "allocation": [500_000_000],
            "cliff": [0],
            "cliff_amt": [0],
            "vesting_frequency": ["monthly"],
            "start": ["10-14-2021"],
            "end": ["09-14-2022"]
        })
    },
    "tornado-cash": {
        "total_supply": 3_000_000,
        "vesting": pd.DataFrame({
            "group": ["Team and Investors"],
            "allocation": [3_000_000],
            "cliff": [365],
            "cliff_amt": [0],
            "vesting_frequency": ["daily"],
            "start": ["12-12-2021"],
            "end": ["02-12-2023"]
        })
    },
    "forta": {
        "total_supply": 1_000_000_000,
        "vesting": pd.DataFrame({
            "group": ["Backers and Contributor"],
            "allocation": [545_329_994],
            "cliff": [365],
            "cliff_amt": [0],
            "vesting_frequency": ["daily"],
            "start": ["08-31-2022"],
            "end": ["08-30-2025"]
        })
    },
    "pooltogether": { 
        "total_supply": 10_000_000,
        "vesting": pd.DataFrame({
            "group": ["Team", "Investors"],
            "allocation": [1_244_000, 752_000],
            "cliff": [0, 0],
            "cliff_amt": [0, 0],
            "vesting_frequency": ["daily", "daily"],
            "start": ["02-16-2021", "02-16-2021"],
            "end": ["02-16-2022", "02-16-2022"]
        })
    },
    "merit-circle": {
        "total_supply": 899_737_985,
        "vesting": pd.DataFrame({
            "group": ["Team and Advisors", "Early Investors"],
            "allocation": [200_000_000, 140_625_000],
            "cliff": [0, 0],
            "cliff_amt": [0, 0],
            "vesting_frequency": ["daily", "daily"],
            "start": ["08-06-2022", "08-06-2022"],
            "end": ["08-30-2025", "08-30-2025"]
        })
    },
    "decentraland": {
        "total_supply": 2_193_211_827,
        "vesting": pd.DataFrame({
            "group": ["Team"],
            "allocation": [561_200_000],
            "cliff": [180],
            "cliff_amt": [0],
            "vesting_frequency": ["daily"],
            "start": ["08-17-2020"],
            "end": ["08-17-2024"]
        })
    },
    "looksrare": {
        "total_supply": 1_000_000_000,
        "vesting": pd.DataFrame({
            "group": ["Team Token"],
            "allocation": [100_000_000],
            "cliff": [180],
            "cliff_amt": [0],
            "vesting_frequency": ["quarterly"],
            "start": ["06-15-2022"],
            "end": ["08-30-2023"]
        })
    },
    "sweatcoin": {
        "total_supply": 22_249_455_607,
        "vesting": pd.DataFrame({
            "group": ["Private Round"],
            "allocation": [459_097_271],
            "cliff": [365],
            "cliff_amt": [0],
            "vesting_frequency": ["daily"],
            "start": ["09-12-2022"],
            "end": ["09-12-2026"]
        })
    },
    "curve-dao-token": {
        "total_supply": 3_003_030_299,
        "vesting": pd.DataFrame({
            "group": ["Team and Investors"],
            "allocation": [909_090_909],
            "cliff": [0],
            "cliff_amt": [0],
            "vesting_frequency": ["daily"],
            "start": ["08-13-2020"],
            "end": ["08-13-2024"]
        })
    },
    "stakewise": {
        "total_supply": 1_000_000_000,
        "vesting": pd.DataFrame({
            "group": ["Team", "Investors"],
            "allocation": [217_000_000, 251_500_000],
            "cliff": [180, 180],
            "cliff_amt": [0, 0],
            "vesting_frequency": ["daily", "daily"],
            "start": ["04-01-2021", "04-01-2021"],
            "end": ["03-31-2025", "03-31-2023"]
        })
    },
    "stepn": {
        "total_supply": 6_000_000_000,
        "vesting": pd.DataFrame({
            "group": ["Team", "Private Sale"],
            "allocation": [852_000_000, 978_000_000],
            "cliff": [0, 0],
            "cliff_amt": [0, 0],
            "vesting_frequency": ["daily", "daily"],
            "start": ["02-28-2023", "02-28-2023"],
            "end": ["02-28-2027", "02-28-2026"]
        })
    },
    "gelato": {
        "total_supply": 420_690_000,
        "vesting": pd.DataFrame({
            "group": ["Private Investors I", "Private Investors II"],
            "allocation": [44_172_450, 44_172_450],
            "cliff": [0, 0],
            "cliff_amt": [0, 0],
            "vesting_frequency": ["daily", "daily"],
            "start": ["09-13-2022", "02-27-2023"],
            "end": ["09-14-2022", "02-28-2023"]
        })
    },
    "lido-dao": {
        "total_supply": 1_000_000_000,
        "vesting": pd.DataFrame({
            "group": ["Team and Validators", "Investors"],
            "allocation": [400_400_000, 301_625_218],
            "cliff": [0, 0],
            "cliff_amt": [0, 0],
            "vesting_frequency": ["daily", "daily"],
            "start": ["12-17-2021", "12-17-2021"],
            "end": ["12-17-2022", "12-17-2022"]
        })
    },
    "filecoin": {
        "total_supply": 1_963_892_418,
        "vesting": pd.DataFrame({
            "group": ["Protocol Labs Team and Contributors", "Protocol Labs", "Filecoin Foundation"],
            "allocation": [90_000_000, 210_000_000, 100_000_000],
            "cliff": [0, 0, 0],
            "cliff_amt": [0, 0, 0],
            "vesting_frequency": ["daily", "daily", "daily"],
            "start": ["08-10-2017", "08-10-2017", "08-10-2017"],
            "end": ["08-10-2023", "08-10-2023", "08-10-2023"]
        })
    }

    

}

public_allocations = {
    "nym" : {
        "total_supply": 1_000_000_000,
        "vesting": pd.DataFrame({
            "group": ["Reserve & Community"],
            "allocation": [100_000_000],
            "cliff": [ 0],
            "cliff_amt": [0],
            "vesting_frequency": ["quarterly"],
            "start": ["04-13-2022"],
            "end": ["01-13-2024"]
        })
    },
    "project-galaxy": {
        "total_supply": 200_000_000,
        "vesting": pd.DataFrame({
            "group": ["Public Sale", "Treasury"],
            "allocation": [10_000_000, 40_000_000],
            "cliff": [0, 90],
            "cliff_amt": [0, 0],
            "vesting_frequency": ["weekly", "quarterly"],
            "start": [ "05-05-2022", "05-05-2022" ],
            "end": ["04-27-2023", "04-09-2027"]
        })
    },
    "bitdao": {
        "total_supply": 9_610_239_403,
        "vesting": pd.DataFrame({
            "group": ["Treasury"],
            "allocation": [3_000_000_000],
            "cliff": [90],
            "cliff_amt": [0],
            "vesting_frequency": ["monthly"],
            "start": ["07-14-2021"],
            "end": ["09-14-2022"]
        })
    },
    "pooltogether": { 
        "total_supply": 10_000_000,
        "vesting": pd.DataFrame({
            "group": ["Treasury"],
            "allocation": [5_754_000],
            "cliff": [0],
            "cliff_amt": [0],
            "vesting_frequency": ["daily"],
            "start": ["02-16-2021"],
            "end": ["02-16-2023"]
        })
    },
    "merit-circle": {
        "total_supply": 899_737_985,
        "vesting": pd.DataFrame({
            "group": ["Public Sale"],
            "allocation": [301_875_000],
            "cliff": [0],
            "cliff_amt": [0],
            "vesting_frequency": ["daily"],
            "start": ["11-04-2021"],
            "end": ["11-04-2024"]
        })
    },

    "sweatcoin": {
        "total_supply": 22_249_455_607,
        "vesting": pd.DataFrame({
            "group": ["Community"],
            "allocation": [5_156_802_051],
            "cliff": [0],
            "cliff_amt": [10],
            "vesting_frequency": ["daily"],
            "start": ["09-12-2022"],
            "end": ["09-12-2024"]
        })
    },
    "stakewise": {
        "total_supply": 1_000_000_000,
        "vesting": pd.DataFrame({
            "group": ["Community"],
            "allocation": [ 510_000_000],
            "cliff": [0],
            "cliff_amt": [0],
            "vesting_frequency": ["daily"],
            "start": ["04-01-2021"],
            "end": ["03-31-2025"]
        })
    },
    "aptos": {
        "total_supply": 1_000_000_000,
        "vesting": pd.DataFrame({
            "group": ["Community"],
            "allocation": [385_217_360],
            "cliff": [0],
            "cliff_amt": [0],
            "vesting_frequency": ["monthly"],
            "start": ["11-11-2022"],
            "end": ["11-11-2032"]
        })
    }
}
