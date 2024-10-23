import matplotlib.pyplot as plt
import numpy as np

def calculate_diagonal_sums(matrix):
    primary_diagonal_sum = 0
    secondary_diagonal_sum = 0
    N = len(matrix)

    # Calculate the sum of the primary and secondary diagonals
    for i in range(N):
        primary_diagonal_sum += matrix[i][i]
        secondary_diagonal_sum += matrix[i][N - i - 1]

    return primary_diagonal_sum, secondary_diagonal_sum

def visualize_spiral_with_numbers_arrows_and_sums(N):
    # Create the spiral matrix
    matrix = [[0] * N for _ in range(N)]
    x, y = N // 2, N // 2
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
    direction_names = ["right", "down", "left", "up"]
    current_direction = 0
    number = 1
    step_size = 1

    # Prepare the figure for visualizing the process of building the spiral
    fig, ax = plt.subplots(figsize=(6, 6))
    
    # Set up the plot
    ax.set_xticks([])
    ax.set_yticks([])

    while number <= N * N:
        for _ in range(2):
            for _ in range(step_size):
                if 0 <= x < N and 0 <= y < N:
                    matrix[x][y] = number

                    # Refresh the plot to show the matrix being filled
                    ax.clear()
                    ax.imshow(matrix, cmap="Blues", vmin=0, vmax=N * N)
                    
                    # Add the numbers to the matrix
                    for i in range(N):
                        for j in range(N):
                            if matrix[i][j] != 0:
                                ax.text(j, i, f"{matrix[i][j]}", va='center', ha='center', fontsize=12)
                    
                    # Add arrows to show the direction of each step
                    direction = direction_names[current_direction]
                    if direction == "right":
                        ax.annotate('', xy=(y, x), xytext=(y-0.5, x),
                                    arrowprops=dict(facecolor='red', shrink=0.05))
                    elif direction == "down":
                        ax.annotate('', xy=(y, x), xytext=(y, x-0.5),
                                    arrowprops=dict(facecolor='blue', shrink=0.05))
                    elif direction == "left":
                        ax.annotate('', xy=(y, x), xytext=(y+0.5, x),
                                    arrowprops=dict(facecolor='green', shrink=0.1))
                    elif direction == "up":
                        ax.annotate('', xy=(y, x), xytext=(y, x+0.5),
                                    arrowprops=dict(facecolor='orange', shrink=0.05))
                    
                    plt.pause(0.3)  # Pause briefly between steps to refresh the display
                    number += 1
                # Move to the next step
                y += directions[current_direction][1]
                x += directions[current_direction][0]
            current_direction = (current_direction + 1) % 4
        step_size += 1

    # Calculate diagonal sums
    primary_sum, secondary_sum = calculate_diagonal_sums(matrix)

    # Display the final matrix with diagonal sums
    ax.clear()
    ax.imshow(matrix, cmap="Blues", vmin=0, vmax=N * N)

    # Display the numbers in the matrix
    for i in range(N):
        for j in range(N):
            if matrix[i][j] != 0:
                ax.text(j, i, f"{matrix[i][j]}", va='center', ha='center', fontsize=12)

    # Display the diagonal sums below the plot
    ax.text(0, -0.6, f"Primary diagonal sum: {primary_sum}", fontsize=12, color='black', ha='center')
    ax.text(0, -0.87, f"Secondary diagonal sum: {secondary_sum}", fontsize=12, color='black', ha='center')

    # Adjust the figure size to make space for the text
    fig.subplots_adjust(bottom=0.2)
    # Show the plot
    plt.show()

# Test code to combine matrix visualization and diagonal sum calculation
if __name__ == "__main__":
    N = int(input('Please enter the matrix size: '))
    visualize_spiral_with_numbers_arrows_and_sums(N)
