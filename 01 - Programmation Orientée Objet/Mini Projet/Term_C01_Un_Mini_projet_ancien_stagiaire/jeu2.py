import pygame
import math
from random import *


# Initialisation de pygame
pygame.init()
clock = pygame.time.Clock()

# Dimensions de la fenetre
largeur = 638
hauteur = 320
screen = pygame.display.set_mode((largeur, hauteur))


# Chargement des images et de la police de caractères
fond = pygame.image.load('img/fond.jpg').convert()
balle = pygame.image.load('img/balle.png').convert_alpha()
font = pygame.font.Font('font/elite.ttf', 16) 


# Texte qui sera affiché au bas de la fenetre
WHITE = pygame.Color(255, 255, 255)
text = font.render('Projet NSI', True, WHITE) 

# Création du score
score = 0 
AffchageScore = font.render('Score =',score, True, WHITE)

# Création de la classe Balle
class Balle:
	def __init__(self,x,y):
	# Coordonnees de la VITESSE initiale de la balle (générees aléatoirement)
		self.angle = 2*math.pi*random()
		self.deltax = 5*math.cos(self.angle)
		self.deltay = 5*math.sin(self.angle)

	def getX(self):
		return x
	
	def getY(self):
		return y
	
	def setX(self,valeurX):
		return valeurX
	
	def setY(self,valeurY):
		return valeurY
	
	def estTouchee(self) :
		if event.type == pygame.KEYDOWN and event.key == pygame.BUTTON_LEFT :
			global score 
			score += 1
			self.kill()
		
##################################################### A FINIR

	def est_au_bord(self):
		if (self.x>largeur-50 and self.deltax>0) or (self.x<0 and self.deltax<0):
			self.deltax = -self.deltax
		elif (self.y>hauteur-50 and self.deltay>0) or (self.y<0 and self.deltay<0):
			self.deltay = -self.deltay
	
	def update_pos(self) : 
		self.x += self.deltax
		self.y += self.deltay


x = random()*largeur-55
y = random()*hauteur-55
#  --------------------------------------------------------------------------
#  Boucle exécutée pendant toute la partie (Barre espace pour quitter le jeu)
#  --------------------------------------------------------------------------
continuer = True

while continuer:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			continuer = False
		if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
			continuer = False
						

	# Affichage des objets à l'écran 
	screen.blit(fond, (0,0))
	screen.blit(text, (490,300))
	screen.blit(AffchageScore, (1,300))
	screen.blit(balle, (x, y))


	pygame.display.update()
	clock.tick(60)


#  --------------------------------------------------------------------------
#                              Fin de la boucle 
#  --------------------------------------------------------------------------
