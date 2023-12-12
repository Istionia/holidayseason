import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up window dimensions
width, height = 800, 600
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Virtual Fireplace")

# Set up colors
black = (30, 30, 30)  # Dark gray
orange = (255, 165, 0)
red = (255, 0, 0)
fireplace_brown = (139, 69, 19)  # Darker brown
fireplace_brown_light = (165, 100, 25)  # Lighter brown

class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = random.randint(20, 30)
        self.color = random.choice((orange, red, fireplace_brown_light))  # Use the lighter brown
        self.speed = random.uniform(1, 3)
        print(f"Particle created at ({self.x}, {self.y}) with color {self.color} and size {self.size}")

    def move(self):
        self.y -= self.speed

    def draw(self):
        pygame.draw.circle(win, self.color, (self.x, int(self.y)), self.size)
        print(f"Particle drawn at ({self.x}, {self.y}) with color {self.color}")

# Define main function
def main():
    particles = []
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Create new particles
        for _ in range(5):
            new_particle = Particle(random.randint(350, 450), height)
            particles.append(new_particle)
            print(f"New particle created at ({new_particle.x}, {new_particle.y})")

        # Move and draw particles
        for particle in particles:
            particle.move()
            particle.draw()
            print(f"Particle at ({particle.x}, {particle.y}) moved and drawn")

        # Remove particles that are out of the screen
        particles = [p for p in particles if p.y > 0]

        # Fill the background with black
        win.fill(black)

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(30)
        print("Frame updated")

if __name__ == "__main__":
    main()