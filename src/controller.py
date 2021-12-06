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
        self.start_img = pygame.image.load("assets/start_bt.png")
        self.start_bt = button.Button(310,350,self.start_img,0.2)
        self.start_bt.draw(self.screen)
        self.b1 = pygame.image.load("assets/button_1.png")
        self.bar1 = button.Button(0,0,self.b1,0)
        self.bar1.draw(self.screen)
        self.b2 = pygame.image.load("assets/button_2.png")
        self.bar2 = button.Button(0,0,self.b2,0)
        self.bar2.draw(self.screen)
        self.b3 = pygame.image.load("assets/button_3.png")
        self.alley1 = button.Button(0,0,self.b3,0)
        self.alley1.draw(self.screen)
        self.b4 = pygame.image.load("assets/button_4.png")
        self.alley2 = button.Button(0,0,self.b4,0) 
        self.alley2.draw(self.screen)
  
     

    def mainloop(self):
      
        while True:
            if self.background == None:
                Decisions.Decisions.startScreen(self, self.screen,self.background)  
            if self.start_bt.draw(self.screen) == True: 
                self.start_bt = button.Button(0,0,self.start_img,0)
                Decisions.Decisions.bar(self,self.screen)
                self.bar1 = button.Button(60,390,self.b1,0.4)
                self.bar1.draw(self.screen)
                self.bar2 = button.Button(500,390,self.b2,0.4)
                self.bar2.draw(self.screen)
                pygame.display.update()
            if self.bar1.draw(self.screen) == True:
                self.bar1 = button.Button(0,0,self.b1,0)
                self.bar2 = button.Button(0,0,self.b2,0)
                Decisions.Decisions.alleyWay(self,self.screen)
                self.alley1 = button.Button(50,400,self.b3,0.4)
                self.alley1.draw(self.screen)
                self.alley2 = button.Button(500,400,self.b4,0.4)
                self.alley2.draw(self.screen)
                pygame.display.update()
            if self.alley1.draw(self.screen) == True:
                self.alley1 = button.Button(0,0,self.b3,0)
                self.alley2 = button.Button(0,0,self.b4,0)
                Decisions.Decisions.taxi_home(self, self.screen) 
                pygame.display.update()
            if self.bar2.draw(self.screen) == True:
                self.bar1 = button.Button(0,0,self.b1,0)
                self.bar2 = button.Button(0,0,self.b2,0)
                Decisions.Decisions.hospitalBed(self, self.screen)
            for event in pygame.event.get():
        
                          
                        
                if event.type == pygame.QUIT:
                     exit()
   
     
            

