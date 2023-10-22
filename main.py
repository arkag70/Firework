from firework import *
import sys
import numpy as np
BATCHES = 10
yforces = np.arange(-1.25, -0.8, 0.05)

def createCracker(crackers, color):
    crackers.append(Cracker(screen, color))
    yforce = choice(yforces)
    crackers[-1].applyForce((0, yforce))

# Initialize Pygame
pygame.init()

# Set the dimensions of the window

screen = pygame.display.set_mode((width, height))

# Set the background color to black
background_color = (0, 0, 0, 100)

# Main game loop
if __name__ == "__main__":

    batch = 0
    counts = list(range(20, 100, 20))
    while batch < BATCHES:
        count = 0
        print(f"Batch {batch + 1}")
        crackers = [Cracker(screen, choice(colors))]

        for cracker in crackers:
            yforce = choice(yforces)
            cracker.applyForce((0, yforce))

        running = True
        while running:
            count += 1

            if count == choice(counts):
                createCracker(crackers, choice(colors))
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Fill the screen with the background color
            screen.fill(background_color)

            # Other game logic and drawing would go here

            for cracker in crackers:
                cracker.update()
                cracker.show()
            crackers = [ cracker for cracker in crackers if cracker.lifespan >= 0]

            if len(crackers) == 0:
                batch += 1
                break
            # Update the display
            pygame.display.flip()
            pygame.time.delay(20)

    # Quit Pygame
    pygame.quit()
    sys.exit()
