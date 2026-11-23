from pathlib import Path

import matplotlib.pyplot as plt

OUTPUT_FILE = Path(__file__).resolve().parent / 'app_performance_report.png'

time = [0, 4, 8, 12, 16, 20, 24, 28, 32]

app_x_memory = [120, 125, 130, 145, 160, 175, 190, 220, 250]

app_y_memory = [100, 110, 125, 140, 155, 180, 210, 230, 240]

plt.bar([t - 0.75 for t in time], app_x_memory,
        width=1.5, color='blue', label='App X')

plt.bar([t + 0.75 for t in time], app_y_memory,
        width=1.5, color='orange', label='App Y')

plt.xlabel("Time (seconds)")
plt.ylabel("Memory (MB)")
plt.title("Memory Comparison - App X vs App Y")

plt.legend()
plt.grid(True)

plt.savefig(OUTPUT_FILE)
plt.show()
