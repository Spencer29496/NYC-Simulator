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
        start_bt = pygame.image.load("assets/startbt.png")
        self.start_butt = button.Button(458, 540, start_bt, 0.3)



    def mainloop(self):
	
        while True:  
                self.eventloop()
                self.start_butt.draw(self.screen)
                       
            # update models
        

            # collisions
            


            # update the screen

    # OPTIONAL: put the event loop in a seperate method just to break up the mainloop()
    def eventloop(self):
          # while self.background == pygame.image.load("assets/startscreen.jpg"):
                   #start_bt = Decisions.Decisions("assets/startbt.png")
                   #start_butt 

                       
            
