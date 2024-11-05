import pygame
import math
from random import *

# Initialisation de pygame
pygame.init()
clock = pygame.time.Clock()

# Renommage de la fenètre pygame
pygame.display.set_caption('Clicker | Appuyer sur SPACE pour quitter')
# Dimensions de la fenêtre
largeur = 638
hauteur = 320
screen = pygame.display.set_mode((largeur, hauteur))

# Chargement des images et de la police de caractères
fond = pygame.image.load('img/fond.jpg').convert()
balle_image = pygame.image.load('img/balle.png').convert_alpha()
font = pygame.font.Font('font/elite.ttf', 16)

# Couleur pour le texte
WHITE = pygame.Color(255, 255, 255)

# Initialisation du score
score = 0

# Création de la classe Balle
class Balle:
    def __init__(self):
        self.x = randint(0, largeur - 50)
        self.y = randint(0, hauteur - 50)
        self.angle = 2 * math.pi * random()
        self.deltax = 5 * math.cos(self.angle)
        self.deltay = 5 * math.sin(self.angle)

    def est_au_bord(self):
        if (self.x > largeur - 50 and self.deltax > 0) or (self.x < 0 and self.deltax < 0):
            self.deltax = -self.deltax
        elif (self.y > hauteur - 50 and self.deltay > 0) or (self.y < 0 and self.deltay < 0):
            self.deltay = -self.deltay

    def update_pos(self):
        self.x += self.deltax
        self.y += self.deltay
        self.est_au_bord()

    def estTouchee(self, pos):
        balle_rect = pygame.Rect(self.x, self.y, balle_image.get_width(), balle_image.get_height())
        return balle_rect.collidepoint(pos)

# Création de x balles
balles = [Balle() for _ in range(50)]

# Boucle principale du jeu
continuer = True
while continuer:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            continuer = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            for balle in balles[:]:  # Utilise une copie de la liste pour éviter les erreurs de modification en boucle
                if balle.estTouchee(pos):
                    score += 1
                    balles.remove(balle) 
                    break  # Si le break est présent, lorsque deux balles se superposent, une seule balle sera supprimée. 
                    	   #Si on retire le break, toutes les balles présentes à l'emplacement du clic seront supprimées .

    # Mettre à jour la position de chaque balle restante
    for balle in balles:
        balle.update_pos()

    # Affichage des objets à l'écran
    screen.blit(fond, (0, 0))
    for balle in balles:
        screen.blit(balle_image, (balle.x, balle.y))

    # Mise à jour du score
    AffichageScore = font.render(f'Score = {score}', True, WHITE)
    screen.blit(AffichageScore, (1, 300))

    # Texte du projet
    text = font.render('Projet NSI', True, WHITE)
    screen.blit(text, (490, 300))

    pygame.display.update()
    clock.tick(60)

