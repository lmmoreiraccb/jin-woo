import pygame
import sys
pygame.init()



screen_width = 600
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

estado = "instrucciones"

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type== pygame.KEYDOWN:
            if event.key == pygame.K_q:
                print(estado)
                if estado == "instrucciones":
                    estado = "Pantalla inicial"
                elif estado == "Pantalla inicial":
                      estado = "Pantalla 2"
                elif estado == "Pantalla 2": 
                    estado = "Pantalla 3"
            if event.key == pygame.K_1:
                if estado == "Pantalla 3":
                    estado = "Pantalla 4"
            if event.key == pygame.K_2:
                if estado == "Pantalla 3":
                    estado = "Pantalla 6"
            if event.key == pygame.K_q:
                if estado == "Pantalla 4":
                     estado = "Pantalla 5"
                elif estado == "Pantalla 5":
                    estado = "Pantalla 7"
                elif estado == "Pantalla 6":
                     estado = "Pantalla 7"
            if event.key == pygame.K_1:
                if estado == "Pantalla 7":
                    estado = "luchar"
            if event.key == pygame.K_2:
                if estado == "Pantalla 7":
                    estado = "noluchar"
            if event.key == pygame.K_q:
                if estado == "luchar":
                    estado = "luchar1"
                elif estado == "luchar1":
                   estado = "opciondaga1"
                if estado == "noluchar":
                    estado = "noluchar1"
            if event.key == pygame.K_1:
                if estado == "opciondaga1":
                    estado = "luchar2"
            if event.key == pygame.K_2:
                if estado == "opciondaga1":
                    estado = "nonluchar" 
            if event.key == pygame.K_q:        
                if estado == "nonluchar":
                    estado = "nonluchar2"
                if estado == "luchar2":
                    estado = "luchar3"
                if estado == "luchar3":
                    estado = "luchar4"
                if estado == "noluchar1":
                    estado = "opnoluchar1"
            if event.key == pygame.K_1:
                if estado == "opnoluchar1":
                    estado = "redencion"
            if event.key == pygame.K_2:
                if estado == "opnoluchar1":
                    estado = "reflexion1"
            if event.key == pygame.K_q:
                if estado == "reflexion1":
                    estado = "reflexion2"
            
                          

                
                 
                
                    
                
     

    if estado == "instrucciones":
        instrucciones = pygame.image.load("instrucciones.png")
        screen.blit(instrucciones,(0,0))
        pygame.display.update()
                   
    elif estado == "Pantalla inicial":
        image = pygame.image.load("inicio2.png")
        image=pygame.transform.scale(image, (screen_width, screen_height))
        screen.blit(image,(0,0))
        pygame.display.update()        

    elif estado == "Pantalla 2":
        image1 = pygame.image.load("Unsabio.png")
        screen.blit(image1,(0,0))
        pygame.display.update()

    elif estado == "Pantalla 3":
         image2 = pygame.image.load("Image2.png")
         screen.blit(image2,(0,0))
         pygame.display.update()

    elif estado == "Pantalla 4":
         sabioop1 = pygame.image.load("sabioop1.png")
         screen.blit(sabioop1,(0,0))
         pygame.display.update()
         
    elif estado == "Pantalla 5":
         sabioop12 = pygame.image.load("sabioop12.png")
         screen.blit(sabioop12,(0,0))
         pygame.display.update()

    elif estado == "Pantalla 6":
         sabioop2 = pygame.image.load("sabioop2.png")
         screen.blit(sabioop2, (0,0))
         pygame.display.update()
         
    elif estado == "Pantalla 7":
        desafio = pygame.image.load("desafio1.png")
        screen.blit(desafio,(0,0))
        pygame.display.update()

    elif estado == "luchar":
        luchar = pygame.image.load("luchar.png")
        screen.blit(luchar,(0,0))
        pygame.display.update()

    elif estado == "luchar1":
        luchar1 = pygame.image.load("luchar1.png")
        screen.blit(luchar1,(0,0))
        pygame.display.update()

    elif estado == "noluchar":
        noluchar = pygame.image.load("noluchar.png")
        screen.blit(noluchar,(0,0))
        pygame.display.update()

    elif estado == "noluchar1":
        noluchar1 = pygame.image.load("noluchar1.png")
        screen.blit(noluchar1,(0,0))
        pygame.display.update()

    elif estado == "opciondaga1":
        opciondaga1 = pygame.image.load("opciondaga1.png")
        screen.blit(opciondaga1,(0,0))
        pygame.display.update()

    elif estado == "nonluchar":
        nonluchar = pygame.image.load("nonluchar.png")
        screen.blit(nonluchar,(0,0))
        pygame.display.update()

    elif estado == "nonluchar2":
        nonluchar2 = pygame.image.load("nonluchar2.png")
        screen.blit(nonluchar2,(0,0))
        pygame.display.update()
           
    
    elif estado =="luchar2":
        luchar2 = pygame.image.load("luchar2.png")
        screen.blit(luchar2,(0,0))
        pygame.display.update()

    elif estado == "luchar3":
        luchar3 = pygame.image.load("luchar3.png")
        screen.blit(luchar3,(0,0))
        pygame.display.update()

    elif estado == "luchar4":
        luchar4 = pygame.image.load("luchar4.png")
        screen.blit(luchar4,(0,0))
        pygame.display.update()
        
    elif estado == "opnoluchar1":
        opnoluchar1 = pygame.image.load("opnoluchar1.png")
        screen.blit(opnoluchar1,(0,0))
        pygame.display.update()
    
    elif estado == "redencion":
        redencion = pygame.image.load("redencion.png")
        screen.blit(redencion,(0,0))
        pygame.display.update()

    elif estado == "reflexion1":
        reflexion1 = pygame.image.load("reflexion1.png")
        screen.blit(reflexion1,(0,0))
        pygame.display.update()

    elif estado == "reflexion2":
        reflexion2 = pygame.image.load("reflexion2.png")
        screen.blit(reflexion2,(0,0))
        pygame.display.update()

    

 
    
        


    pygame.display.flip()    

#cierra pygame
pygame.quit()
sys.exit() 





