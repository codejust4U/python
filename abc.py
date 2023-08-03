import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Assuming 'epochs', 'X', 'y', 'all_m', and 'all_b' are defined appropriately

fig, ax = plt.subplots(figsize=(9, 5))

x_i = np.arange(-3, 3, 0.1)
y_i = x_i * (-27) - 150
X,y = make_regression(n_samples=100,n_features=1,n_informative=1,n_targets=1,noise=20,random_state=13)
plt.scatter(X,y)
ax.scatter(X, y)

line, = ax.plot(x_i, x_i * 150 - 4, 'r-', linewidth=2)

def update(i):
    label = 'epoch{0}'.format(i + 1)
    line.set_ydata(x_i * all_m[i] + all_b[i])
    ax.set_xlabel(label)

# The 'frames' argument should be the number of epochs
epochs = len(all_m)

# The 'interval' argument is the delay between frames in milliseconds
animation_interval = 500

anim = FuncAnimation(fig, update, repeat=True, frames=epochs, interval=animation_interval)

plt.show()
