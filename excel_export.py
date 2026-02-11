import pandas as pd
import os

def export_to_excel(records):

    if not os.path.exists("output"):
        os.makedirs("output")

    df = pd.DataFrame(records)
    df = df.sort_values(by="Register Number")
    df.to_excel("output/Sorted_OMR_Result.xlsx", index=False)
