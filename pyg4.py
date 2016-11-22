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


pygame.display.set_caption('Name of my game')

pygame.display.update()

gameExit = False

while not gameExit:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit = True

	gameDisplay.fill(green)
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