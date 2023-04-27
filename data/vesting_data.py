import pandas as pd

"""
To add data to our dataset, one only needs to add a new dictionary entry with metadata on the different
groups, allocations, dates, etc. Once run through the pipeline, this metadata becomes detailed price and supply data 
for each tokens vesting period.
"""

private_allocations = {
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
    },
    "uniswap": {
        "total_supply": 1000000000,
        "vesting": [
            {
                "group": "Team and Investors",
                "allocation": 400000000,
                "cliff": 0,
                "cliff_amt": 0,
                "vesting_frequency": "daily",
                "start": "09-01-2020",
                "end": "09-01-2024"
            }
        ]
    },
    "euler": {
        "total_supply": 27182818,
        "vesting": [
            {
                "group": "Investors",
                "allocation": 7026759,
                "cliff": 0,
                "cliff_amt": 0,
                "vesting_frequency": "daily",
                "start": "12-31-2021",
                "end": "06-24-2023"
            }
        ]
    },
    "project-galaxy": {
        "total_supply": 200000000,
        "vesting": [
            {
                "group": "Investors I",
                "allocation": 21260000,
                "cliff": 90,
                "cliff_amt": 12,
                "vesting_frequency": "quarterly",
                "start": "05-09-2022",
                "end": "05-09-2025"
            },
            {
                "group": "Investors II",
                "allocation": 20280000,
                "cliff": 0,
                "cliff_amt": 12,
                "vesting_frequency": "quarterly",
                "start": "05-09-2022",
                "end": "05-09-2025"
            }
        ]
    },
    "bitdao": {
        "total_supply": 9610239403,
        "vesting": [
            {
                "group": "Investors",
                "allocation": 500000000,
                "cliff": 0,
                "cliff_amt": 0,
                "vesting_frequency": "monthly",
                "start": "10-14-2021",
                "end": "09-14-2022"
            }
        ]
    },
    "tornado-cash": {
        "total_supply": 3000000,
        "vesting": [
            {
                "group": "Team and Investors",
                "allocation": 3000000,
                "cliff": 365,
                "cliff_amt": 0,
                "vesting_frequency": "daily",
                "start": "12-12-2021",
                "end": "02-12-2023"
            }
        ]
    },
    "forta": {
        "total_supply": 1000000000,
        "vesting": [
            {
                "group": "Backers and Contributor",
                "allocation": 545329994,
                "cliff": 365,
                "cliff_amt": 0,
                "vesting_frequency": "daily",
                "start": "08-31-2022",
                "end": "08-30-2025"
            }
        ]
    },
    "pooltogether": {
        "total_supply": 10000000,
        "vesting": [
            {
                "group": "Team",
                "allocation": 1244000,
                "cliff": 0,
                "cliff_amt": 0,
                "vesting_frequency": "daily",
                "start": "02-16-2021",
                "end": "02-16-2022"
            },
            {
                "group": "Investors",
                "allocation": 752000,
                "cliff": 0,
                "cliff_amt": 0,
                "vesting_frequency": "daily",
                "start": "02-16-2021",
                "end": "02-16-2022"
            }
        ]
    },
    "merit-circle": {
        "total_supply": 899737985,
        "vesting": [
            {
                "group": "Team and Advisors",
                "allocation": 200000000,
                "cliff": 0,
                "cliff_amt": 0,
                "vesting_frequency": "daily",
                "start": "08-06-2022",
                "end": "08-30-2025"
            },
            {
                "group": "Early Investors",
                "allocation": 140625000,
                "cliff": 0,
                "cliff_amt": 0,
                "vesting_frequency": "daily",
                "start": "08-06-2022",
                "end": "08-30-2025"
            }
        ]
    },
    "decentraland": {
        "total_supply": 2193211827,
        "vesting": [
            {
                "group": "Team",
                "allocation": 561200000,
                "cliff": 180,
                "cliff_amt": 0,
                "vesting_frequency": "daily",
                "start": "08-17-2020",
                "end": "08-17-2024"
            }
        ]
    },
    "looksrare": {
        "total_supply": 1000000000,
        "vesting": [
            {
                "group": "Team Token",
                "allocation": 100000000,
                "cliff": 180,
                "cliff_amt": 0,
                "vesting_frequency": "quarterly",
                "start": "06-15-2022",
                "end": "08-30-2023"
            }
        ]
    },
    "sweatcoin": {
        "total_supply": 22249455607,
        "vesting": [
            {
                "group": "Private Round",
                "allocation": 459097271,
                "cliff": 365,
                "cliff_amt": 0,
                "vesting_frequency": "daily",
                "start": "09-12-2022",
                "end": "09-12-2026"
            }
        ]
    },
    "curve-dao-token": {
        "total_supply": 3003030299,
        "vesting": [
            {
                "group": "Team and Investors",
                "allocation": 909090909,
                "cliff": 0,
                "cliff_amt": 0,
                "vesting_frequency": "daily",
                "start": "08-13-2020",
                "end": "08-13-2024"
            }
        ]
    },
    "stakewise": {
        "total_supply": 1000000000,
        "vesting": [
            {
                "group": "Team",
                "allocation": 217000000,
                "cliff": 180,
                "cliff_amt": 0,
                "vesting_frequency": "daily",
                "start": "04-01-2021",
                "end": "03-31-2025"
            },
            {
                "group": "Investors",
                "allocation": 251500000,
                "cliff": 180,
                "cliff_amt": 0,
                "vesting_frequency": "daily",
                "start": "04-01-2021",
                "end": "03-31-2023"
            }
        ]
    },
    "stepn": {
        "total_supply": 6000000000,
        "vesting": [
            {
                "group": "Team",
                "allocation": 852000000,
                "cliff": 0,
                "cliff_amt": 0,
                "vesting_frequency": "daily",
                "start": "02-28-2023",
                "end": "02-28-2027"
            },
            {
                "group": "Private Sale",
                "allocation": 978000000,
                "cliff": 0,
                "cliff_amt": 0,
                "vesting_frequency": "daily",
                "start": "02-28-2023",
                "end": "02-28-2026"
            }
        ]
    },
    "gelato": {
        "total_supply": 420690000,
        "vesting": [
            {
                "group": "Private Investors I",
                "allocation": 44172450,
                "cliff": 0,
                "cliff_amt": 0,
                "vesting_frequency": "daily",
                "start": "09-13-2022",
                "end": "09-14-2022"
            },
            {
                "group": "Private Investors II",
                "allocation": 44172450,
                "cliff": 0,
                "cliff_amt": 0,
                "vesting_frequency": "daily",
                "start": "02-27-2023",
                "end": "02-28-2023"
            }
        ]
    },
    "lido-dao": {
        "total_supply": 1000000000,
        "vesting": [
            {
                "group": "Team and Validators",
                "allocation": 400400000,
                "cliff": 0,
                "cliff_amt": 0,
                "vesting_frequency": "daily",
                "start": "12-17-2021",
                "end": "12-17-2022"
            },
            {
                "group": "Investors",
                "allocation": 301625218,
                "cliff": 0,
                "cliff_amt": 0,
                "vesting_frequency": "daily",
                "start": "12-17-2021",
                "end": "12-17-2022"
            }
        ]
    },
    "filecoin": {
        "total_supply": 1963892418,
        "vesting": [
            {
                "group": "Protocol Labs Team and Contributors",
                "allocation": 90000000,
                "cliff": 0,
                "cliff_amt": 0,
                "vesting_frequency": "daily",
                "start": "08-10-2017",
                "end": "08-10-2023"
            },
            {
                "group": "Protocol Labs",
                "allocation": 210000000,
                "cliff": 0,
                "cliff_amt": 0,
                "vesting_frequency": "daily",
                "start": "08-10-2017",
                "end": "08-10-2023"
            },
            {
                "group": "Filecoin Foundation",
                "allocation": 100000000,
                "cliff": 0,
                "cliff_amt": 0,
                "vesting_frequency": "daily",
                "start": "08-10-2017",
                "end": "08-10-2023"
            }
        ]
    }
}


