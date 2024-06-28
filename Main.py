from Settings import *
from Player import Player

class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HIGHT))
        pygame.display.set_caption("Shadow of the past")
        self.clock = pygame.time.Clock()
        self.running = True

        self.all_sprites = []

        self.player = Player((400,300), self.all_sprites)

    def run(self):
        while self.running:    

            # Date Time
            datetime = self.clock.tick() / 1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            #Draw
            pygame.display.update()

        pygame.quit()      

if __name__ == "__main__":
    game = Game()
    game.run()                      