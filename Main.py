import pygame

pygame.init()

window = pygame.display.set_mode((1920,1080))

pygame.display.set_caption("Shadow of the Past")

#Położenie startowe postaci

x = 0
y = 990

#wymiary postaci:

szerokosc = 40
height = 90
velocity = 5

run = True

while run:
    pygame.time.delay(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    przyciski = pygame.key.get_pressed()

    if przyciski[pygame.K_LEFT]:
        x -= velocity
    if przyciski[pygame.K_RIGHT]:
        x += velocity
    if przyciski[pygame.K_UP]:
        y -= velocity
    if przyciski[pygame.K_DOWN]:
        y += velocity
    if przyciski[pygame.K_ESCAPE]:
        run = False
    
    window.fill(("black"))
    pygame.draw.rect(window, ("red"), (x, y, szerokosc, height))
    pygame.display.update()            
pygame.quit()            