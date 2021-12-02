import pygame
import sys

class Controller:

    def __init__(self):
        self.window_width = 900
        self.window_height = 600
        pygame.init()
        self.screen = pygame.display.set_mode(self.window_width, self.window_height)
        self.background = pygame.image.load(startscreen.jpg)
        self.background.fill((250, 250, 250))


    def mainloop(self):
        while True:  
            self.eventloop()

            # update models
            self.enemies.update()
            self.projectiles.update()

            # collisions
            fight = pygame.sprite.spritecollide(self.player, self.enemies, False)
            if fight:
                for enemy in fight:
                    if self.player.fight(enemy):
                        enemy.kill()
                    else:
                        self.player.health -= 1

            bullets = pygame.sprite.groupcollide(self.enemies, self.projectiles, False, True)
            if bullets:
                for enemy in bullets:
                    enemy.pause()

            # end the program
            if self.player.health == 0:
                return

            # redraw
            self.screen.blit(self.background, (0, 0))
            self.all_sprites.draw(self.screen)
            #self.projectiles.draw(self.screen)

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

