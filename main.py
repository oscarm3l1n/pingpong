import pygame
import sys
import random

def check_collision():
    if ball_rect.colliderect(left_racket_rect) or ball_rect.colliderect(right_racket_rect):
        return True
    return False

def change_direction():
    global speedx
    global speedy

    speedx *= -1
    speedy = random.choice(directions)

def score_display():
    score_surface = game_font.render(f"{left_score} - {right_score}", True, (255, 255, 255))
    score_rect = score_surface.get_rect(center = (width / 2, height - 100))
    screen.blit(score_surface, score_rect)

r = 255
g = 160
b = 125

width = height = 800
rectangle_size = (50, 200)

# General setup
pygame.init()
clock = pygame.time.Clock()
game_font = pygame.font.Font("04B_19.TTF", 40)

# Create the display surface
screen = pygame.display.set_mode((width, height))

# Game variables
speedx = 5
speedy = 0
ball_move = 0
directions = [1, 2, 3, 4, 5]

# Ball
ball_surf = pygame.Surface([25, 25])
ball_surf.fill((125,125,255))
ball_rect = ball_surf.get_rect(center = (width/2, height/2))

# Left racket
left_racket_surf = pygame.Surface([50, 200])
left_racket_surf.fill((0,0,0))
left_racket_rect = left_racket_surf.get_rect(midleft = (0, height/2))
left_up = False
left_down = False
left_score = 0

# Right racket
right_racket_surf = pygame.Surface([50, 200])
right_racket_surf.fill((0,0,0))
right_racket_rect = right_racket_surf.get_rect(midleft = (width - 50, height/2))
right_up = False
right_down = False
right_score = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(1)
        # Key pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                right_up = True
            if event.key == pygame.K_DOWN:
                right_down = True
            if event.key == pygame.K_w:
                left_up  = True
            if event.key == pygame.K_s:
                left_down = True
        # Key released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                right_up = False
            if event.key == pygame.K_DOWN:
                right_down = False
            if event.key == pygame.K_w:
                left_up  = False
            if event.key == pygame.K_s:
                left_down = False

    # Fill screen
    screen.fill((r, g, b))

    score_display()

    # Right
    if right_up:
        if right_racket_rect.top > 0: 
            right_racket_rect.centery -= 5
    if right_down:
        if right_racket_rect.bottom < height :
            right_racket_rect.centery += 5

    # Left
    if left_up:
        if left_racket_rect.top > 0:
            left_racket_rect.centery -= 5
    if left_down:
        if left_racket_rect.bottom < height:
            left_racket_rect.centery += 5

    # Ball
    if check_collision():
        change_direction()
    ball_rect.centerx -= speedx
    ball_rect.centery -= speedy
    if ball_rect.centerx <= 0:
        # left side scores
        left_score += 1
        ball_rect.centerx = width / 2
        ball_rect.centery = height / 2
        speedy = 0
    if ball_rect.centerx >= width:
        # right side scores
        right_score += 1
        ball_rect.centerx = width / 2
        ball_rect.centery = height / 2
        speedy = 0
    screen.blit(ball_surf, ball_rect)

    # Check if ball goes outside of map
    if ball_rect.centery <= 0:
        speedy *= -1
    if ball_rect.centery >= height:
        speedy *= -1

    # Left racket
    screen.blit(left_racket_surf, left_racket_rect)

    # Right racket
    screen.blit(right_racket_surf, right_racket_rect)

    pygame.display.flip()
    # 60 FPS
    clock.tick(60)