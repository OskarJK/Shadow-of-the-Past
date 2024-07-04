import pygame
from pygame.math import Vector2

class Player(pygame.sprite.Sprite):

    def __init__(self, game, x, y):
        super().__init__()
        self.game = game
        self.image_right = pygame.image.load('images/player/Ghost_right.png')
        self.image_left = pygame.image.load('images/player/Ghost_left.png')
        self.image = self.image_right.subsurface(0, 0, 90, 90)
        self.rect = pygame.Rect(x, y, 90, 90)
        self.current_frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50
        self.direction = "right"
        self.speed = 5  # Prędkość poruszania się postaci
        self.animations = {
            "right": self.image_right,
            "left": self.image_left
        }

    def tick(self):
        pressed = pygame.key.get_pressed()
        movement = Vector2(0, 0)

        if pressed[pygame.K_w]:
            movement.y -= 1
        if pressed[pygame.K_s]:
            movement.y += 1
        if pressed[pygame.K_a]:
            movement.x -= 1
            self.direction = "left"
        if pressed[pygame.K_d]:
            movement.x += 1
            self.direction = "right"

        self.add_force(movement)

        # Update animation
        self.update_animation()

    def add_force(self, force):
        new_x = self.rect.x + int(force.x * self.speed)
        new_y = self.rect.y + int(force.y * self.speed)

        # Check horizontal boundaries
        if 0 <= new_x <= self.game.window.get_width() - self.rect.width:
            self.rect.x = new_x

        # Check vertical boundaries
        if 0 <= new_y <= self.game.window.get_height() - self.rect.height:
            self.rect.y = new_y

    def update_animation(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.current_frame = (self.current_frame + 1) % 8  # 8 frames in the sprite sheet
            self.image = self.animations[self.direction].subsurface(self.current_frame * 90, 0, 90, 90)

    def draw(self):
        self.game.window.blit(self.image, self.rect.topleft)

    def handle_collision(self, other_sprite):
        if self.rect.colliderect(other_sprite.rect):
            # Handle collision logic here
            pass
