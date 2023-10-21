from firework import *
import sys
import numpy as np

# Initialize Pygame
pygame.init()

# Set the dimensions of the window

screen = pygame.display.set_mode((width, height))

# Set the background color to black
background_color = (0, 0, 0)

# Main game loop
if __name__ == "__main__":
    yforces = np.arange(-1.25, -0.8, 0.05)
    crackers = [Cracker(screen, (255, 0, 0, 10)) for _ in range(15)]
    for cracker in crackers:
        yforce = choice(yforces)
        cracker.applyForce((0, yforce))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill the screen with the background color
        screen.fill(background_color)

        # Other game logic and drawing would go here

        for cracker in crackers:
            cracker.update()
        for cracker in crackers:
            cracker.show()
        crackers = [ cracker for cracker in crackers if cracker.lifespan >= 0]

        if len(crackers) == 0:
            break
        # Update the display
        pygame.display.flip()
        pygame.time.delay(20)

    # Quit Pygame
    pygame.quit()
    sys.exit()
