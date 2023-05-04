import pandas as pd
import math
import time
import json
import os

# We'll store the old data here.
old_data = None

def is_equal(a,b):
    if a == b:
        return True
    if math.isnan(a) and math.isnan(b):
        return True
    return False

def compare_dataframes(old_data, new_data):
    changes = []
    for col in new_data.columns:
        for row in range(len(new_data)):
            old_value = old_data.at[row, col]
            new_value = new_data.at[row, col]
            if not is_equal(old_value,new_value):
                change = {
                    'row': row,
                    'column': col,
                    'old_value': old_value,
                    'new_value': new_value
                }
                changes.append(change)
    return changes

def save_changes_to_json(changes):
    with open("log.txt", "w") as f:  # w for overwrite, a for append
        f.write(json.dumps(changes, indent=2))

if __name__ == "__main__":

    #while True:
    print("Reading old funnel...")
    old_data = pd.read_excel("old_funnel.xlsm",sheet_name="FY23 Growth Initiatives",header=8)
    print("Reading new funnel...")
    new_data = pd.read_excel("funnel.xlsm", sheet_name="FY23 Growth Initiatives", header=8)
    print("Comparing...")
    changes = compare_dataframes(old_data, new_data)

    if changes:
        save_changes_to_json(changes)
    else:
        print("no changes")

    #    time.sleep(1)
