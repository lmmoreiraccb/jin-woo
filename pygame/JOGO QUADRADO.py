import pygame
import sys
import random

# Inicia pygame
pygame.init()

# Configuration of the window
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Cuadrado asesino")

# Color of the background
background_color = (0, 0, 0)

# Size and initial position of the square
square_size = 50
x = width // 2 - square_size // 2
y = height // 2 - square_size // 2

# Speed of the square
speed = 5

# Create a class for the laser
class Laser:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 5
        self.height = 20
        self.speed = 10

    def move(self):
        self.y -= self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, self.width, self.height))

# Create a class for the targets
class Target:
    def __init__(self):
        self.x = random.randint(0, width - 20)
        self.y = random.randint(0, height // 2 - 20)
        self.width = 20
        self.height = 20
        self.speed = 2

    def move(self):
        self.y += self.speed
        if self.y > height - self.height or self.y < 0:
            self.speed *= -1

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, self.width, self.height))

# Initialize the score
score = 0

# Initialize the laser
laser = None

# Initialize the targets
targets = [Target() for _ in range(5)]

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the targets
    for target in targets:
        target.move()

        # Check if the target is outside the screen boundaries
        if target.x < 0 or target.x + target.width > width or target.y < 0 or target.y + target.height > height:
            targets.remove(target)
            targets.append(Target())
        
    # Detect keys pressed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        y -= speed # Move the square up
    if keys[pygame.K_DOWN]:
        y += speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_LEFT]:
        x -= speed
    
    # Check if the space key is pressed to shoot a laser
    if keys[pygame.K_SPACE]:
        if laser is None:
            laser = Laser(x + square_size // 2, y + square_size)

    # Move the laser
    if laser is not None:
        laser.move()

    # Move the targets
    for target in targets:
        target.move()

    # Check if the laser hits a target and add a point to the score
    if laser is not None:
        for target in targets:
            if (laser.x >= target.x and laser.x <= target.x + target.width and
                laser.y >= target.y and laser.y <= target.y + target.height):
                score += 1
                targets.remove(target)
                targets.append(Target())
                laser = None
                break

    # Check if the laser is off the screen
    if laser is not None and laser.y < 0:
        laser = None

    # Keep the square within the limits of the screen
    if x < 0:
        x = 0
    elif x + square_size > width:
        x = width - square_size
    if y < 0:
        y = 0
    elif y + square_size > height:
        y = height - square_size

    # Fill the background and draw the square, laser, and targets
    screen.fill(background_color)
    pygame.draw.rect(screen, (0, 0, 255), (x, y, square_size, square_size))
    if laser is not None:
        laser.draw(screen)
    for target in targets:
        target.draw(screen)

    # Display the score
    font = pygame.font.Font(None, 36)
    text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(text, (10, 10))

    # Initialize the game over flag
game_over = False

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the targets
    for target in targets:
        target.move()

        # Check if the target is outside the screen boundaries
        if target.x < 0 or target.x + target.width > width or target.y < 0 or target.y + target.height > height:
            targets.remove(target)
            targets.append(Target())

    # Detect keys pressed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        y -= speed # Move the square up
    if keys[pygame.K_DOWN]:
        y += speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_LEFT]:
        x -= speed

    # Check if the space key is pressed to shoot a laser
    if keys[pygame.K_SPACE]:
        if laser is None:
            laser = Laser(x + square_size // 2, y + square_size)

    # Move the laser
    if laser is not None:
        laser.move()

    # Move the targets
    for target in targets:
        target.move()

    # Check if the laser hits a target and add a point to the score
    if laser is not None:
        for target in targets:
            if (laser.x >= target.x and laser.x <= target.x + target.width and
                laser.y >= target.y and laser.y <= target.y + target.height):
                score += 1
                targets.remove(target)
                targets.append(Target())
                laser = None
                break

    # Check if the laser is off the screen
    if laser is not None and laser.y < 0:
        laser = None

    # Check if the blue square collides with a red square
    for target in targets:
        if (x < target.x + target.width and
            x + square_size > target.x and
            y < target.y + target.height and
            y + square_size > target.y):
            game_over = True
            break

    # Keep the square within the limits of the screen
    if x < 0:
        x = 0
    elif x + square_size > width:
        x = width - square_size
    if y < 0:
        y = 0
    elif y + square_size > height:
        y = height - square_size

    # Fill the background and draw the square, laser, and targets
    screen.fill(background_color)
    pygame.draw.rect(screen, (0, 0, 255), (x, y, square_size, square_size))
    if laser is not None:
        laser.draw(screen)
    for target in targets:
        target.draw(screen)

    # Display the score
    font = pygame.font.Font(None, 36)
    text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(text, (10, 10))

    # Display the game over message
    if game_over:
        font = pygame.font.Font(None, 48)
        text = font.render("Game Over!", True, (255, 255, 255))
        screen.blit(text, (width // 2 - text.get_width() // 2, height // 2 - text.get_height() // 2))
        pygame.time.wait(2000) # Pause for 2 seconds
        game_over = False # Reset the game over flag
        score = 0 # Reset the score
        laser = None # Reset the laser
        targets = [Target() for _ in range(5)] # Reset the targets

        

    # Update the screen
    pygame.display.flip()

    # Control the speed of the loop
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
sys.exit() 

    
