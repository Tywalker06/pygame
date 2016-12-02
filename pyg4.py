import pygame
from pygame import *
from random import *
import random
import sys
import time
from pygame.locals import*
from pygame.sprite import*
pygame.init();

white = (255, 255, 255)
black = (0, 0, 0)
red = (250, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

display_width = 800
display_height = 600

move_x = display_width/2
move_y = display_height/2

gameDisplay = pygame.display.set_mode((display_width,display_height))

timer = pygame.time.get_ticks()

font = pygame.font.SysFont(None, 30)

def Message_to_user(msg, color):
	screen_message = font.render(msg, True, color)
	gameDisplay.blit(screen_message, [200, display_height/2])

def timer_message(msg, color):
	screen_message = font.render(msg, True, color)
	gameDisplay.blit(screen_message, [200, display_height - 20])

def score(msg, color):
    screen_message = font.render(msg, True, color)
    gameDisplay.blit(screen_message,[0,0])


fps = 45
clock = pygame.time.Clock()

blocksize = 10

pygame.display.set_caption('Mouse Punch')

ranx = random.randrange(0, display_width - blocksize)
rany = random.randrange(0, display_height - blocksize)




class Mouse(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = image.load("mouse.png").convert_alpha()
        self.image = transform.scale(self.image, (50, 50))
        self.x = ranx
        self.y = rany
        self.rect = self.image.get_rect()

    def move(self):
        randX = randint(0, display_width - 15)
        randY = randint(0, display_height - 100)
        self.rect.center = (randX,randY)

class Bomb(Mouse):
    def __init__(self):
        Sprite.__init__(self)
        self.image = image.load("bomb.png").convert_alpha()
        self.image = transform.scale(self.image, (50, 50))
        self.x = ranx
        self.y = rany
        self.rect = self.image.get_rect()

	
    
class Snake(Sprite):
	def __init__ (self):
		Sprite.__init__(self)
		self.image = pygame.Surface( [blocksize, blocksize])
		self.rect = self.image.get_rect()
	



my_mouse = Mouse(ranx, rany)
my_snake = Snake()
my_bomb = Bomb()

sprites = RenderPlain(my_mouse,my_snake,my_bomb)
my_mouse.move()
my_bomb.move()
sprites.update()
sprites.draw(gameDisplay)



move_x = display_width/2
move_y = display_height/2




def gameLoop():
	move_x = display_width/2
	move_y = display_height/2

	move_x_change = 0
	move_y_change = 0

	count = 0

	ranx = random.randrange(0, display_width - blocksize)
	rany = random.randrange(0, display_height - blocksize)
	seconds = (pygame.time.get_ticks() - timer)/1000

	gameExit = False
	gameOver = False
	while not gameExit:

		while gameOver == True:

			gameDisplay.fill(black)
			Message_to_user("Game Over, Press 'p' to play again or 'q' to quit", red)
			pygame.display.update()

			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						gameExit = True
						gameOver = False
					if event.key == pygame.K_p:
						gameLoop()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameExit = True
			if event.type == pygame.KEYDOWN:
				

				if event.key == pygame.K_LEFT:
					move_x_change = - blocksize
					move_y_change = 0
				elif event.key == pygame.K_RIGHT:
					move_x_change = blocksize
					move_y_change = 0
				elif event.key == pygame.K_UP:
					move_y_change = - blocksize
					move_x_change = 0
				elif event.key == pygame.K_DOWN:
					move_y_change = blocksize
					move_x_change = 0


		if move_x >= display_width or move_x < 0 or move_y >= display_height or move_y < 0 or seconds > 60:
			gameOver = True

		if pygame.sprite.collide_rect(my_mouse,my_snake):
			my_mouse.move()
			my_bomb.move()
			
			mixer.Sound("lose.wav").play()
			
			count += 1

		if pygame.sprite.collide_rect(my_snake, my_bomb):
			my_bomb.move()
			gameOver = True


		seconds = (pygame.time.get_ticks() - timer)/1000
		

		if gameOver != True:
			
			timer_message("Timer: " + str(seconds), black)
			pygame.display.update()


		
		move_x += move_x_change
		move_y += move_y_change

		my_snake.rect.x = move_x
		my_snake.rect.y = move_y


		gameDisplay.fill(green)
		
		sprites.draw(gameDisplay)
		
		score("Score: " + str(count), black)
		
		pygame.display.update()
		sprites.update()
		sprites.draw(gameDisplay)
		
		clock.tick(fps)
		
	pygame.quit()
	quit()

gameLoop()

