
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt

DATA_DIR = Path(__file__).resolve().parent

# --------------------------------------------------
# 1. Read automation test results
# --------------------------------------------------

df = pd.read_csv(DATA_DIR / "automation_results.csv")

print("\nAUTOMATION TEST RESULTS")
print(df)

# --------------------------------------------------
# 2. Analyse test execution results using Pandas
# --------------------------------------------------

total_tests = len(df)

passed_tests = len(df[df["status"] == "Pass"])

failed_tests = len(df[df["status"] == "Fail"])

pass_percentage = (passed_tests / total_tests) * 100

print("\nTEST EXECUTION SUMMARY")
print("----------------------")
print("Total Tests:", total_tests)
print("Passed Tests:", passed_tests)
print("Failed Tests:", failed_tests)
print("Pass Percentage:", round(pass_percentage, 2), "%")

# --------------------------------------------------
# 3. Identify slow test cases
# --------------------------------------------------

slow_tests = df[df["execution_time"] > 5]

print("\nSLOW TEST CASES")
print(slow_tests)

# --------------------------------------------------
# 4. Create Pass vs Fail Bar Chart
# --------------------------------------------------

status = ["Passed", "Failed"]

counts = [passed_tests, failed_tests]

plt.figure(figsize=(8, 5))

plt.bar(
    status,
    counts,
    color=["green", "red"],
    label="Test Count"
)

plt.xlabel("Test Status")
plt.ylabel("Number of Tests")
plt.title("Automation Test Execution Summary")

plt.legend()
plt.grid(axis="y")

plt.savefig(DATA_DIR / "test_execution_summary.png")
plt.show()

# --------------------------------------------------
# 5. Create Execution Time Line Chart
# --------------------------------------------------

plt.figure(figsize=(12, 5))

plt.plot(
    df["test_case"],
    df["execution_time"],
    marker="o",
    color="blue",
    label="Execution Time"
)

plt.xlabel("Test Cases")
plt.ylabel("Execution Time (seconds)")
plt.title("Test Case Execution Time")

plt.xticks(rotation=90)

plt.legend()
plt.grid(True)

plt.tight_layout()

plt.savefig(DATA_DIR / "test_execution_time.png")
plt.show()

# --------------------------------------------------
# 6. Create Slow Test Cases Horizontal Bar Chart
# --------------------------------------------------

plt.figure(figsize=(10, 6))

plt.barh(
    slow_tests["test_case"],
    slow_tests["execution_time"],
    color="orange",
    label="Slow Tests"
)

plt.xlabel("Execution Time (seconds)")
plt.ylabel("Test Cases")
plt.title("Slow Test Cases - Above 5 Seconds")

plt.legend()
plt.grid(axis="x")

plt.tight_layout()

plt.savefig(DATA_DIR / "slow_test_cases.png")
plt.show()

# --------------------------------------------------
# 7. Export analysis results
# --------------------------------------------------

slow_tests.to_csv(DATA_DIR / "slow_test_report.csv", index=False)

print("\nVisualization completed successfully!")
print("Generated:")
print("- test_execution_summary.png")
print("- test_execution_time.png")
print("- slow_test_cases.png")
print("- slow_test_report.csv")
