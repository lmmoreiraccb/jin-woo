import pygame
import sys

#Inicializar Pygame
pygame.init()

#Configuracion de la ventana
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("El cuadrado asesino")

#Color de fondo
background_color = (0, 0, 0)

#Tamaño y posicion inicialo del cuadrado

square_size = 50
x = width // 2 - square_size // 2
y = height // 2 - square_size // 2


#velocidad de movimiento del cuadrado
speed = 5


#Bucle principal del juego
running = True
while running:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        running = False

#Detectar teclas presionadas
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
                y -= speed # Mueve el cuadrado hacia arriba
        if keys[pygame.K_DOWN]:
                y += speed
        if keys[pygame.K_LEFT]:
                x -= speed
        if keys[pygame.K_RIGHT]:
                x += speed

# Mantener el cuadrado dentro de los limites superiores de la pantalla
        if x < 0:
                 x = 0
        elif x + square_size > width:
                x = width - square_size
        if y < 0:
                y = 0
        elif y + square_size > height:
                y = height - square_size


# Rellenar el fondo y dibujar el cuadrado
        screen.fill(background_color)
        pygame.draw.rect(screen, (255, 0, 0), (x, y, square_size, square_size))


#Actualiza la pantalla
        pygame.display. flip()

#Controlar la velocidad del bucle
        pygame.time.Clock() .tick(60)

#salir de pygame
pygame.quit()
sys.exit()