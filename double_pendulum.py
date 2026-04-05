import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
start_angle = input('STARTING ANGLE: ')
speed = int((input('SPEED: ')))
g = 9.81
m1, m2 = 1, 1
L1, L2 = 1, 1
dt = 0.02
theta1 = -(int(start_angle) * np.pi / 180) + np.pi
theta1 = float(theta1)
theta2 = -(int(start_angle) * np.pi / 180) + np.pi
theta2 = float(theta2)
omega1 = 0
omega2 = 0
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
line, = ax.plot([], [], 'o-', lw = 2, zorder = 2)
trail, = ax.plot([], [], color = 'black', lw = 1, zorder = 1)
x2_trail = []
y2_trail = []
def update(frame):
    global theta1, theta2, omega1, omega2
    for _ in range(speed):
        delta = theta1 - theta2
        den = 2 * m1 + m2 - m2 * np.cos(2 * delta)
        if abs(den) < 1e-6:
            den = 1e-6
        domega1 = (-g * (2 * m1 + m2) * np.sin(theta1) - m2 * g * np.sin(theta1 - 2 * theta2) - 2 * np.sin(delta) * m2 * (omega2**2 * L2 + omega1**2 * L1 * np.cos(delta))) / (L1 * den)
        domega2 = (2*np.sin(delta)*(omega1**2*L1*(m1+m2) + g*(m1+m2)*np.cos(theta1) + omega2**2*L2*m2*np.cos(delta))) / (L2*den)
        omega1 += domega1 * dt
        omega2 += domega2 * dt
        theta1 += omega1 * dt
        theta2 += omega2 * dt
    x1 = L1 * np.sin(theta1)
    y1 = -L1 * np.cos(theta1)
    x2 = x1 + L2 * np.sin(theta2)
    y2 = y1 - L2 * np.cos(theta2)
    x2_trail.append(x2)
    y2_trail.append(y2)
    line.set_data([0, x1, x2], [0, y1, y2])
    trail.set_data(x2_trail, y2_trail)
    return line, trail
ani = FuncAnimation(fig, update, frames = 3000, interval = 20)
plt.show()
