import pygame
import sys

pygame.init()
clock = pygame.time.Clock()

largeur, hauteur = 638, 320
screen = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Paramètres")
fond = pygame.image.load('img/fond.jpg').convert()
balle_image = pygame.image.load('img/balle.png').convert_alpha()
font = pygame.font.Font('font/elite.ttf', 16)

WHITE = (255, 255, 255)
GREY = (100, 100, 100)
BLACK = (0, 0, 0)
font = pygame.font.Font(None, 36)
small_font = pygame.font.Font(None, 24)

nombre_de_balles = 1
mode_reactivite = False

plus_balles_rect = pygame.Rect(420, 80, 50, 30)
moins_balles_rect = pygame.Rect(150, 80, 50, 30)
toggle_reactivite_rect = pygame.Rect(210, 140, 220, 50)
valider_rect = pygame.Rect(300, 240, 100, 40)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect(center=(x, y))
    surface.blit(textobj, textrect)

def configurer_settings():
    global nombre_de_balles, mode_reactivite

    parametres = True
    while parametres:
        screen.blit(fond, (0, 0))

        # Titre
        draw_text("Paramètres", font, BLACK, screen, largeur // 2,30)

        # Nombre de balles
        draw_text(f"Nombre de balles: {nombre_de_balles}", small_font, BLACK, screen, largeur // 2, 80)
        pygame.draw.rect(screen, GREY, plus_balles_rect)
        pygame.draw.rect(screen, GREY, moins_balles_rect)
        draw_text("+", small_font, BLACK, screen, plus_balles_rect.centerx, plus_balles_rect.centery)
        draw_text("-", small_font, BLACK, screen, moins_balles_rect.centerx, moins_balles_rect.centery)

        # Mode réactivité
        reactivite_text = "Activé" if mode_reactivite else "Désactivé"
        pygame.draw.rect(screen, GREY, toggle_reactivite_rect)
        draw_text(f"Mode réactivité: {reactivite_text}", small_font, BLACK, screen, largeur // 2, 160)

        # Bouton de validation
        pygame.draw.rect(screen, GREY, valider_rect)
        draw_text("Valider", small_font, BLACK, screen, valider_rect.centerx, valider_rect.centery)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if plus_balles_rect.collidepoint(event.pos) and nombre_de_balles < 100:
                    nombre_de_balles += 1
                elif moins_balles_rect.collidepoint(event.pos) and nombre_de_balles > 1:
                    nombre_de_balles -= 1
                elif toggle_reactivite_rect.collidepoint(event.pos):
                    mode_reactivite = not mode_reactivite
                elif valider_rect.collidepoint(event.pos):
                    parametres = False  

        
        pygame.display.update()
        clock.tick(60)

    # Retourner les paramètres configurés
    return {"nombre_de_balles": nombre_de_balles, "mode_reactivite": mode_reactivite}


if __name__ == "__main__":
    settings = configurer_settings()
    print("\nParamètres configurés :")
    print(f" - Nombre de balles : {settings['nombre_de_balles']}")
    print(f" - Mode réactivité activé : {'Oui' if settings['mode_reactivite'] else 'Non'}")
