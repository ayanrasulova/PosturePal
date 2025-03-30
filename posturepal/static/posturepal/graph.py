# to run the graph: in terminal run these commands: 
# python app.py
# python graph.py

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import requests
import time

x_data = []  # time data (seconds) for x axis
y_data = []  # posture score data for y axis

fig, ax = plt.subplots() #c reates axis
ax.set_xlim(0, 300)  # 5m of data
ax.set_ylim(0, 100)  
ax.set_xlabel('Time (seconds)')
ax.set_ylabel('Posture Score')
ax.set_title('Real-Time Posture Score Tracking')

line, = ax.plot([], [], lw=2)


# Update function for animation
def update(frame):
    try:
        # get score from flask
        response = requests.post('http://127.0.0.1:5000/calculate', json={'x': 10, 'y': 0, 'z': 0})
        data = response.json()
        posture_score = data.get('score', 0)  # default to 0 if no score is returned

        # update time and posture score data
        current_time = len(x_data)  # time in s since start
        x_data.append(current_time)
        y_data.append(posture_score)

        line.set_data(x_data, y_data)
        ax.set_xlim(max(0, current_time - 300), current_time) # x axis only shows last 300s (5m)

    except Exception as e:
        print(f"Error fetching posture score: {e}")

    return line,

ani = animation.FuncAnimation(fig, update, interval=1000)  # animates (update every second)

plt.show()
