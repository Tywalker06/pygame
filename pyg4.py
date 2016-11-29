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
display_height = 800

gameDisplay = pygame.display.set_mode((display_width,display_height))


font = pygame.font.SysFont(None, 30)

def Message_to_user(msg, color):
	screen_message = font.render(msg, True, color)
	gameDisplay.blit(screen_message, [200, display_height/2])

fps = 30
clock = pygame.time.Clock()

blocksize = 10

pygame.display.set_caption('Snake Game')

randMouseX = random.randrange(0, display_width - blocksize)
randMouseY = random.randrange(0, display_height - blocksize)

class Mouse(Sprite):
	def __init__(self):
		Sprite.__init__(self)
		self.image = image.load("mouse.png").convert_alpha()
		self.image = transform.scale(self.image, (50, 50))
		self.rect = self.image.get_rect()



# pygame.display.update()
my_mouse = Mouse()
sprites = RenderPlain(my_mouse)

sprites.update()
sprites.draw(gameDisplay)



def gameLoop():
	move_x = display_width/2
	move_y = display_height/2

	move_x_change = 0
	move_y_change = 0


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


		if move_x >= display_width or move_x < 0 or move_y >= display_height or move_y < 0:
			gameOver = True


		move_x += move_x_change
		move_y += move_y_change

		gameDisplay.fill(green)
		pygame.draw.rect(gameDisplay, black, [move_x, move_y, blocksize, blocksize,])
		sprites.draw(gameDisplay)
		

		pygame.display.update()
		sprites.update()
		# sprites.draw(gameDisplay)
		
		clock.tick(fps)
		
	pygame.quit()
	quit()

gameLoop()

# class Box(pygame.sprite.Sprite)
# 	def __init__(self, color, x, y, width, height):
# 		pygame.sprite.Sprite
# class Shovel(Sprite):
# 	def __init__(self):
# 		Sprite.__init__(self)
# 		self.image = image.load("shovel.gif").convert()
# 		self.rect = self.image.get_rect()

# class Poop(Gold):
# 	def __init__(self):
# 		Sprite.__init__(self)
# 		self.image = image.load("poop.bmp").convert_alpha()
# 		self.rect = self.image.get_rect
# #Using the already defined Gold class witht he exception of new pic and 
# shovel = Shovel()
# sprites = RenderPlain