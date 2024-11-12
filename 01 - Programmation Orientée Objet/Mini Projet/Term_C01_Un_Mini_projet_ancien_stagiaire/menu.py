import pygame
import settings  


pygame.init()
clock = pygame.time.Clock()


pygame.display.set_caption('Clicker | Appuyer sur SPACE pour quitter')

largeur = 638
hauteur = 320
screen = pygame.display.set_mode((largeur, hauteur))


fond = pygame.image.load('img/fond.jpg').convert()
balle_image = pygame.image.load('img/balle.png').convert_alpha()
font = pygame.font.Font('font/elite.ttf', 16)
fontTitle = pygame.font.Font('font/elite.ttf', 40)

WHITE = pygame.Color(255, 255, 255)
GREY = pygame.Color(100, 100, 100)


button_width, button_height = 200, 50
start_button_rect = pygame.Rect(largeur // 2 - button_width // 2, hauteur // 2 - button_height - 10, button_width, button_height)
quit_button_rect = pygame.Rect(largeur // 2 - button_width // 2, hauteur // 2 + 10, button_width, button_height)

settings_button_rect = pygame.Rect(10, hauteur - button_height - 10, button_width, button_height)

configuration = {"nombre_de_balles": 1, "mode_reactivite": False}  

continuer = True
while continuer:
    screen.blit(fond, (0, 0))  

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            continuer = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if start_button_rect.collidepoint(event.pos):
                try:
                    import jeu
                    jeu.lancer_jeu(configuration)  
                except AttributeError:
                    print("Erreur : Assurez-vous que jeu.py contient une fonction 'lancer_jeu'")
            elif quit_button_rect.collidepoint(event.pos):
                continuer = False  
            elif settings_button_rect.collidepoint(event.pos):
                configuration = settings.configurer_settings()  

    pygame.draw.rect(screen, GREY, start_button_rect)
    pygame.draw.rect(screen, GREY, quit_button_rect)
    pygame.draw.rect(screen, GREY, settings_button_rect)

    start_text = font.render('Lancer une partie', True, WHITE)
    quit_text = font.render('Quitter le jeu', True, WHITE)
    settings_text = font.render('Paramètres', True, WHITE)
    screen.blit(start_text, (start_button_rect.x + (button_width - start_text.get_width()) // 2,
                             start_button_rect.y + (button_height - start_text.get_height()) // 2))
    screen.blit(quit_text, (quit_button_rect.x + (button_width - quit_text.get_width()) // 2,
                            quit_button_rect.y + (button_height - quit_text.get_height()) // 2))
    screen.blit(settings_text, (settings_button_rect.x + (button_width - settings_text.get_width()) // 2,
                                settings_button_rect.y + (button_height - settings_text.get_height()) // 2))

    text = font.render('Projet NSI', True, WHITE)
    title = fontTitle.render("Clicker", True, WHITE)
    screen.blit(text, (490, 300))
    screen.blit(title, (230, 50))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
