import pygame

pygame.init()

window = pygame.display.set_mode((1920,1080))

pygame.display.set_caption("Shadow of the Past")

#Położenie startowe postaci

x = 0
y = 990

#wymiary postaci:
character = pygame.Rect(10,10,90,90)
velocity = 1

walkleft = False
walkright = False


run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            run = False
            
    przyciski = pygame.key.get_pressed()

    if przyciski[pygame.K_LEFT]:
        character.x -= velocity
    if przyciski[pygame.K_RIGHT]:
        character.x += velocity
    if przyciski[pygame.K_UP]:
        character.y -= velocity
    if przyciski[pygame.K_DOWN]:
        character.y += velocity

    
    window.fill(("black"))
    pygame.draw.rect(window, ("red"), character)
    pygame.display.flip()            
pygame.quit()            