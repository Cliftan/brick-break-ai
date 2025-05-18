import pygame
import random

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
ball_x_direction = 0
ball_y_direction = 0
ball_x_speed = 4
ball_y_speed = 4
board = [[5,5,5,5,5,5,5,5], [4,4,4,4,4,4,4,4], [3,3,3,3,3,3,3,3], [2,2,2,2,2,2,2,2], [1,1,1,1,1,1,1,1]]
colors = [red, orange, green, blue, purple]
speed = 8
player_direction = 0
active = False

#Initializes the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#Sets up the board
def draw_board(board):
    board_squares = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] > 0:   
                piece = pygame.draw.rect(screen, colors[(board[i][j])-1], [j*100, i*40, 98 ,38])
                top = pygame.rect.Rect((j*100, i*40), (98 ,1))
                bot = pygame.rect.Rect((j*100, (i*40) +37 ),(98 ,1))
                left = pygame.rect.Rect((j*100, i*40), (37 ,1))
                right = pygame.rect.Rect(((j*100)+97, i*40), ( 37,1))
                board_squares.append([top, bot, left, right, (i,j)])
    return board_squares

run = True
while run:
    screen.fill(black)
    timer.tick(fps)
    squares = draw_board(board)

    player = pygame.draw.rect(screen, red, [player_x, SCREEN_HEIGHT - 30, 120, 15], 0)
    ball = pygame.draw.circle(screen, white,[ball_x,ball_y], 10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

#Buttons to move left right
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and not active:
        active = True
        ball_y_direction = -1
        ball_x_direction = random.choice([-1,1])
    elif keys[pygame.K_a] and active:
        player_direction = -1
    elif keys[pygame.K_d]  and active:
        player_direction = 1
    else:
        player_direction = 0

    if ball_x <= 10 or ball_x >= SCREEN_WIDTH -10:
        ball_x_direction *= -1

    if ball.colliderect(player):
        ball_y_direction *= -1

    for i in range(len(squares)):
        if ball.colliderect(squares[i][0]) or ball.colliderect(squares[i][1]):
            ball_y_direction *= -1 
            board[squares[i][4][0]][squares[i][4][1]]-=1
        if ball.colliderect(squares[i][2]) or ball.colliderect(squares[i][3]):
            ball_x_direction *= -1 
            board[squares[i][4][0]][squares[i][4][1]]-=1
        
        
    if ball_y >= SCREEN_HEIGHT - 10:
        active = False

  
    player_x += player_direction*speed
    ball_y += ball_y_direction * ball_y_speed
    ball_x += ball_x_direction * ball_x_speed

    pygame.display.flip()

pygame.quit()