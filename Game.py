import pygame
import sys
from player import Player

class Game(object):

    def __init__(self):
        #Konfiguracja
        self.tps_max = 60.0

        #Initialization
        pygame.init()
        self.window = pygame.display.set_mode((1920,1080))
        self.image_background = pygame.image.load('images/background/background.jpg')
        self.tps_clock = pygame.time.Clock()
        self.tps_delta = 0.0

        self.player = Player(self, 10, 10)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    sys.exit(0)
            #Ticking
            self.tps_delta += self.tps_clock.tick() / 1000.0
            while self.tps_delta > 1 / self.tps_max:
                self.tick()
                self.tps_delta -= 1 / self.tps_max

            #Drawing          
            self.draw()
            pygame.display.flip()                      
                        
    def tick(self):
        self.player.tick()

    def draw(self):
        self.window.blit(self.image_background, (0, 0))
        self.player.draw()


if __name__ == "__main__":
    Game()        