import pygame
from pygame.locals import *
import random

pygame.init()

GAME_RES = WIDTH, HEIGHT = 1080, 1920
FPS = 60
GAME_TITLE = 'Flappy Bird'

window = pygame.display.set_mode(GAME_RES, HWACCEL|HWSURFACE|DOUBLEBUF)
pygame.display.set_caption(GAME_TITLE)
clock = pygame.time.Clock()
difficulty = 1

# Game Values

background_image = pygame.image.load("./images/Background.png")

class Ghost:

    player_sprite = pygame.image.load('./images/Ghost.png')
    player_rect = player_sprite.get_rect()
    player_x = WIDTH / 6
    player_y = HEIGHT / 2 - player_rect.height / 2
    speed_up = HEIGHT / 10
    speed_down = 15


    def bounce(self):
        for i in range(10):
            self.player_y -= self.speed_up / 10

    def isPressed(self):
        if pygame.mouse.get_pressed()[0]:
            return True

    def isDead(self):
        if self.player_y < 0:
            return True
        if self.player_y > (HEIGHT - self.player_rect.height):
            return True

ghost = Ghost()

def physics():
    ghost.player_y += ghost.speed_down





class Walls:

    wall_sprite_down = pygame.image.load('./images/Wall.png')
    wall_rect_down = wall_sprite_down.get_rect()
    wall_x_down = WIDTH - 300
    wall_y_down = random.randint((HEIGHT / 2), (HEIGHT - 400))

    wall_sprite_up = pygame.image.load('./images/Wall_up.png')
    wall_rect_up = wall_sprite_up.get_rect()
    wall_x_up = wall_x_down
    wall_y_up = wall_y_down - wall_rect_up.height - 700

    list_of_walls_down = []
    list_of_walls_up = []

    down_y, down_x = wall_y_down, wall_x_down
    list_of_walls_down.insert(0, [down_y, down_x])

    up_y, up_x = wall_y_up, wall_x_up
    list_of_walls_up.insert(0, [up_y, up_x])

    def draw(self):
        for block in self.list_of_walls_down[::-1]:
            pygame.Surface.blit(window, self.wall_sprite_down, (block[1], block[0]))
        for block in self.list_of_walls_up[::-1]:
            pygame.Surface.blit(window, self.wall_sprite_up, (block[1], block[0]))


wall = Walls()

# End of Game Values

# Game loop
game_ended = False
while not game_ended:

    # Event handling
    for event in pygame.event.get():
        if event.type == QUIT:
            game_ended  = True
            break
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                game_ended  = True
                break
        if ghost.isPressed():
            ghost.bounce()
            break

    if ghost.isDead():
        game_ended = True

    # Walls Moving


    # Game logic
    physics()

    # Fill Background
    window.blit(background_image, [0, 0])

    # Ghost Drawing
    pygame.Surface.blit(window, ghost.player_sprite, (ghost.player_x, ghost.player_y))

    # Walls Drawing
    wall.draw()

    # Display Update
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
exit(0)
