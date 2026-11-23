import matplotlib.pyplot as plt

apps = ['App X', 'App Y']

memory = [250, 240]

plt.barh(apps, memory, color=['blue', 'orange'])

plt.xlabel("Memory (MB)")
plt.ylabel("Applications")
plt.title("Application Memory Comparison")

plt.grid(axis='x')

plt.show()