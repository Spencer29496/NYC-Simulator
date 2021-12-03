import pygame
import time
from src import character
from src import controller
from pygame import mixer

<<<<<<< HEAD
class Decisions():
=======
class Decisions:
>>>>>>> bc761514ef8f8fa34a6afe25531c3f5d158dadae
    def __init__(self):
        pygame.init()
        mixer.init()
        self.window_width = 900
        self.window_height = 600
        self.screen = pygame.display.set_mode((self.window_width, self.window_height))
        self.screen.fill((0,0,0))
        self.background = None
        self.screen.blit(self.background,(0,0))
        mixer.music.load("assets/Frank_Sinatra.wav")
        mixer.music.play() 

    def startScreen(self):
        self.background = pygame.image.load("assets/startscreen.jpg")
        self.screen.blit(self.background,(0,0))
        pygame.display.set_caption('New York City Simulator')
        fontObj = pygame.font.Font("assets/Fancy.ttf", 50)
        textSurfaceObj = fontObj.render('New York City Simulator', True, (255,255,255), None)
        textRectObj = textSurfaceObj.get_rect(center = (450,100))
<<<<<<< HEAD
        mixer.music.load("assets/Frank_Sinatra.wav")
        mixer.music.play(-1, 0.0)
        self.screen.blit(textSurfaceObj,textRectObj)
=======
        #mixer.music.load("assets/Frank_Sinatra.wav")
        #mixer.music.play()
        screen.blit(textSurfaceObj,textRectObj)
>>>>>>> bc761514ef8f8fa34a6afe25531c3f5d158dadae

    def bar(self):
        bar = pygame.image.load("assets/bar.jpg")
        self.background = pygame.transform.scale(bar, (self.window_width, self.window_height))
        self.screen.blit(self.background,(0,0))
        mixer.music.load("assets/bar_music.wav")
        mixer.music.play()
        pygame.display.update()
        barguy = pygame.image.load("assets/barfight.jpg")
        bar_fight = character.Player(50, 200, barguy, 0.4)
        bar_fight.draw(screen)
        bar_fight.bar_fight(self.screen)
        pygame.display.update()


        

