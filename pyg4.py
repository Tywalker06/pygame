import pygame
import random
import sys
import time
pygame.init();

white = (255, 255, 255)
black = (0, 0, 0)
red = (250, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

display_width = 800
display_height = 800

gameDisplay = pygame.display.set_mode((display_width,display_height))

move_x = display_width/2
move_y = display_height/2

move_x_change = 0
move_y_change = 0

font = pygame.font.SysFont(None, 30)

def Message_to_user(msg, color):
	screen_message = font.render(msg, True, color)
	gameDisplay.blit(screen_message, [display_width/2, display_height/2])

fps = 30
clock = pygame.time.Clock()

blocksize = 10

pygame.display.set_caption('Name of my game')

# pygame.display.update()

gameExit = False

while not gameExit:
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
		gameExit = True

		# if event.type == pygame.KEYUP:
		# 	if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
		# 		move_x_change = 0
		# 	if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
		# 		move_y_change = 0

	move_x += move_x_change
	move_y += move_y_change

	gameDisplay.fill(green)
	pygame.draw.rect(gameDisplay, black, [move_x, move_y, blocksize, blocksize,])
	pygame.display.update()

	clock.tick(fps)

Message_to_user("Sorry, Thanks For Playing", red)
pygame.display.update()
time.sleep(2)
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