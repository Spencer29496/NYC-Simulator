import pygame
import sys
from src import button
from src import Decisions
from pygame import mixer

class Controller:

    def __init__(self):
        pygame.init
        mixer.init()
        pygame.font.init()
        self.window_width = 900
        self.window_height = 600
        self.screen = pygame.display.set_mode((self.window_width, self.window_height))
        self.screen.fill((0,0,0))
        self.background = pygame.image.load("assets/startscreen.jpg")
        self.screen.blit(self.background,(0,0))

  
     

    def mainloop(self):
      
        while True:
            start_img = pygame.image.load("assets/start_bt.png")
            start_bt = button.Button(250,400,start_img,0.3)
            Decisions.Decisions.startScreen(self)
            start_bt.draw(self.screen)       
            for event in pygame.event.get():
                if start_bt.click(start_img,event) == True:
                    bar = pygame.image.load("assets/bar.jpg")
                    self.background = pygame.transform.scale(bar, (self.window_width, self.window_height))
                    self.screen.blit(self.background,(0,0))
                    mixer.music.load("assets/bar_music.wav")
                    mixer.music.play()
                    pygame.display.update()

                    #Decisions.Decisions.bar(self,self.screen) 
                if event.type == pygame.QUIT:
                    exit()
   
            #self.eventloop()
            #while self.background == pygame.image.load("assets/startscreen.jpg"):
                #start_img = pygame.image.load("assets/start_bt.png")
                #start_bt = button.Button(250,400,start_img,0.3)
                #start_bt.draw(self.screen)
                       
            # update models
        

            # collisions
            


            # update the screen

    # OPTIONAL: put the event loop in a seperate method just to break up the mainloop()
    #def eventloop(self):
        #for event in pygame.event.get():
            #while self.background == pygame.image.load("assets/startscreen.jpg"):
                #start_img = pygame.image.load("assets/start_bt.png")
                #start_bt = button.Button(0,0,start_img,0.5)
                #start_bt.draw(self.screen)
            #if event.type == pygame.QUIT:
                #exit()
          
