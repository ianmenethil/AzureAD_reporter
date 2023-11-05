# Description: Logicbomb.py contains Common classes used in python files. Contents:
from datetime import datetime
import pandas as pd

class Logic:
    @staticmethod
    def check_compliance(row, datetime_columns, ninety_days_ago, logger, row_identifier):  # pylint: disable=unused-argument
        is_compliant = False
        # latest_date = None
        # reason = "No valid dates found"  # pylint: disable=unused-variable
        for field_name in datetime_columns:
            date_str = row.get(field_name)
            if pd.isna(date_str) or date_str in ['', 'None', None]:
                continue  # Skip empty or non-existing date strings
            try:
                date_obj = pd.to_datetime(date_str)

                if ninety_days_ago <= date_obj <= datetime.now():  # Check if the date is within the range between 90 days ago and now
                    is_compliant = True
                    # latest_date = date_obj
                    # reason = f"Compliant - {field_name}: {latest_date.strftime('%Y-%m-%d')}"  # pylint: disable=unused-variable
            except Exception as e:
                logger.error(f"Error processing date for field '{field_name}' with value '{date_str}': {e}")
        # current_date_str = datetime.now().strftime('%Y-%m-%d')  # pylint: disable=unused-variable
        # ninety_days_ago_str = ninety_days_ago.strftime('%Y-%m-%d')  # pylint: disable=unused-variable
        # logger.info(f"User: {row_identifier} | Checking {current_date_str} against {ninety_days_ago_str} | {reason}")
        return is_compliant

    @staticmethod
    def get_row_identifier(row):  # Use mail if available, otherwise use displayName
        return row['mail'] if pd.notna(row['mail']) and row['mail'] != '' else row['displayName']
