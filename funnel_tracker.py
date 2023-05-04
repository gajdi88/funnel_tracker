import pandas as pd
from deepdiff import DeepDiff
import time
import json
import os

# We'll store the old data here.
old_data = None

def check_mods(new_data,old_data = None):

    # Only act if the modified file is our target file.
    try:
        # Read the Excel file.


        if old_data is not None:
            # Compare the old data with the new data.
            diff = DeepDiff(old_data, new_data,ignore_nan_inequality=True)
            if diff:
                # Log the changes.
                with open("log.txt", "a") as f:
                    f.write(json.dumps(diff, indent=2))

        # Update the old data.
        old_data = new_data
    except Exception as e:
        print(f"Error: {str(e)}")
    return old_data

if __name__ == "__main__":

    #while True:
    old_data = pd.read_excel("old_funnel.xlsm",sheet_name="FY23 Growth Initiatives",header=8).to_dict()
    new_data = pd.read_excel("funnel.xlsm", sheet_name="FY23 Growth Initiatives", header=8).to_dict()

    old_data = check_mods(new_data, old_data=old_data)

    #    time.sleep(1)
