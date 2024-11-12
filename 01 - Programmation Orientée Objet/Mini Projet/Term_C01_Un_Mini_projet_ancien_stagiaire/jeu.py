import pygame
import math
import settings
from random import *
import time

config = settings.configurer_settings()
nombre_de_balles = config["nombre_de_balles"] if not config["mode_reactivite"] else 1
mode_reactivite = config["mode_reactivite"]

pygame.init()
clock = pygame.time.Clock()

pygame.display.set_caption('Clicker | Appuyer sur SPACE pour retouner au menu')

largeur = 638
hauteur = 320
screen = pygame.display.set_mode((largeur, hauteur))

fond = pygame.image.load('img/fond.jpg').convert()
balle_image = pygame.image.load('img/balle.png').convert_alpha()
font = pygame.font.Font('font/elite.ttf', 16)

WHITE = pygame.Color(255, 255, 255)

score = 0
accuracy = 0
clicks = 0

class Balle:
    def __init__(self):
        self.reset_position()
    
    def reset_position(self):
        self.x = randint(0, largeur - 50)
        self.y = randint(0, hauteur - 50)
        self.angle = 2 * math.pi * random()
        
        speed = 8 if mode_reactivite else 5
        self.deltax = speed * math.cos(self.angle)
        self.deltay = speed * math.sin(self.angle)
        self.creation_time = time.time()  

    def est_au_bord(self):
        if (self.x > largeur - 50 and self.deltax > 0) or (self.x < 0 and self.deltax < 0):
            self.deltax = -self.deltax
        if (self.y > hauteur - 50 and self.deltay > 0) or (self.y < 0 and self.deltay < 0):
            self.deltay = -self.deltay

    def update_pos(self):
        self.x += self.deltax
        self.y += self.deltay
        self.est_au_bord()

    def estTouchee(self, pos):
        balle_rect = pygame.Rect(self.x, self.y, balle_image.get_width(), balle_image.get_height())
        return balle_rect.collidepoint(pos)

balles = [Balle() for _ in range(nombre_de_balles)]

continuer = True
while continuer:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            import menu
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            clicks += 1
            a_touche = False  
            
            for balle in balles[:]:  
                if balle.estTouchee(pos):
                   
                    if mode_reactivite:
                        elapsed_time = time.time() - balle.creation_time
                        if elapsed_time <= 1:  
                            score += 1
                            accuracy += 1
                        
                        balle.reset_position()
                    else:
                        
                        score += 1
                        accuracy += 1
                        balles.remove(balle) 
                    
                    a_touche = True
                    break
            if not a_touche:
                accuracy -= 1  
    
    for balle in balles:
        balle.update_pos()
        

        if mode_reactivite and (time.time() - balle.creation_time) > 1:
            balle.reset_position()

    screen.blit(fond, (0, 0))
    for balle in balles:
        screen.blit(balle_image, (balle.x, balle.y))

    AffichageScore = font.render(f'Score = {score}', True, WHITE)
    screen.blit(AffichageScore, (1, 300))

    if clicks == 0:
        AffichageAccuracy = font.render(f'Précision = 100%', True, WHITE)
    else:
        precision = max(0, min((accuracy / clicks) * 100, 100))
        AffichageAccuracy = font.render(f'Précision = {precision:.1f}%', True, WHITE)
    screen.blit(AffichageAccuracy, (1, 280))

    text = font.render('Projet NSI', True, WHITE)
    screen.blit(text, (490, 300))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
