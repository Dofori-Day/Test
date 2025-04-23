import pygame
import time
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Circle")

player_x = WIDTH // 2
player_y = HEIGHT // 2
player_speed = 5
circle_x, circle_y = random.randint(0, WIDTH - 50), random.randint(0, HEIGHT - 50)
score = 0
time_limit = 30  # seconds
start_time = time.time()
running = True

font = pygame.font.Font(None, 36)
catch_sound = pygame.mixer.Sound("catch.mp3")

while running:
    screen.fill(BLACK)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed
    
    player_x = max(0, min(WIDTH - 50, player_x))
    player_y = max(0, min(HEIGHT - 50, player_y))

    pygame.draw.rect(screen, BLUE, (player_x, player_y, 50, 50))
    pygame.draw.circle(screen, RED, (circle_x + 25, circle_y + 25), 25)

    if abs(player_x - circle_x) < 50 and abs(player_y - circle_y) < 50:
        score += 1
        catch_sound.play()
        circle_x, circle_y = random.randint(0, WIDTH - 50), random.randint(0, HEIGHT - 50)

    elapsed_time = time.time() - start_time
    if elapsed_time > time_limit:
        running = False

    score_text = font.render(f"Score: {score}", True, WHITE)
    timer_text = font.render(f"Time: {int(time_limit - elapsed_time)}s", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(timer_text, (10, 50))

    pygame.display.flip()
    pygame.time.Clock().tick(30)

screen.fill(BLACK)
game_over_text = font.render("Game Over!", True, WHITE)
final_score_text = font.render(f"Your Score: {score}", True, WHITE)
screen.blit(game_over_text, (WIDTH // 2 - 100, HEIGHT // 2 - 50))
screen.blit(final_score_text, (WIDTH // 2 - 120, HEIGHT // 2 + 10))
pygame.display.flip()
pygame.time.wait(3000)
pygame.quit()