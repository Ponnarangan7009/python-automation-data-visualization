from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).resolve().parent

df = pd.read_csv(DATA_DIR / 'test_results.csv')


failed_cases = df[df['status'] == 'Fail']
print(failed_cases)

failed_cases.to_csv(DATA_DIR / 'failed_tests.csv', index=False)
failed_cases.to_excel(DATA_DIR / 'failed_tests.xlsx', index=False)
