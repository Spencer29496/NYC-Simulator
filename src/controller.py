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
        self.background = None
        self.start_img = pygame.image.load("assets/start_bt.png").convert_alpha()
        self.start_bt = button.Button(310,350,self.start_img,0.2)
        self.start_bt.draw(self.screen)
  
     

    def mainloop(self):
      
        while True:
           # b1 = pygame.image.load("assets/button_1.png").convert_alpha()
           # bar1 = button.Button(60,390,b1,0.4)
          #  b2 = pygame.image.load("assets/button_2.png").convert_alpha()
           # bar2 = button.Button(500,390,b2,0.4)
           # b3 = pygame.image.load("assets/button_3.png").convert_alpha()
           # alley3 = button.Button(60,250,b3,0.4)
          #  b4 = pygame.image.load("assets/button_4.png").convert_alpha()
           # alley4 = button.Button(500,250,b4,0.4) 
            if self.background == None:
                Decisions.Decisions.startScreen(self, self.screen,self.background)   
            if self.start_bt.draw(self.screen) == True: 
                self.start_bt = button.Button(0,0,self.start_img,0)
                Decisions.Decisions.bar(self,self.screen)
            for event in pygame.event.get():
        
                          
                        
                if event.type == pygame.QUIT:
                     exit()
   
     
            

