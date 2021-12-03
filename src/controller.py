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
        mixer.music.load("assets/Frank_Sinatra.wav")
        mixer.music.play()
        pygame.display.set_caption('New York City Simulator')
        fontObj = pygame.font.Font("assets/Fancy.ttf", 50)
        textSurfaceObj = fontObj.render('New York City Simulator', True, (255,255,255), None)
        textRectObj = textSurfaceObj.get_rect(center = (450,100))
        self.screen.blit(textSurfaceObj,textRectObj)  

  
     

    def mainloop(self):
      
        while True:
            start_img = pygame.image.load("assets/start_bt.png")
            start_bt = button.Button(250,400,start_img,0.3)
            b1 = pygame.image.load("assets/button_1.png")
            bar1 = button.Button(60,390,b1,0.4)
            b2 = pygame.image.load("assets/button_2.png")
            bar2 = button.Button(500,390,b2,0.4) 
            Decisions.Decisions.startScreen(self, self.screen,self.background)
            start_bt.draw(self.screen)     
            for event in pygame.event.get():
                if start_bt.click(start_img,event) == True: 
                    bar = pygame.image.load("assets/bar.jpg")
                    self.background = pygame.transform.scale(bar, (self.window_width, self.window_height))
                    self.screen.blit(self.background,(0,0))
                    pygame.display.update()
                    Decisions.Decisions.bar(self,self.screen) 
                    bar1.draw(self.screen)
                    bar2.draw(self.screen)
                    pygame.display.update()
                    if bar2.click(start_img,event) == True:
                        hospital = pygame.image.load("assets/hospital.png")
                        self.background = pygame.transform.scale(bar, (self.window_width, self.window_height))
                        self.screen.blit(self.background,(0,0))
                        mixer.music.load("assets/bar_music.wav")
                        mixer.music.play()
                        pygame.display.update()
                        Decisions.Decisions.hospitalBed(self,self.screen)
                    if bar1.click(start_img,event) == True:
                       alley = pygame.image.load("assets/alleyway.jpg")
                       self.background = pygame.transform.scale(bar, (self.window_width, self.window_height))
                       self.screen.blit(self.background,(0,0))
                       mixer.music.load("assets/bar_music.wav")
                       mixer.music.play()
                       pygame.display.update()
                       Decisions.Decisions.alleyWay(self,self.screen)
                        
                        
                if event.type == pygame.QUIT:
                    exit()
   
     
            

