# Create a DataFrame using the following automation test data:
# Test case	Execution time	Status
# Login	2.5	Pass
# Search	3.2	Pass
# Payment	5.8	Fail
# Logout	1.5	Pass

# Tasks:
# 1. Create a dictionary containing these three columns.
# 2. Convert the dictionary into a DataFrame.
# 3. Print the DataFrame.
# 4. Print only the status column.

import pandas as pd

test_case = ['Login', 'Search', 'Payment', 'Logout']

data = {
    'test_case': ['Login', 'Search', 'Payment', 'Logout'],
    'execution_time':[2.5, 3.2, 5.8, 1.5],
    'status': ['Pass', 'Pass', 'Fail', 'Pass']

}

series_data = pd.Series(data['test_case'])
data_frame = pd.DataFrame(data)

# print(series_data)
# print(data_frame)

# print(data_frame.loc[2])
# print(data_frame.head(5))
# print(data_frame.tail(5))
# print(data_frame.shape)
# data_frame.info()
print(data_frame.describe())
print(data_frame.describe(include="all"))