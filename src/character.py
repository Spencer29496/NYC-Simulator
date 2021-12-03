import pygame
from src import button

class Player():

    def __init__(self,x ,y, image, scale):
       width = image.get_width()
       height = image.get_height()
       self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
       self.rect = self.image.get_rect()
       self.rect.topleft = (x, y)
        
    def draw(self, surface):
        surface.blit(self.image, (self.rect.x,self.rect.y))

    def bar_fight(self, screen):
        #barguy = pygame.image.load("assets/barfight.jpg")    
        fontObj = pygame.font.Font("assets/Lato-Bold.ttf", 30)
        textSurfaceObj = fontObj.render('A FIGHT BREAKS OUT!!!! WHICH DECISION WILL YOU MAKE', True, (255,255,255), (0,0,0))
        textRectObj = textSurfaceObj.get_rect(center = (450,100))
        screen.blit(textSurfaceObj,textRectObj)  
   
    def alley_fight(self, screen):
        fontObj = pygame.font.Font("assets/Lato-Bold.ttf", 30)
        textSurfaceObj = fontObj.render('YOU SEE A HOMELESS MAN. WILL YOU GIVE HIM MONEY?', True, (255,255,255), (0,0,0))
        textRectObj = textSurfaceObj.get_rect(center = (450,100))
        screen.blit(textSurfaceObj,textRectObj) 
       

    def hospital(self, screen):
        fontObj = pygame.font.Font("assets/Lato-Bold.ttf", 30)
        textSurfaceObj = fontObj.render('YOU GOT BEAT UP. WELCOME TO THE HOSPITAL!!', True, (255,255,255), (0,0,0))
        textRectObj = textSurfaceObj.get_rect(center = (450,100))
        screen.blit(textSurfaceObj,textRectObj)

