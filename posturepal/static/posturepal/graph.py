# to run the graph: in terminal run these commands: 
# python app.py
# python graph.py

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

x_data = []  
y_data = [] 

fig, ax = plt.subplots()
ax.set_xlim(0, 300)  
ax.set_ylim(0, 100) 
ax.set_xlabel('Time (seconds)')
ax.set_ylabel('Posture Score')
ax.set_title('Real-Time Posture Score Tracking')

line, = ax.plot([], [], lw=2)

def posture_score(data):
    x, y, z = data
    return 100 / (1 + (x - 10)**2 + y**2 + z**2)
# with "ideal posture values," X will be hovering around ~10, Y and Z will be close to 0
# with "poor posture values," X will be approaching 0, Y and Z will either increase or decrease
# good posture values - posture score approaches 100, bad posture values - posture score approaches 0.33

def animate(frame):
    global x_data, y_data

    posture_data = [random.uniform(8, 12), random.uniform(-2, 2), random.uniform(-2, 2)]

    score = posture_score(posture_data)

    current_time = len(x_data)  
    x_data.append(current_time)
    y_data.append(score)

    if len(x_data) > 300:
        x_data.pop(0)
        y_data.pop(0)

    line.set_data(x_data, y_data)

    ax.set_xlim(max(0, current_time - 300), current_time)

    print(f"Frame: {frame} | X: {posture_data[0]:.2f}, Y: {posture_data[1]:.2f}, Z: {posture_data[2]:.2f} | Score: {score:.2f}")
    
    return line,

ani = animation.FuncAnimation(fig, animate, interval=1000)  

plt.show()

