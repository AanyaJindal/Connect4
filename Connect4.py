import pygame
import random

pygame.init()
pygame.font.init()

DISPLAY_WIDTH = 640
DISPLAY_HEIGHT = 480

#         R    G    B
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLACK = (  0,   0,   0)
GRAY  = (169, 169, 169)

# 0 denotes empty, 1 denotes red, 2 denotes black
ball = []
ball.append(pygame.image.load('Assets/empty.png'))
ball.append(pygame.image.load('Assets/red.png'))
ball.append(pygame.image.load('Assets/black.png'))
for i in range(3):
	ball[i] = pygame.transform.scale(ball[i], (50, 50))

game_display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
font_display = pygame.font.SysFont('comicsansms', 25)
pygame.display.set_caption("CONNECT 4");
clock = pygame.time.Clock()

# filling of the board till now
records = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
# for denoting which player has to move
turn = 0
# denotes the entry where ball will be dropped in the particular column
top = [5, 5, 5, 5, 5, 5, 5]
# denotes the current selection of ball
current_ball = 0
winner = 0

def draw_board():
	y = 50
	# for filling the status of game till now
	for i in range(len(records)):
		x = 145
		for j in range(len(records[i])):
			game_display.blit(ball[records[i][j]], (x, y))
			if records[i][j] > 0:
				game_display.blit(ball[0], (x, y))
			x += 50
		y += 50

	# black's turn
	if turn%2 == 0:
		pygame.draw.rect(game_display, GRAY, (548, 398, 55, 55))
	else:
		pygame.draw.rect(game_display, GRAY, (48, 398, 55, 55))
	game_display.blit(ball[1], (50, 400))
	game_display.blit(ball[2], (550, 400))

def check_win(c, r):
	

def click_column(i):
	global turn
	global top
	if top[i] == -1:
		# the column is full
		return
	if turn%2 == 0:
		records[top[i]][i] = 2
	else:
		records[top[i]][i] = 1
	check_win(top[i], i)
	turn += 1
	top[i] -= 1
	
def click_slot(mx, my):
	x = 145
	for i in range(7):
		if mx >= x and mx <= x+50:
			click_column(i)
			return
		x += 50

def mouse_click(mx, my):
	if mx >= 145 and mx <= 495 and my >= 50 and my <= 350:
		click_slot(mx, my)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONUP:
            mx, my = pygame.mouse.get_pos()
            mouse_click(mx, my)

    game_display.fill(WHITE)
    draw_board()
    pygame.display.flip()
    clock.tick(60)