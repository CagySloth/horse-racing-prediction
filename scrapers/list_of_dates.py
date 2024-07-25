import pandas as pd
from datetime import datetime
from typing import List, Dict


def get_dates(start_date: str, end_date: str = datetime.now()) -> List[Dict[str, str]]:
    """
    Generate dates in the desired format for Wednesdays and Saturdays
    between start_date and end_date.

    Args:
        start_date (str): The start date in 'YYYY/MM/DD' format.
        end_date (str): The end date in 'YYYY/MM/DD' format.

    Returns:
        list: A list of dictionaries containing the date, weekday, and location.
    """
    # Generate date range
    date_range = pd.date_range(start=start_date, end=end_date, freq='D')
    
    result = []
    for date in date_range:
        if date.weekday() == 2:  # Wednesday
            result.append({
                "date": date.strftime('%Y/%m/%d'),
                "weekday": "weds",
                "loc": "HV"
            })
        elif date.weekday() == 5:  # Saturday
            result.append({
                "date": date.strftime('%Y/%m/%d'),
                "weekday": "sat",
                "loc": "ST"
            })
    
    return result

