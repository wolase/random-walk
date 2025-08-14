import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt
import os
from matplotlib.animation import FuncAnimation

def random_walk(dimension):
    directions = ["north", "south", "east", "west", "northeast", "northwest", "southeast", "southwest"]

    x, y = [0.5], [0.5]  # Starting point at the center of the grid
    i = 0

    while abs(x[i]) != dimension + 0.5 and abs(y[i]) != dimension + 0.5:
        move = random.choice(directions)

        if move == 'north':
            x[i] = x[i-1]
            y[i] = y[i-1] + 1
        elif move == 'south':
            x[i] = x[i-1]
            y[i] = y[i-1] - 1
        elif move == 'east':
            x[i] = x[i-1] + 1
            y[i] = y[i-1]
        elif move == 'west':
            x[i] = x[i-1] - 1
            y[i] = y[i-1]
        elif move == 'north-east':
            x[i] = x[i-1] + 1
            y[i] = y[i-1] + 1
        elif move == 'south-east':
            x[i] = x[i-1] + 1
            y[i] = y[i-1] - 1
        elif move == 'south-west':
            x[i] = x[i-1] - 1
            y[i] = y[i-1] - 1
        else:  
            x[i] = x[i-1] - 1
            y[i] = y[i-1] + 1

        x.append(x[i])
        y.append(y[i])
        i += 1

    # Inserting starting point at beginning
    x.insert(0, 0.5)
    y.insert(0, 0.5)

    df = pd.DataFrame({'x': x, 'y': y})

    # Static plot part

    plt.plot(x, y, marker='o', markersize=5, color='red')
    plt.title('Random walk in 8 directions')
    ax = plt.gca()
    ax.set_xticks(np.arange(-dimension, dimension+1, 1))
    ax.set_yticks(np.arange(-dimension, dimension+1, 1))
    plt.grid(True)

    #Saving the outputs

    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_folder = os.path.join(script_dir, "output")
    os.makedirs(output_folder, exist_ok=True)

    png_path = os.path.join(output_folder, "random_walk_2d.png")
    plt.savefig(png_path)
    print(f"PNG saved at: {png_path}")
    plt.show()

    # Animation part
    fig, ax = plt.subplots()
    ax.set_xlim(-dimension-1, dimension+1)
    ax.set_ylim(-dimension-1, dimension+1)
    ax.set_xticks(np.arange(-dimension, dimension+1, 1))
    ax.set_yticks(np.arange(-dimension, dimension+1, 1))
    ax.grid(True)
    ax.set_title('Random walk in 8 directions (Animated)')

    line, = ax.plot([], [], lw=2, color='red')
    point, = ax.plot([], [], 'ro')

    def init():
        line.set_data([], [])
        point.set_data([], [])
        return line, point

    def update(frame):
        line.set_data(x[:frame], y[:frame])
        if frame < len(x) and frame < len(y):
            point.set_data([x[frame]], [y[frame]])
        else:
            point.set_data([], [])
        return line, point

    anim = FuncAnimation(fig, update, frames=len(x), init_func=init, blit=True, interval=300)

    # Saving the animation in output folder
    gif_path = os.path.join(output_folder, "random_walk_2d.gif")
    anim.save(gif_path, writer="pillow")

    plt.show()

    return
