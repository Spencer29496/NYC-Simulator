import pygame
import time
from src import controller
from pygame import mixer

class Decisions():
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
        mixer.music.load("assets/Frank_Sinatra.wav")
        mixer.music.play(-1, 0.0)
        self.screen.blit(textSurfaceObj,textRectObj)

    def bar(self):
        bar = pygame.image.load("assets/bar.jpg")
        self.background = pygame.transform.scale(bar, (self.window_width, self.window_height))
        self.screen.blit(self.background,(0,0))
        mixer.music.load("assets/bar_music.wav")
        mixer.music.play()
        pygame.display.update()

