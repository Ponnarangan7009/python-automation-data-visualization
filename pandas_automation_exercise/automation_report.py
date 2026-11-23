from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).resolve().parent

df = pd.read_csv(DATA_DIR / 'automation_results.csv')

total_test_counts = len(df['status'])

total_passed_test_count = len(df[df['status'] == 'Pass'])
total_failed_test_count = len(df[df['status'] == 'Fail'])
passed_test_percentage = total_passed_test_count/total_test_counts * 100


df[df['status'] == 'Pass'].to_csv(DATA_DIR / 'passed_tests.csv', index=False)
df[df['status'] == 'Fail'].to_csv(DATA_DIR / 'failed_tests.csv', index=False)

slow_test_cases = df[df['execution_time'] > 5]
slow_test_cases.to_csv(DATA_DIR / 'slow_tests.csv', index=False)

summary = {
    "Metric": ["Total Tests", "Passed", "Failed", "Pass Percentage"],
    "Value": [total_test_counts, total_passed_test_count, total_failed_test_count, passed_test_percentage]
}
summary_df = pd.DataFrame(summary)

print(summary_df)

summary_df.to_csv(DATA_DIR / "execution_summary.csv", index=False)
