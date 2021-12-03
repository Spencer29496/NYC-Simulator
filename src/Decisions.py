import pygame
import time
from src import character
from src import controller
from pygame import mixer

class Decisions:
    def __init__(self):
        pygame.init()
        mixer.init
        self.window_width, self.window_height = pygame.display.get_surface().get_size()

    def startScreen(self,screen, background):
        background = pygame.image.load("assets/startscreen.jpg")
        screen.blit(background,(0,0))
        pygame.display.set_caption('New York City Simulator')
        fontObj = pygame.font.Font("assets/Fancy.ttf", 50)
        textSurfaceObj = fontObj.render('New York City Simulator', True, (255,255,255), None)
        textRectObj = textSurfaceObj.get_rect(center = (450,100))
        #mixer.music.load("assets/Frank_Sinatra.wav")
        #mixer.music.play()
        screen.blit(textSurfaceObj,textRectObj)

    def bar(self,screen):
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


        

