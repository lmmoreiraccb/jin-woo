import pygame
import sys
pygame.init()

screen_width = 600
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

estado = "instrucciones"
def cargar(nombre):
    img = pygame.image.load(nombre)
    screen.blit(img, (0,0))
    pygame.display.update()

# Mapeo de estados y teclas a nuevos estados
state_transitions = {
    ('instrucciones', pygame.K_q): "Pantalla inicial",
    ('Pantalla inicial', pygame.K_q): "Pantalla 2",
    ('Pantalla 2', pygame.K_q): "Pantalla 3",
    ('Pantalla 3', pygame.K_1): "Pantalla 4",
    ('Pantalla 3', pygame.K_2): "Pantalla 6",
    ('Pantalla 4', pygame.K_q): "Pantalla 5",
    ('Pantalla 5', pygame.K_q): "Pantalla 7",
    ('Pantalla 6', pygame.K_q): "Pantalla 7",
    ('Pantalla 7', pygame.K_1): "luchar",
    ('Pantalla 7', pygame.K_2): "noluchar",
    ('luchar', pygame.K_q): "luchar1",
    ('luchar1', pygame.K_q): "opciondaga1",
    ('noluchar', pygame.K_q): "noluchar1",
    ('opciondaga1', pygame.K_1): "luchar2",
    ('opciondaga1', pygame.K_2): "nonluchar",
    ('nonluchar', pygame.K_q): "nonluchar2",
    ('luchar2', pygame.K_q): "luchar3",
    ('luchar3', pygame.K_q): "luchar4",
    ('noluchar1', pygame.K_q): "opnoluchar1",
    ('opnoluchar1', pygame.K_1): "redencion",
    ('opnoluchar1', pygame.K_2): "reflexion1",
    ('reflexion1', pygame.K_q): "reflexion2"
}
# Inicializar Pygame y el estado
pygame.init()
running = True
estado = "instrucciones"

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            # Obtén el nuevo estado usando el mapeo de estados y teclas
            new_state = state_transitions.get((estado, event.key))
            if new_state:
                print(new_state)
                estado = new_state
          
    if estado == "instrucciones":
        cargar("instrucciones.png")        
                   
    elif estado == "Pantalla inicial":
        image = pygame.image.load("inicio2.png")
        image=pygame.transform.scale(image, (screen_width, screen_height))
        screen.blit(image,(0,0))        

    elif estado == "Pantalla 2":
        cargar("Unsabio.png")
        
    elif estado == "Pantalla 3":
         cargar("Image2.png")
         
    elif estado == "Pantalla 4":
         cargar("sabioop1.png")
               
    elif estado == "Pantalla 5":
         cargar("sabioop12.png")
         
    elif estado == "Pantalla 6":
         cargar("sabioop2.png")
                
    elif estado == "Pantalla 7":
        cargar("desafio1.png")
       
    elif estado == "luchar":
        cargar("luchar.png")
        
    elif estado == "luchar1":
        cargar("luchar1.png")
        
    elif estado == "noluchar":
        cargar("noluchar.png")

    elif estado == "noluchar1":
        cargar("noluchar1.png")
        
    elif estado == "opciondaga1":
        cargar("opciondaga1.png")
        
    elif estado == "nonluchar":
        cargar("nonluchar.png")
        
    elif estado == "nonluchar2":
        cargar("nonluchar2.png")
           
    elif estado =="luchar2":
        cargar("luchar2.png")
        
    elif estado == "luchar3":
        cargar("luchar3.png")
        
    elif estado == "luchar4":
        cargar("luchar4.png")
               
    elif estado == "opnoluchar1":
        cargar("opnoluchar1.png")
           
    elif estado == "redencion":
        cargar("redencion.png")
        
    elif estado == "reflexion1":
        cargar("reflexion1.png")       
    
    elif estado == "reflexion2":
        cargar("reflexion2.png")
        
    pygame.display.flip()    
#cierra pygame
pygame.quit()
sys.exit() 
#de 210 a 129
#-81 lineas de codigo




