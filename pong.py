import pygame
import sys

# Importation de Pygame
pygame.init()

# Constante de la fenêtre
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

# Création de l'écran
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Py-Pong")

# Constante des couleurs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

player1_pos = [5, SCREEN_HEIGHT // 2 - 25]
player2_pos = [SCREEN_WIDTH - 30, SCREEN_HEIGHT // 2 - 25]
ball_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]
ball_velocity = [2, 2]

# Initialisation des scores
player1_score = 0
player2_score = 0

# Boucle principale
while True:
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # Récupération des touches
    keys = pygame.key.get_pressed()

    if keys[pygame.K_z]:
        player1_pos[1] -= 5
    if keys[pygame.K_s]:
        player1_pos[1] += 5
    if keys[pygame.K_UP]:
        player2_pos[1] -= 5
    if keys[pygame.K_DOWN]:
        player2_pos[1] += 5

    # Réinitialisation de la partie
    if keys[pygame.K_r]:
        ball_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]
        ball_velocity = [0, 0]
        player1_score = 0
        player2_score = 0

    # Mise à jour de la position de la balle
    ball_pos[0] += ball_velocity[0]
    ball_pos[1] += ball_velocity[1]

    # Collision de la balle avec le haut et le bas
    if ball_pos[1] <= 0 or ball_pos[1] >= SCREEN_HEIGHT:
        ball_velocity[1] = -ball_velocity[1]

    # Collision avec les raquettes
    if (player1_pos[0] < ball_pos[0] < player1_pos[0] + 25 and player1_pos[1] < ball_pos[1] < player1_pos[1] + 50) or \
        (player2_pos[0] < ball_pos[0] < player2_pos[0] + 25 and player2_pos[1] < ball_pos[1] < player2_pos[1] + 50):
        ball_velocity[0] = -ball_velocity[0]

    # Mise à jour du score
    if ball_pos[0] <= 0:
        player2_score += 1
        ball_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]
    if ball_pos[0] >= SCREEN_WIDTH:
        player1_score += 1
        ball_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]


    # Effacement l'écran
    screen.fill(BLACK)

    # Affichage des raquettes et de la balle
    pygame.draw.rect(screen, WHITE, (player1_pos[0], player1_pos[1], 25, 50))
    pygame.draw.rect(screen, WHITE, (player2_pos[0], player2_pos[1], 25, 50))
    pygame.draw.circle(screen, WHITE, ball_pos, 10)

    # Affichage du score
    font = pygame.font.Font(None, 36)
    score_display = font.render(f"{player1_score} - {player2_score}", True, WHITE)
    screen.blit(score_display, (SCREEN_WIDTH // 2 - 50, 10))

    # Mise à jour de la fenêtre
    pygame.display.flip()

    # Limitation de la vitesse de la boucle
    pygame.time.Clock().tick(60)
