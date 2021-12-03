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
<<<<<<< HEAD
        self.screen.blit(self.background,(0,0))
=======
        #self.screen.blit(self.background,(0,0))
        #start_bt = pygame.image.load("assets/startbt.png")
        #self.start_butt = button.Button(458, 540, start_bt, 0.3)
        #mixer.music.load("assets/Frank_Sinatra.wav")
        #mixer.music.play()
        #pygame.display.set_caption('New York City Simulator')
        #fontObj = pygame.font.Font("assets/Fancy.ttf", 50)
        #textSurfaceObj = fontObj.render('New York City Simulator', True, (255,255,255), None)
        #textRectObj = textSurfaceObj.get_rect(center = (450,100))
        #self.screen.blit(textSurfaceObj,textRectObj)  
>>>>>>> bc761514ef8f8fa34a6afe25531c3f5d158dadae

  
     

    def mainloop(self):
      
        while True:
            start_img = pygame.image.load("assets/start_bt.png")
            start_bt = button.Button(250,400,start_img,0.3)
<<<<<<< HEAD
            Decisions.Decisions.startScreen(self)
            start_bt.draw(self.screen)       
=======
            b1 = pygame.image.load("assets/button_1.png")
            bar1 = button.Button(60,390,b1,0.4)
            b2 = pygame.image.load("assets/button_2.png")
            bar2 = button.Button(500,390,b2,0.4) 
            Decisions.Decisions.startScreen(self, self.screen,self.background)
            start_bt.draw(self.screen)        
>>>>>>> bc761514ef8f8fa34a6afe25531c3f5d158dadae
            for event in pygame.event.get():
                if start_bt.click(start_img,event) == True:
                    bar = pygame.image.load("assets/bar.jpg")
                    self.background = pygame.transform.scale(bar, (self.window_width, self.window_height))
                    self.screen.blit(self.background,(0,0))
                    mixer.music.load("assets/bar_music.wav")
                    mixer.music.play()
                    pygame.display.update()

                    Decisions.Decisions.bar(self,self.screen) 
                    bar1.draw(self.screen)
                    bar2.draw(self.screen)
                    
                    pygame.display.update()
                if event.type == pygame.QUIT:
                    exit()
   
     
            


            # update the screen

    # OPTIONAL: put the event loop in a seperate method just to break up the mainloop()

    #def eventloop(self):
          # while self.background == pygame.image.load("assets/startscreen.jpg"):
                   #start_bt = Decisions.Decisions("assets/startbt.png")
                   #start_butt 

                       
            
    #def eventloop(self):
        #for event in pygame.event.get():
            #while self.background == pygame.image.load("assets/startscreen.jpg"):
                #start_img = pygame.image.load("assets/start_bt.png")
                #start_bt = button.Button(0,0,start_img,0.5)
                #start_bt.draw(self.screen)
            #if event.type == pygame.QUIT:
                #exit()
          
