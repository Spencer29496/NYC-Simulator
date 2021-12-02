import pygame
import sys
from src import button
from src import Decisions

class Controller:

    def __init__(self):
        pygame.init()
        self.window_width = 900
        self.window_height = 600
        self.screen = pygame.display.set_mode((self.window_width, self.window_height))
        self.screen.fill((0,0,0))
        self.background = pygame.image.load("assets/startscreen.jpg")
        self.screen.blit(self.background,(0,0))



    def mainloop(self):
	
        while True:  
                self.eventloop()
                self.start_butt.draw(self.screen)
                       
            # update models
        

            # collisions
            


            # update the screen

    # OPTIONAL: put the event loop in a seperate method just to break up the mainloop()
    def eventloop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.player.move("U")
                if event.key == pygame.K_DOWN:
                    self.player.move("D")

