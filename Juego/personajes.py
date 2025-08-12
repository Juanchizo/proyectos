import pygame
import constantes
import math
pygame.font.init()

class Circulo:
    def __init__(self):
        self.radio = constantes.RADIO
        self.vida = 100

class Sword():
    def __init__(self, x_sw, y_sw):
        self.color = (255, 0, 0)
        self.centro = [x_sw, y_sw]
        self.sword_img = pygame.image.load("src/espada.png")
        self.sword_img = pygame.transform.scale(self.sword_img, (65, 65))
        self.sword_img = pygame.transform.rotate(self.sword_img, -45)
        self.radio = constantes.RADIO
        self.vida = constantes.VIDA
        self.recta_sw = None

    def movimiento(self, x_mov, y_mov):
        self.centro[0] += x_mov
        self.centro[1] += y_mov
    
    def dibujar(self, vent):
        pygame.draw.circle(vent, self.color, (self.centro[0], self.centro[1]), self.radio)
        
        font = pygame.font.Font(None, 35)
        text = font.render(str(self.vida), True, (255, 255, 255))
        border_text = font.render(str(self.vida), True, (0, 0, 0))
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            vent.blit(border_text, text.get_rect(center=(self.centro[0]+dx, self.centro[1]+dy)))
        text_rect = text.get_rect(center=(self.centro[0], self.centro[1]))
        vent.blit(text, text_rect)



class Spear():
    def __init__(self, x_s, y_s):
        self.radio = constantes.RADIO
        self.vida = constantes.VIDA
        self.xy_spear = [x_s, y_s]
        self.xy_s = (self.xy_spear[0], self.xy_spear[1])
        self.visible = True
        self.recta = None
        
    def movimiento_s(self, x_mov, y_mov):
        self.xy_spear[0] += x_mov
        self.xy_spear[1] += y_mov
        self.xy_s = (self.xy_spear[0], self.xy_spear[1])
        
    def dibujar(self, vent):
        if not self.visible:
            return
        font_s = pygame.font.Font(None, 35)
        
        render = pygame.draw.circle(vent, (0, 255, 0), self.xy_s, self.radio)
        
        text_s = font_s.render(str(self.vida), True, (255, 255, 255))
        border_text_s = font_s.render(str(self.vida), True, (0, 0, 0))
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            vent.blit(border_text_s, text_s.get_rect(center=(self.xy_spear[0]+dx, self.xy_spear[1]+dy)))
        text_rect_s = text_s.get_rect(center=self.xy_s)
        vent.blit(text_s, text_rect_s)
        
        self.recta = render