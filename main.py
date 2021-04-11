import pygame
import os

WIDTH, HEIGHT = 900, 500
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Battleship")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

VELOCITY = 2
FPS = 60

SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40
BORDER = pygame.Rect(WIDTH/2-5, 0, 10, HEIGHT)



SPACESHIP1_IMAGE = pygame.image.load(
    os.path.join('Assets', 'spaceship_yellow.png'))
SPACESHIP1 = pygame.transform.rotate(pygame.transform.scale(
    SPACESHIP1_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)
pygame.transform.rotate

SPACESHIP2_IMAGE = pygame.image.load(
    os.path.join('Assets', 'spaceship_red.png'))
SPACESHIP2 = pygame.transform.rotate(pygame.transform.scale(
    SPACESHIP2_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)


def draw_window(player1_spaceship, player2_spaceship):
    WINDOW.fill(WHITE)
    pygame.draw.rect(WINDOW, BLACK, BORDER)
    WINDOW.blit(SPACESHIP1, (player1_spaceship.x, player1_spaceship.y))
    WINDOW.blit(SPACESHIP2, (player2_spaceship.x, player2_spaceship.y))
    pygame.display.update()


def player1_movement(keys_pressed, player1_spaceship):
    if keys_pressed[pygame.K_a] and player1_spaceship.x - VELOCITY > 0:
        player1_spaceship.x -= VELOCITY

    if keys_pressed[pygame.K_d] and player1_spaceship.x + VELOCITY + player1_spaceship.width < BORDER.x: 
        player1_spaceship.x += VELOCITY

    if keys_pressed[pygame.K_w] and player1_spaceship.y - VELOCITY > 0: 
        player1_spaceship.y -= VELOCITY

    if keys_pressed[pygame.K_s] and player1_spaceship.y + VELOCITY + player1_spaceship.height < HEIGHT-15: 
        player1_spaceship.y += VELOCITY


def player2_movement(keys_pressed, player2_spaceship):
    if keys_pressed[pygame.K_LEFT] and player2_spaceship.x - VELOCITY > BORDER.x + BORDER.width:
        player2_spaceship.x -= VELOCITY

    if keys_pressed[pygame.K_RIGHT] and player2_spaceship.x + VELOCITY + player2_spaceship.width < WIDTH: 
        player2_spaceship.x += VELOCITY

    if keys_pressed[pygame.K_UP] and player2_spaceship.y - VELOCITY > 0: 
        player2_spaceship.y -= VELOCITY

    if keys_pressed[pygame.K_DOWN] and player2_spaceship.y + VELOCITY + player2_spaceship.height < HEIGHT-15: 
        player2_spaceship.y += VELOCITY


def main():
    player1_spaceship = pygame.Rect(
        100, 240, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    player2_spaceship = pygame.Rect(
        700, 240, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    clock = pygame.time.Clock()
    running = True

    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys_pressed = pygame.key.get_pressed()
        player1_movement(keys_pressed, player1_spaceship)
        player2_movement(keys_pressed, player2_spaceship)


        draw_window(player1_spaceship, player2_spaceship)
        
    pygame.quit()



if __name__ == "__main__":
    main()
