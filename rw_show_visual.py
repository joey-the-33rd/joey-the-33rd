import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Make a random walk.
# Keep making new walks, as long as the program is active.

while True:
    # Make a random walk.
    
    rw = RandomWalk()
    rw.fill_walk()

    # Plot the points in the walk.
    plt.style.use('classic')
    # Set the sze of the ploting window.
    fig, ax = plt.subplots(figsize=(15,9), dpi=114)
    ax.scatter(rw.x_values, rw.y_values, s=15)

    # Coloring the points
    points_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=points_numbers, 
               cmap=plt.cm.Blues, edgecolors='none', s=1)
    
    # Cleaning up the axes.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    
    # Emphasize the first and last points.
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red',
               edgecolors='none', s=100)

    # Set title and labels.
    ax.set_title("Random Walk", fontsize=24)
    ax.set_xlabel("X Moves", fontsize=14)
    ax.set_ylabel("Y Moves", fontsize=14)

    # Set size of tick labels.
    ax.tick_params(axis='both', which='major', labelsize=14)

    ax.set_aspect('equal')

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break