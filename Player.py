import pygame

class Player(object):

    def __init__(self, game):
        self.game = game

    def tick(self):
        pass

    def draw(self):
        pygame.draw.rect(self.game.window , ("red"), pygame.Rect(10, 10, 90, 90))