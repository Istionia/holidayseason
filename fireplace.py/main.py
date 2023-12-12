import pygame
import sys
import random
from typing import List, Tuple, Union

# Initialize Pygame
pygame.init()

# Set up window dimensions
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Virtual Fireplace")

# Set up colors
BLACK: Tuple[int, int, int] = (30, 30, 30)  # Dark gray
ORANGE: Tuple[int, int, int] = (255, 165, 0)
RED: Tuple[int, int, int] = (255, 0, 0)
FIREPLACE_BROWN: Tuple[int, int, int] = (139, 69, 19)

# Define Particle class
class Particle:
    def __init__(self, x: int, y: int) -> None:
        """
        Initialize a Particle.

        Parameters:
        - x (int): The x-coordinate of the particle.
        - y (int): The y-coordinate of the particle.
        """
        self.x = x
        self.y = y
        self.size = random.randint(10, 20)
        self.color = random.choice((ORANGE, RED, FIREPLACE_BROWN))
        self.speed = random.uniform(1, 3)

    def move(self) -> None:
        """Move the particle upward based on its speed."""
        self.y -= self.speed

    def draw(self) -> None:
        """Draw the particle on the window."""
        pygame.draw.circle(WIN, self.color, (self.x, int(self.y)), self.size)

# Define main function
def main() -> None:
    """
    Run the main loop to display the virtual fireplace.
    """
    particles: List[Particle] = []
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Create new particles
        for _ in range(5):
            new_particle = Particle(random.randint(350, 450), HEIGHT)
            particles.append(new_particle)

        # Move and draw particles
        for particle in particles:
            particle.move()
            particle.draw()

        # Remove particles that are out of the screen
        particles = [p for p in particles if p.y > 0]

        # Fill the background with dark gray
        WIN.fill(BLACK)

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(30)

if __name__ == "__main__":
    main()
