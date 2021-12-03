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
        self.color = (0,0,0)


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

    def newScreen(self):
        self.screen.fill(self.color) 
        self.draw(self.screen) 


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

    def alleyWay(self, screen):
        alleyway = pygame.image.load("assets/alleyway.jpg")
        self.background = pygame.transform.scale(alleyway, (self.window_width, self.window_height))
        self.screen.blit(self.background,(0,0))
        pygame.display.update()
        homeless = pygame.image.load("assets/homeless.png")
        street_guy = character.Player(300,350,homeless,0.4)
        street_guy.draw(screen)
        street_guy.alley_fight(self.screen)
        pygame.display.update()


    def hospitalBed(self, screen):
        hospital = pygame.image.load("assets/hospital.png")
        self.background = pygame.transform.scale(hospital, (self.window_width, self.window_height))
        self.screen.blit(self.background,(0,0))
        pygame.display.update()
        doctor = pygame.image.load("assets/doctor.png")
        medic = character.Player(550,200,doctor,0.3)
        medic.draw(screen)
        medic.hospital(self.screen)
        pygame.display.update()


        

