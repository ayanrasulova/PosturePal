import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

# Create figure and axis
fig, ax = plt.subplots()
x_data, y_data = [], []  # lists to store incoming data
line, = ax.plot([], [], 'b-', lw=2)  # Line object

# graph lmiits
ax.set_xlim(0, 100)  # fixed x-axis range (can be adjusted)
ax.set_ylim(-10, 10)  # adjust based on expected data range
ax.set_xlabel("Time")
ax.set_ylabel("Value")
ax.set_title("Real-Time Data Stream")

# function to get new data
def get_new_data():
    return random.uniform(-5, 5)  # replace with actual data source

# update function for animation
def update(frame):
    x_data.append(frame)  # Simulate time index
    y_data.append(get_new_data())

    # Keep the last 100 points (prevents memory overload)
    if len(x_data) > 100:
        x_data.pop(0)
        y_data.pop(0)

    line.set_data(x_data, y_data)
    ax.set_xlim(max(0, frame-100), frame)  # slide window forward
    return line,

# animate the graph (updates every 100ms)
ani = animation.FuncAnimation(fig, update, interval=100)

plt.show()
