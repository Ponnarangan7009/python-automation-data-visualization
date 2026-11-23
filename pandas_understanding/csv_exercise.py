from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).resolve().parent

df = pd.read_csv(DATA_DIR / "test_results.csv")

print(df[df['status'] == 'Pass']) # data frame
print(df['status'] == 'Pass') # series

print(df[
    (df["status"] == "Fail") &
    (df["execution_time"] > 5)
])

print(df[
    (df["status"] == "Fail") |
    (df["execution_time"] > 5)
])

print(df.loc[1, "status"])
print(df.iloc[3, 0])

