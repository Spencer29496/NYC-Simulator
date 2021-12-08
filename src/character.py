import pygame


class Player():

    def __init__(self,x ,y, image, scale):
       """
       This method sets the instance variables
       args(x,y,image,scale): the coordinates image and the scale for the caption and image displayed on screen
       return: none
       """
       width = image.get_width()
       height = image.get_height()
       self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
       self.rect = self.image.get_rect()
       self.rect.topleft = (x, y)
        
    def draw(self, surface):
        """
       This method updates the screen
       args(surface): the screen that is being updated
       return: none
       """
        surface.blit(self.image, (self.rect.x,self.rect.y))

    def bar_fight(self, screen):
        """
       This method sets the captioning for the bar fight scenario
       args(screen): the screen
       return: none
       """
        #barguy = pygame.image.load("assets/barfight.jpg")    
        fontObj = pygame.font.Font("assets/Lato-Bold.ttf", 30)
        textSurfaceObj = fontObj.render('A FIGHT BREAKS OUT!!!! WHICH DECISION WILL YOU MAKE', True, (255,255,255), (0,0,0))
        textRectObj = textSurfaceObj.get_rect(center = (450,100))
        screen.blit(textSurfaceObj,textRectObj)

    def alley_guy(self,screen):
        """
       This method sets the captioning for the alley guy scenario
       args(screen): the screen
       return: none
       """
        fontObj = pygame.font.Font("assets/Lato-Bold.ttf", 30)
        textSurfaceObj = fontObj.render('You see a homeless man! Do you give him money?', True, (255,255,255), (0,0,0))
        textRectObj = textSurfaceObj.get_rect(center = (450,100))
        screen.blit(textSurfaceObj,textRectObj)

    def taxi_time(self, screen):
        """
       This method sets the captioning for the taxi scenario
       args(screen): the screen
       return: none
       """
        fontObj = pygame.font.Font("assets/Lato-Bold.ttf", 25)
        textSurfaceObj = fontObj.render('YOU FIND A TAXI AFTER A LONG NIGHT. DO YOU PAY FOR THE DRIVE ?', True, (255,255,255), (0,0,0))
        textRectObj = textSurfaceObj.get_rect(center = (450,100))
        screen.blit(textSurfaceObj,textRectObj)


    def hospital(self, screen):
        """
       This method sets the captioning for the hospital scenario
       args(screen): the screen
       return: none
       """
        fontObj = pygame.font.Font("assets/Lato-Bold.ttf", 30)
        textSurfaceObj = fontObj.render('YOU GOT BEAT UP. WELCOME TO THE HOSPITAL!! YOU LOST!', True, (255,255,255), (0,0,0))
        textRectObj = textSurfaceObj.get_rect(center = (450,100))
        screen.blit(textSurfaceObj,textRectObj)


    def arrivedHome(self, screen):
        """
       This method sets the captioning for the final home scenario
       args(screen): the screen
       return: none
       """
        fontObj = pygame.font.Font("assets/Lato-Bold.ttf", 25)
        textSurfaceObj = fontObj.render('YOU ARRIVED HOME SAFE! CONGRATULATIONS!!', True, (255,255,255), (0,0,0))
        textRectObj = textSurfaceObj.get_rect(center = (450,100))
        screen.blit(textSurfaceObj,textRectObj)
 
    def coldHospital(self, screen):
        """
       This method sets the captioning for the hypothermia scenario
       args(screen): the screen
       return: none
       """
        fontObj = pygame.font.Font("assets/Lato-Bold.ttf", 25)
        textSurfaceObj = fontObj.render('YOU TRIED WALKING HOME AND GOT HYPOTHERMIA', True, (255,255,255), (0,0,0))
        textRectObj = textSurfaceObj.get_rect(center = (450,100))
        screen.blit(textSurfaceObj,textRectObj)
 


