import pygame
import constantes
from personajes import Sword, Spear

#Set la ventanita y nombre
ventana = pygame.display.set_mode((constantes.ANCHO, constantes.ALTO))
pygame.display.set_caption("RAWGAME")

#Clase Espadungi
espada = Sword(constantes.SW_POS[0], constantes.SW_POS[1])
lanza = Spear(constantes.S_POS[0], constantes.S_POS[1])

a_pres = False
d_pres = False
s_pres = False
w_pres = False

a_pres_s = False
d_pres_s = False
s_pres_s = False
w_pres_s = False

s_render = True

reloj = pygame.time.Clock()

#Running
run = True
while run == True:
    
    
    #Seteando los FPS
    reloj.tick(constantes.FPS)
    
    ventana.fill(constantes.BG)
    
    #Ejecuta el movimiento
    if a_pres == True:
        espada.movimiento(-constantes.VELOCIDAD, 0)
    if d_pres == True:
        espada.movimiento(constantes.VELOCIDAD, 0)
    if s_pres == True:
        espada.movimiento(0, constantes.VELOCIDAD)
    if w_pres == True:
        espada.movimiento(0, -constantes.VELOCIDAD)
        
    if a_pres_s == True:
        lanza.movimiento_s(-constantes.VELOCIDAD, 0)
    if d_pres_s == True:
        lanza.movimiento_s(constantes.VELOCIDAD, 0)
    if s_pres_s == True:
        lanza.movimiento_s(0, constantes.VELOCIDAD)
    if w_pres_s == True:
        lanza.movimiento_s(0, -constantes.VELOCIDAD)

 
    lanza.dibujar(ventana)
    espada.dibujar(ventana)

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            run = False

        #Cuando se presiona la tecla
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                # print("Izquierda")
                a_pres = True
                
            if event.key == pygame.K_d:
                # print("Derecha")
                d_pres = True
                
            if event.key == pygame.K_s:
                # print("Abajo")
                s_pres = True
                
            if event.key == pygame.K_w:
                # print("Arriba")
                w_pres = True
        
        #Cuando se deja de presionar        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                # print("Izquierda")
                a_pres = False
                
            if event.key == pygame.K_d:
                # print("Derecha")
                d_pres = False
                
            if event.key == pygame.K_s:
                # print("Abajo")
                s_pres = False
                
            if event.key == pygame.K_w:
                # print("Arriba")
                w_pres = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("Izquierda")
                a_pres_s = True
                
            if event.key == pygame.K_RIGHT:
                print("Derecha")
                d_pres_s = True
                
            if event.key == pygame.K_DOWN:
                print("Abajo")
                s_pres_s = True
                
            if event.key == pygame.K_UP:
                print("Arriba")
                w_pres_s = True
        
        #Cuando se deja de presionar        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                a_pres_s = False
                
            if event.key == pygame.K_RIGHT:
                d_pres_s = False
                
            if event.key == pygame.K_DOWN:
                s_pres_s = False
                
            if event.key == pygame.K_UP:
                w_pres_s = False
    pygame.display.update()    
pygame.quit()