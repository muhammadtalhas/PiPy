import pygame
from pygame.locals import *


class main_menu():
    def __init__(self, inputSelf):
        screen = pygame.display.set_mode(inputSelf.size,pygame.FULLSCREEN)

        #BackGround = Background('../bg.jpg', [0,0])
        #pygame.image.load(BackGround)
        pygame.display.set_caption("PiPy")
         
         

        screen.fill(inputSelf.WHITE)

        pygame.draw.rect(screen, inputSelf.GREEN, (0,0,480,25), 0)

        #First row
        pygame.draw.circle(screen, inputSelf.RED, (40,180),40, 0)
        pygame.draw.circle(screen, inputSelf.RED, (120,180),40, 0)
        pygame.draw.circle(screen, inputSelf.RED, (200,180),40, 0)
        pygame.draw.circle(screen, inputSelf.RED, (280,180),40, 0)

        #Second row
        pygame.draw.circle(screen, inputSelf.RED, (40,300),40, 0)
        pygame.draw.circle(screen, inputSelf.RED, (120,300),40, 0)
        pygame.draw.circle(screen, inputSelf.RED, (200,300),40, 0)
        pygame.draw.circle(screen, inputSelf.RED, (280,300),40, 0)

        #Third row
        pygame.draw.circle(screen, inputSelf.RED, (40,420),40, 0)
        pygame.draw.circle(screen, inputSelf.RED, (120,420),40, 0)
        pygame.draw.circle(screen, inputSelf.RED, (200,420),40, 0)
        pygame.draw.circle(screen, inputSelf.RED, (280,420),40, 0)

        self.getInput()

    def getInput(self, event):
        exitApp = False
        while not exitApp:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exitApp = true
                if event.type is KEYDOWN and event.key == K_b:
                    exitApp = true
                if event.pos[0] > 0 and event.pos[0] < 80:
                    if event.pos[1] > 140 and event.pos[1] < 220:
                        print(1)
                    if event.pos[1] > 260 and event.pos[1] < 340:
                        print(5)
                    if event.pos[1] > 380 and event.pos[1] < 460:
                        print(9)
        print("exit confirmed")

                
            
        
