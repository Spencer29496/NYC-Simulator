import pygame
import sys

class Controller:

    def __init__(self):
        pygame.init()
        self.window_width = 900
        self.window_height = 600
<<<<<<< HEAD
        pygame.init()
        self.screen = pygame.display.set_mode((self.window_width, self.window_height))
        self.background = pygame.image.load("assets/startscreen.jpg")
=======
        self.screen = pygame.display.set_mode((self.window_width, self.window_height))
        self.background = pygame.image.load("assets/startscreen.jpg")

>>>>>>> e9c673c579b6722b431f4d4e06262824fc796bb2


    def mainloop(self):
        while True:  
            self.eventloop()

<<<<<<< HEAD
            
=======
            # update models
        

            # collisions
            

>>>>>>> e9c673c579b6722b431f4d4e06262824fc796bb2
            # update the screen
            pygame.display.flip()

    # OPTIONAL: put the event loop in a seperate method just to break up the mainloop()
    def eventloop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.player.move("U")
                if event.key == pygame.K_DOWN:
                    self.player.move("D")
                if event.key == pygame.K_LEFT:
                    self.player.move("L")
                if event.key == pygame.K_RIGHT:
                    self.player.move("R")
                if event.key == pygame.K_SPACE:
                    if len(self.projectiles.sprites()) <= 5:
                        p = Projectile.Projectile(self.window_width)
                        pos = self.player.rect.midright
                        p.rect.x = pos[0]
                        p.rect.y = pos[1]
                        self.projectiles.add(p)
                        self.all_sprites(p)
                    else:
                        print("can't shoot", len(self.projectiles.sprites()))

