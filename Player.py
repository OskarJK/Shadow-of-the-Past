from Settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self, position, groups):
        super().__init__(groups)
        self.image = pygame.image.load(join('images', 'player', 'down', 'character.png')).convert_alpha()
        self.rect = self.image.get_frect(center = position)
