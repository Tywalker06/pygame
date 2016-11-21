import pygame
import random
import sys
pygame.init();

white = (255, 255, 255)
black = (0, 0, 0)
red = (0, 255, 0)
green = (0, 255, 0)
blue = (0, 0, 255)


class Shovel(Sprite):
	def __init__(self):
		Sprite.__init__(self)
		self.image = image.load("shovel.gif").convert()
		self.rect = self.image.get_rect()

class Poop(Gold):
	def __init__(self):
		Sprite.__init__(self)
		self.image = image.load("poop.bmp").convert_alpha()
		self.rect = self.image.get_rect
#Using the already defined Gold class witht he exception of new pic and 
shovel = Shovel()
sprites = RenderPlain