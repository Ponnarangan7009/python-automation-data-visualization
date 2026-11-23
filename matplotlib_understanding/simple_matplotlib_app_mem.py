import matplotlib.pyplot as plt

time = [0, 4, 8, 12, 16, 20, 24, 28, 32]

app_x_memory = [120, 125, 130, 145, 165, 185, 200, 220, 250]

plt.plot(time, app_x_memory, marker='o')

plt.xlabel("Time (seconds)")
plt.ylabel("App x memory (MB)")
plt.title("Memory Comparison - App X")

plt.grid(True)
plt.show()