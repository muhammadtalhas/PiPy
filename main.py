import pygame
from pygame.locals import *
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
pygame.init()

size = (320,480)
screen = pygame.display.set_mode(size)#,pygame.FULLSCREEN)
 
pygame.display.set_caption("PiPy")
 
done = False
 
clock = pygame.time.Clock()
screen.fill(WHITE)
pygame.draw.circle(screen, RED, (40,180),40, 0)
pygame.draw.circle(screen, GREEN, (120,180),40, 0)
 
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type is KEYDOWN and event.key == K_w:
            #Debug to window- uncomment
            #pygame.display.set_mode(size)
            done = True
    
    pygame.display.flip()
    clock.tick(60)
print (clock)
pygame.quit()
