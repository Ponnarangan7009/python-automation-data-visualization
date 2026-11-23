import pandas as pd

memory = [120, 125, 130, 145, 160]

data = {
    "time": [0, 4, 8, 12, 16],
    "memory": [120, 125, 130, 145, 160],
    "cpu": [10, 15, 20, 25, 30]
}

series_data = pd.Series(memory)
df_data = pd.DataFrame(data)
print(series_data)
print(df_data['memory'])
print(df_data['cpu'])
print(df_data)