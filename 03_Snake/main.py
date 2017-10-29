import pygame
from pygame.locals import *
import random

pygame.init()

GAME_RES = WIDTH, HEIGHT = 800, 600
FPS = 10
GAME_TITLE = 'Snake - MarconiGames'

window = pygame.display.set_mode(GAME_RES, HWACCEL|HWSURFACE|DOUBLEBUF)
pygame.display.set_caption(GAME_TITLE)
clock = pygame.time.Clock()

# Game Values

background_color = (150, 150, 150) # RGB value

# Class for representing the snake
class Snake:

    # Initialization methon
    def __init__(self):

        # Sprite loading
        self.block_sprite = pygame.image.load('./images/snake_block.png')
        self.head_sprite = pygame.image.load('./images/snake_head.png')
        self.rect = self.block_sprite.get_rect()

        # Current coords and previous coordinates variables
        # initialized to these values
        self.curr_x = self.rect.width * 3
        self.curr_y = HEIGHT // 2 - self.rect.height // 2
        self.last_x = None
        self.last_y = None

        # List representing snake's tail
        self.tail = []

        self.direction = 'right'
        self.speed = 0.6

    def move(self):
        # Called every frame, it's responsible for snake's movement
        self.last_x, self.last_y = self.curr_x, self.curr_y

        # Move the snake accordingly to the direction
        if self.direction == 'up':
            self.curr_y -= self.rect.height * self.speed
        if self.direction == 'down':
            self.curr_y += self.rect.height * self.speed
        if self.direction == 'left':
            self.curr_x -= self.rect.width * self.speed
        if self.direction == 'right':
            self.curr_x += self.rect.width * self.speed

        # Handle going on walls
        if self.curr_x > WIDTH:
            self.curr_x = -1 * self.rect.width
        if self.curr_x + self.rect.width < 0:
            self.curr_x = WIDTH
        if self.curr_y > HEIGHT:
            self.curr_y = -1 * self.rect.height
        if self.curr_y + self.rect.height < 0:
            self.curr_y = HEIGHT

        # Drop the last block of tail and create a new one
        # at index 0, simulating tail's movement
        if len(self.tail) > 0:
            del self.tail[len(self.tail)-1]
            self.add_block()

        # Check if snake is on top of an apple
        # and do stuff accordingly
        if self.check_if_eating():
            drop_new_apple()
            self.add_block()

    def draw(self):
        # Simply draw the snake onto screen, with drawing
        # tail in reverse order to make it cooler to see
        for block in self.tail[::-1]:
            pygame.Surface.blit(window, self.block_sprite, (block[0], block[1]))
        pygame.Surface.blit(window, self.head_sprite, (self.curr_x, self.curr_y))

    def add_block(self):
        # Function responsible for handling snake's growing up
        x, y = self.last_x, self.last_y
        self.tail.insert(0, [x, y])

    def check_if_eating(self):
        # Function for checking if he is on top of the apple or not
        if self.curr_x + self.rect.width >= apple_x and \
           self.curr_x <= apple_x + apple_rect.width and \
           self.curr_y + self.rect.height >= apple_y and \
           self.curr_y <= apple_y + apple_rect.height:
            return True
        else:
            return False

snake = Snake()

# Apple sprite and initial properties
apple_sprite = pygame.image.load('./images/apple.png')
apple_rect = apple_sprite.get_rect()
apple_x = random.randint(0, WIDTH - apple_rect.width)
apple_y = random.randint(0, HEIGHT - apple_rect.height)

def drop_new_apple():
    # Function for dropping a new one if the existing one is just eaten
    global apple_x, apple_y
    apple_x = WIDTH // apple_rect.width * random.randint(0, apple_rect.width)
    apple_y = HEIGHT // apple_rect.height * random.randint(0, apple_rect.height)

# End of Game Values

# Game loop
game_ended = False
while not game_ended:

    ##### Event Handling
    for event in pygame.event.get():
        if event.type == QUIT:
            game_ended  = True
            break
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                game_ended  = True
                break

            # Snake direction handling
            if event.key == K_w:
                snake.direction = 'up'
            if event.key == K_s:
                snake.direction = 'down'
            if event.key == K_a:
                snake.direction = 'left'
            if event.key == K_d:
                snake.direction = 'right'

    ##### Game Logic
    snake.move()

    ##### Display Rendering
    # Drawing the background-color
    pygame.Surface.fill(window, background_color)

    # Drawing the apple
    pygame.Surface.blit(window, apple_sprite, (apple_x, apple_y))

    # Drawing the snake
    snake.draw()

    ##### Display Update
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
exit(0)
