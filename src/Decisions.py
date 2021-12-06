import pygame
import time
from src import button
from src import character
from src import controller
from pygame import mixer

class Decisions:
    def __init__(self):
        pygame.init
        mixer.init()
        pygame.font.init()
        self.window_width = 900
        self.window_height = 600
        self.screen = pygame.display.set_mode((self.window_width, self.window_height))
        self.screen.fill((0,0,0))
        self.background = None

    def startScreen(self):
        self.background = pygame.image.load("assets/startscreen.jpg")
        self.screen.blit(self.background,(0,0))
        pygame.display.set_caption('New York City Simulator')
        fontObj = pygame.font.Font("assets/Fancy.ttf", 50)
        textSurfaceObj = fontObj.render('New York City Simulator', True, (255,255,255), None)
        textRectObj = textSurfaceObj.get_rect(center = (450,100))
        mixer.music.load("assets/Frank_Sinatra.wav")
        mixer.music.play()
        self.screen.blit(textSurfaceObj,textRectObj)
        pygame.display.update()

    def bar(self):
        bar = pygame.image.load("assets/bar.jpg")
        self.background = pygame.transform.scale(bar, (self.window_width, self.window_height))
        self.screen.blit(self.background,(0,0))
        mixer.music.load("assets/bar_music.wav")
        mixer.music.play()
        barguy = pygame.image.load("assets/barfight.jpg")
        bar_fight = character.Player(50, 200, barguy, 0.4)
        bar_fight.draw(self.screen)
        bar_fight.bar_fight(self.screen)
        pygame.display.update()


    def alley(self):
        alley = pygame.image.load("assets/alleyway.jpg")
        self.background = pygame.transform.scale(alley, (self.window_width, self.window_height))
        self.screen.blit(self.background,(0,0))
        homeless_man = pygame.image.load("assets/homeless guy.png")
        homeless = character.Player(300,300,homeless_man,.3)
        homeless.draw(self.screen)
        homeless.alley_guy(self.screen)
        pygame.display.update()



    def hospital(self):
        hospital = pygame.image.load("assets/hospital.png")
        self.background = pygame.transform.scale(hospital, (self.window_width, self.window_height))
        self.screen.blit(self.background,(0,0))
        doctor = pygame.image.load("assets/doctor.png")
        medic = character.Player(550,200,doctor,0.5)
        medic.draw(self.screen)
        medic.hospital(self.screen)
        pygame.display.update()
    
    def taxiHome(self):
        taxi = pygame.image.load("assets/taxi.jpg")
        self.background = pygame.transform.scale(taxi, (self.window_width, self.window_height))
        self.screen.blit(self.background,(0,0))
        pygame.display.update()
        taxi_man = pygame.image.load("assets/taxidriver.png")
        taxi_guy = character.Player(550,200,taxi_man,0.65)
        taxi_guy.draw(self.screen)
        taxi_guy.taxi_time(self.screen)
        pygame.display.update()

    def finallyHome(self):
        house = pygame.image.load("assets/house.png")
        self.background = pygame.transform.scale(house, (self.window_width, self.window_height))
        self.screen.blit(self.background,(0,0))
        pygame.display.update()
        children = pygame.image.load("assets/kids.png")
        kids = character.Player(250,300,children,0.1)
        kids.draw(self.screen)
        kids.arrivedHome(self.screen)
        pygame.display.update()

    def hospitalCold(self):
        hospital = pygame.image.load("assets/hospital.png")
        self.background = pygame.transform.scale(hospital, (self.window_width, self.window_height))
        self.screen.blit(self.background,(0,0))
        doctor = pygame.image.load("assets/doctor.png")
        medic = character.Player(550,200,doctor,0.5)
        medic.draw(self.screen)
        medic.coldHospital(self.screen)
        pygame.display.update()
