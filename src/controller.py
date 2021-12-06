import pygame
import sys
from src import button
from src import Decisions
from src import character
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
        self.start_bt = button.Button(250,400,self.start_img,0.3)
        self.start_bt.draw(self.screen)
        self.b1 = pygame.image.load("assets/button_1.png")
        self.bar1 = button.Button(0,0,self.b1,0)
        self.b2 = pygame.image.load("assets/button_2.png")
        self.bar2 = button.Button(0,0,self.b2,0)
        self.bar1.draw(self.screen)
        self.bar2.draw(self.screen)
        self.b3 = pygame.image.load("assets/button_3.png")
        self.alley1 = button.Button(0,0,self.b3,0)
        self.b4 = pygame.image.load("assets/button_4.png")
        self.alley2 = button.Button(0,0,self.b4,0)
        self.alley1.draw(self.screen)
        self.alley2.draw(self.screen)
        self.b5 = pygame.image.load("assets/button_5.png")
        self.taxi1 = button.Button(0,0,self.b5,0)
        self.b6 = pygame.image.load("assets/button_6.png")
        self.taxi2 = button.Button(0,0,self.b6,0)
        self.taxi1.draw(self.screen)
        self.taxi2.draw(self.screen)


    def mainloop(self):
    
        while True:
            if self.background == None:
                Decisions.Decisions.startScreen(self)
            if self.start_bt.draw(self.screen) == True: 
                self.start_bt = button.Button(0,0,self.start_img,0)
                Decisions.Decisions.bar(self)
                self.bar1 = button.Button(60,390,self.b1,0.4)
                self.bar1.draw(self.screen)
                self.bar2 = button.Button(500,390,self.b2,0.4)
                self.bar2.draw(self.screen)
                pygame.display.update()
            if self.bar1.draw(self.screen) == True:
                self.bar1 = button.Button(0,0,self.b1,0)
                self.bar2 = button.Button(0,0,self.b2,0)
                Decisions.Decisions.alley(self)
                self.alley1 = button.Button(50,400,self.b3,0.5)
                self.alley2 = button.Button(500,400,self.b4,0.5)
                self.alley1.draw(self.screen)
                self.alley2.draw(self.screen)
                pygame.display.update()
            if self.alley1.draw(self.screen) == True:
                self.alley1 = button.Button(0,0,self.b3,0)
                self.alley2 = button.Button(0,0,self.b4,0)
                Decisions.Decisions.taxiHome(self)
                self.taxi1 = button.Button(500,390,self.b5,0.4)
                self.taxi2 = button.Button(60,390,self.b6,0.4)
                self.taxi1.draw(self.screen)
                self.taxi2.draw(self.screen)
                pygame.display.update()
            if self.taxi1.draw(self.screen) == True:
                self.taxi1 = button.Button(0,0,self.b5,0)
                self.taxi2 = button.Button(0,0,self.b6,0)
                Decisions.Decisions.finallyHome(self)
            if self.bar2.draw(self.screen) == True:
                self.bar1 = button.Button(0,0,self.b1,0)
                self.bar2 = button.Button(0,0,self.b2,0)
                Decisions.Decisions.hospital(self)
            if self.alley2.draw(self.screen) == True:
                self.alley1 = button.Button(0,0,self.b3,0)
                self.alley2 = button.Button(0,0,self.b4,0)
                Decisions.Decisions.hospital(self)
            if self.taxi2.draw(self.screen) == True:
                self.taxi1 = button.Button(0,0,self.b5,0)
                self.taxi2 = button.Button(0,0,self.b6,0)
                Decisions.Decisions.hospitalCold(self)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                    
     
            


            # update the screen

    # OPTIONAL: put the event loop in a seperate method just to break up the mainloop()

            
    def eventloop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
          

