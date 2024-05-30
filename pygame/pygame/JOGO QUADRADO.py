import pygame
import sys
import random

# Inicia pygame
pygame.init()

# Configuracion de la ventana
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Cuadrado asesino")

# Color del fondo
background_color = (0, 0, 0)

# tamaño y posizion inicial del cuadrado
square_size = 50
x = width // 2 - square_size // 2
y = height // 2 - square_size // 2

# velocidad del cuadrado
speed = 5

# crear lasser
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

# crear los objetivos
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

# iniciar el puntaje
score = 0

# iniciar el laser
laser = None

# iniciar los objetivos
targets = [Target() for _ in range(5)]

# loop del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # mueve los objetivos
    for target in targets:
        target.move()

        # revisa si los objetivos se salen de la pantalla
        if target.x < 0 or target.x + target.width > width or target.y < 0 or target.y + target.height > height:
            targets.remove(target)
            targets.append(Target())
        
    # detecta las teclas presionadas
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        y -= speed # mueve el cuadrado hacia arriba
    if keys[pygame.K_DOWN]:
        y += speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_LEFT]:
        x -= speed
    
    # revisa si la tecla esta presionada para disparar
    if keys[pygame.K_SPACE]:
        if laser is None:
            laser = Laser(x + square_size // 2, y + square_size)

    # mueve el laser
    if laser is not None:
        laser.move()

    # mueve los objetivos
    for target in targets:
        target.move()

    # revisa si el laser choco con un objetivo para aumentar el puntaje
    if laser is not None:
        for target in targets:
            if (laser.x >= target.x and laser.x <= target.x + target.width and
                laser.y >= target.y and laser.y <= target.y + target.height):
                score += 1
                targets.remove(target)
                targets.append(Target())
                laser = None
                break

    # revisa si el laser se salio de la pantalla
    if laser is not None and laser.y < 0:
        laser = None

    # mantiene el cuadrado dentro del area
    if x < 0:
        x = 0
    elif x + square_size > width:
        x = width - square_size
    if y < 0:
        y = 0
    elif y + square_size > height:
        y = height - square_size

    # llena el fondo y dibuja los cuadrados
    screen.fill(background_color)
    pygame.draw.rect(screen, (0, 0, 255), (x, y, square_size, square_size))
    if laser is not None:
        laser.draw(screen)
    for target in targets:
        target.draw(screen)

    # muestra el score
    font = pygame.font.Font(None, 36)
    text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(text, (10, 10))

    # inicia el mensaje de game over
game_over = False

# Mloop del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # mueve los objetivos
    for target in targets:
        target.move()

        # revisa si los objetivos salen de la pantalla
        if target.x < 0 or target.x + target.width > width or target.y < 0 or target.y + target.height > height:
            targets.remove(target)
            targets.append(Target())

    # detecta las teclas presionadas
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        y -= speed 
    if keys[pygame.K_DOWN]:
        y += speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_LEFT]:
        x -= speed

    
    if keys[pygame.K_SPACE]:
        if laser is None:
            laser = Laser(x + square_size // 2, y + square_size)

    
    if laser is not None:
        laser.move()

 
    for target in targets:
        target.move()

    
    if laser is not None:
        for target in targets:
            if (laser.x >= target.x and laser.x <= target.x + target.width and
                laser.y >= target.y and laser.y <= target.y + target.height):
                score += 1
                targets.remove(target)
                targets.append(Target())
                laser = None
                break

    if laser is not None and laser.y < 0:
        laser = None

    # revisa si el cuadrado azul choca con uno rojo
    for target in targets:
        if (x < target.x + target.width and
            x + square_size > target.x and
            y < target.y + target.height and
            y + square_size > target.y):
            game_over = True
            break

    
    if x < 0:
        x = 0
    elif x + square_size > width:
        x = width - square_size
    if y < 0:
        y = 0
    elif y + square_size > height:
        y = height - square_size

    screen.fill(background_color)
    pygame.draw.rect(screen, (0, 0, 255), (x, y, square_size, square_size))
    if laser is not None:
        laser.draw(screen)
    for target in targets:
        target.draw(screen)

    font = pygame.font.Font(None, 36)
    text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(text, (10, 10))

    # muestra el mensaje de game over
    if game_over:
        font = pygame.font.Font(None, 48)
        text = font.render("Game Over!", True, (255, 255, 255))
        screen.blit(text, (width // 2 - text.get_width() // 2, height // 2 - text.get_height() // 2))
        pygame.time.wait(2000) # Pause for 2 seconds
        game_over = False # Reset the game over flag
        score = 0 # Reset the score
        laser = None # Reset the laser
        targets = [Target() for _ in range(5)] # Reset the targets

        

    # actualiza la imagen
    pygame.display.flip()

    # controla la velocidad del bucle
    pygame.time.Clock().tick(60)

#cierra pygame
pygame.quit()
sys.exit() 

    
