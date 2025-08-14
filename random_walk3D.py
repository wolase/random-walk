import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  
from matplotlib.animation import FuncAnimation
import os

def random_walk_3d(dimension):
    directions = [
        "north", "south", "east", "west", "up", "down",
        "northeast", "northwest", "southeast", "southwest",
        "up-north", "up-south", "up-east", "up-west",
        "down-north", "down-south", "down-east", "down-west"
    ]

    x, y, z = [0], [0], [0]  # starting point at the center of the cube

    i = 0
    while (
        abs(x[i]) < dimension  and 
        abs(y[i]) < dimension  and
        abs(z[i]) < dimension 
    ):
        move = random.choice(directions)

        if move == 'north':
            x.append(x[i])
            y.append(y[i] + 1)
            z.append(z[i])

        elif move == 'south':
            x.append(x[i])
            y.append(y[i] - 1)
            z.append(z[i])

        elif move == 'east':
            x.append(x[i] + 1)
            y.append(y[i])
            z.append(z[i])

        elif move == 'west':
            x.append(x[i] - 1)
            y.append(y[i])
            z.append(z[i])

        elif move == 'up':
            x.append(x[i])
            y.append(y[i])
            z.append(z[i] + 1)

        elif move == 'down':
            x.append(x[i])
            y.append(y[i])
            z.append(z[i] - 1)

        elif move == 'northeast':
            x.append(x[i] + 1)
            y.append(y[i] + 1)
            z.append(z[i])

        elif move == 'northwest':
            x.append(x[i] - 1)
            y.append(y[i] + 1)
            z.append(z[i])

        elif move == 'southeast':
            x.append(x[i] + 1)
            y.append(y[i] - 1)
            z.append(z[i])

        elif move == 'southwest':
            x.append(x[i] - 1)
            y.append(y[i] - 1)
            z.append(z[i])

        elif move == 'up-north':
            x.append(x[i])
            y.append(y[i] + 1)
            z.append(z[i] + 1)

        elif move == 'up-south':
            x.append(x[i])
            y.append(y[i] - 1)
            z.append(z[i] + 1)

        elif move == 'up-east':
            x.append(x[i] + 1)
            y.append(y[i])
            z.append(z[i] + 1)

        elif move == 'up-west':
            x.append(x[i] - 1)
            y.append(y[i])
            z.append(z[i] + 1)

        elif move == 'down-north':
            x.append(x[i])
            y.append(y[i] + 1)
            z.append(z[i] - 1)

        elif move == 'down-south':
            x.append(x[i])
            y.append(y[i] - 1)
            z.append(z[i] - 1)

        elif move == 'down-east':
            x.append(x[i] + 1)
            y.append(y[i])
            z.append(z[i] - 1)

        elif move == 'down-west':
            x.append(x[i] - 1)
            y.append(y[i])
            z.append(z[i] - 1)

        i += 1

    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_folder = os.path.join(script_dir, "output")
    os.makedirs(output_folder, exist_ok=True)

# Static plot part
    fig_static = plt.figure()
    ax_static = fig_static.add_subplot(111, projection='3d')
    ax_static.plot(x, y, z, color='red', marker='o')
    ax_static.set_title("Random Walk 3D - Static View")
    static_path = os.path.join(output_folder, "random_walk_3d.png")
    plt.savefig(static_path)
    plt.show()

# Animation part
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlim(-dimension, dimension)
    ax.set_ylim(-dimension, dimension)
    ax.set_zlim(-dimension, dimension)
    ax.set_title('Random Walk 3D Animation')

    line, = ax.plot([], [], [], lw=2, color='red')
    point, = ax.plot([], [], [], 'ro')

    def init():
        line.set_data([], [])
        line.set_3d_properties([])
        point.set_data([], [])
        point.set_3d_properties([])
        return line, point

    def update(frame):
        line.set_data(x[:frame], y[:frame])
        line.set_3d_properties(z[:frame])
        point.set_data([x[frame]], [y[frame]])
        point.set_3d_properties([z[frame]])
        return line, point

    anim = FuncAnimation(fig, update, frames=len(x), init_func=init, blit=True, interval=100)

    gif_path = os.path.join(output_folder, "random_walk_3d.gif")
    anim.save(gif_path, writer='pillow')
    plt.show()
    
    return