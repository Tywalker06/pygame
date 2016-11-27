import pygame
import random
import sys
pygame.init();

white = (255, 255, 255)
black = (0, 0, 0)
red = (0, 255, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

gameDisplay = pygame.display.set_mode((800,600))

move_x = 300
move_y = 300
move_x_change = 0

pygame.display.set_caption('Name of my game')

pygame.display.update()

gameExit = False

while not gameExit:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit = True
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				move_x_change = -10
			if event.key == pygame.K_RIGHT:
				move_x = 10

	move_x += move_x_change


	gameDisplay.fill(green)
	pygame.draw.rect(gameDisplay, red, [move_x, move_y, 10, 10,])
	pygame.display.update()

pygame.quit()
quit()



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