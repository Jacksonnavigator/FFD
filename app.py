import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_field():
    # Create a figure
    fig, ax = plt.subplots(figsize=(10, 7))

    # Pitch Outline & Centre Line
    plt.plot([0, 0], [0, 90], color="green")
    plt.plot([0, 130], [90, 90], color="green")
    plt.plot([130, 130], [90, 0], color="green")
    plt.plot([130, 0], [0, 0], color="green")
    plt.plot([65, 65], [0, 90], color="green")

    # Left Penalty Area
    plt.plot([16.5, 16.5], [65, 25], color="green")
    plt.plot([0, 16.5], [65, 65], color="green")
    plt.plot([16.5, 0], [25, 25], color="green")

    # Right Penalty Area
    plt.plot([130, 113.5], [65, 65], color="green")
    plt.plot([113.5, 113.5], [65, 25], color="green")
    plt.plot([113.5, 130], [25, 25], color="green")

    # Left 6-yard Box
    plt.plot([0, 5.5], [54, 54], color="green")
    plt.plot([5.5, 5.5], [54, 36], color="green")
    plt.plot([5.5, 0.5], [36, 36], color="green")

    # Right 6-yard Box
    plt.plot([130, 124.5], [54, 54], color="green")
    plt.plot([124.5, 124.5], [54, 36], color="green")
    plt.plot([124.5, 130], [36, 36], color="green")

    # Prepare Circles; Centre Circle, Penalty Spot
    centreCircle = plt.Circle((65, 45), 9.15, color="green", fill=False)
    centreSpot = plt.Circle((65, 45), 0.8, color="green")
    leftPenSpot = plt.Circle((11, 45), 0.8, color="green")
    rightPenSpot = plt.Circle((119, 45), 0.8, color="green")

    # Draw Circles
    ax.add_patch(centreCircle)
    ax.add_patch(centreSpot)
    ax.add_patch(leftPenSpot)
    ax.add_patch(rightPenSpot)

    # Prepare Arcs
    leftArc = patches.Arc((11, 45), 18.3, 18.3, angle=0, theta1=308, theta2=52, color="green")
    rightArc = patches.Arc((119, 45), 18.3, 18.3, angle=0, theta1=128, theta2=232, color="green")

    # Draw Arcs
    ax.add_patch(leftArc)
    ax.add_patch(rightArc)

    plt.xlim([-5, 135])
    plt.ylim([-5, 95])
    plt.axis('off')  # Hide the axis

def plot_players(players):
    # Draw the field
    draw_field()

    # Plot player positions
    for player in players:
        plt.plot(player['x'], player['y'], 'ro', markersize=12)  # 'ro' is red dot for players
        plt.text(player['x'], player['y'] + 2, player['name'], fontsize=9, ha='center')

    # Show the field with players
    plt.show()

# Example player positions
players = [
    {'name': 'Player 1', 'x': 10, 'y': 45},
    {'name': 'Player 2', 'x': 30, 'y': 60},
    {'name': 'Player 3', 'x': 30, 'y': 30},
    {'name': 'Player 4', 'x': 50, 'y': 45},
    {'name': 'Goalkeeper', 'x': 5.5, 'y': 45}
]

plot_players(players)
