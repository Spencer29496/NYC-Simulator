import pygame
from src import button

class Decisions:
	def __init__(self):
		start_bt = pygame.image.load("assets/startbt.png")
		self.start_butt = button.Button(458, 540, start_bt, 0.3)
