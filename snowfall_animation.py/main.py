import pygame
import sys
import random
from typing import List, Tuple, Union

def initialize_snowflakes(num_snowflakes: int, width: int, height: int) -> List[List[int]]:
    """
    Initialize a list of snowflakes with random positions and speeds.

    Parameters:
    - num_snowflakes (int): Number of snowflakes to create.
    - width (int): Width of the screen.
    - height (int): Height of the screen.

    Returns:
    - List[List[int]]: A list containing snowflake information [x, y, speed].
    """
    snowflakes = []
    for _ in range(num_snowflakes):
        x = random.randint(0, width)
        y = random.randint(0, height)
        speed = random.randint(1, 10)
        snowflakes.append([x, y, speed])
    return snowflakes

def update_snowflakes(snowflakes: List[List[int]], width: int, height: int) -> None:
    """
    Update the positions of snowflakes and reset if they go below the screen.

    Parameters:
    - snowflakes (List[List[int]]): List containing snowflake information [x, y, speed].
    - height (int): Height of the screen.
    """
    for i in range(len(snowflakes)):
        snowflakes[i][1] += snowflakes[i][2]

        # If a snowflake goes below the screen, reset its position
        if snowflakes[i][1] > height:
            snowflakes[i][1] = 0
            snowflakes[i][0] = random.randint(0, width)

def draw_snowflakes(display_surface: pygame.surface.Surface, snowflakes: List[List[int]]) -> None:
    """
    Draw snowflakes on the screen.

    Parameters:
    - display_surface (pygame.surface.Surface): Pygame surface to draw on.
    - snowflakes (List[List[int]]): List containing snowflake information [x, y, speed].
    """
    white = (255, 255, 255)
    for snowflake in snowflakes:
        pygame.draw.circle(display_surface, white, (snowflake[0], int(snowflake[1])), 5)


def main():
    # Initialize Pygame
    pygame.init()

    # Set up display
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Snowfall")

    # Create snowflakes
    num_snowflakes = 100
    snowflakes = initialize_snowflakes(num_snowflakes, width, height)

    # Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Update snowflakes' positions
        update_snowflakes(snowflakes, width, height)

        # Draw background
        screen.fill((0, 0, 0))  # Black background

        # Draw snowflakes
        draw_snowflakes(screen, snowflakes)

        # Update display
        pygame.display.flip()

        # Control the frame rate
        pygame.time.Clock().tick(30)

if __name__ == "__main__":
    main()