public_allocations = {
    "nym": {
        "total_supply": 1000000000,
        "vesting": [
            {
                "group": "Reserve & Community",
                "allocation": 100000000,
                "cliff": 0,
                "cliff_amt": 0,
                "vesting_frequency": "quarterly",
                "start": "04-13-2022",
                "end": "01-13-2024"
            }
        ]
    },
    "project-galaxy": {
        "total_supply": 200000000,
        "vesting": [
            {
                "group": "Public Sale",
                "allocation": 10000000,
                "cliff": 0,
                "cliff_amt": 0,
                "vesting_frequency": "weekly",
                "start": "05-05-2022",
                "end": "04-27-2023"
            },
            {
                "group": "Treasury",
                "allocation": 40000000,
                "cliff": 90,
                "cliff_amt": 0,
                "vesting_frequency": "quarterly",
                "start": "05-05-2022",
                "end": "04-09-2027"
            }
        ]
    },
    "bitdao": {
        "total_supply": 9610239403,
        "vesting": [
            {
                "group": "Treasury",
                "allocation": 3000000000,
                "cliff": 90,
                "cliff_amt": 0,
                "vesting_frequency": "monthly",
                "start": "07-14-2021",
                "end": "09-14-2022"
            }
        ]
    },
    "pooltogether": {
        "total_supply": 10000000,
        "vesting": [
            {
                "group": "Treasury",
                "allocation": 5754000,
                "cliff": 0,
                "cliff_amt": 0,
                "vesting_frequency": "daily",
                "start": "02-16-2021",
                "end": "02-16-2023"
            }
        ]
    },
    "merit-circle": {
        "total_supply": 899737985,
        "vesting": [
            {
                "group": "Public Sale",
                "allocation": 301875000,
                "cliff": 0,
                "cliff_amt": 0,
                "vesting_frequency": "daily",
                "start": "11-04-2021",
                "end": "11-04-2024"
            }
        ]
    },
    "sweatcoin": {
        "total_supply": 22249455607,
        "vesting": [
            {
                "group": "Community",
                "allocation": 5156802051,
                "cliff": 0,
                "cliff_amt": 10,
                "vesting_frequency": "daily",
                "start": "09-12-2022",
                "end": "09-12-2024"
            }
        ]
    },
    "stakewise": {
        "total_supply": 1000000000,
        "vesting": [
            {
                "group": "Community",
                "allocation": 510000000,
                "cliff": 0,
                "cliff_amt": 0,
                "vesting_frequency": "daily",
                "start": "04-01-2021",
                "end": "03-31-2025"
            }
        ]
    },
    "aptos": {
        "total_supply": 1000000000,
        "vesting": [
            {
                "group": "Community",
                "allocation": 385217360,
                "cliff": 0,
                "cliff_amt": 0,
                "vesting_frequency": "monthly",
                "start": "11-11-2022",
                "end": "11-11-2032"
            }
        ]
    }
}
