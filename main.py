import pygame

pygame.init()

timer = pygame.time.Clock()
fps = 60
red = (255,0,0)
black = (0,0,0)
white = (255,255,255)
orange = (255, 128, 0)
green = (0,255,0)
blue = (0,0,255)
purple = (255, 0 ,255)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
player_x = 340
ball_x=SCREEN_WIDTH/2
ball_y = SCREEN_HEIGHT - 40
board = [[5,5,5,5,5,5,5,5], [4,4,4,4,4,4,4,4], [3,3,3,3,3,3,3,3], [2,2,2,2,2,2,2,2], [1,1,1,1,1,1,1,1]]
colors = [red, orange, green, blue, purple]
speed = 8
player_direction = 0
active = False

#Initializes the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#Sets up the board
def draw_board(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            pygame.draw.rect(screen, colors[(board[i][j])-1], [j*100, i*40, 98 ,38])

run = True
while run:
    screen.fill(black)
    timer.tick(fps)
    draw_board(board)

    player = pygame.draw.rect(screen, red, [player_x, SCREEN_HEIGHT - 30, 120, 15], 0)
    ball = pygame.draw.circle(screen, white,[ball_x,ball_y], 10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

#Buttons to move left right
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        active = True
    elif keys[pygame.K_a]:
        player_direction = -1
    elif keys[pygame.K_d]:
        player_direction = 1
    else:
        player_direction = 0

    player_x += player_direction*speed

    pygame.display.flip()

pygame.quit()