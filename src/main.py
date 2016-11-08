import pygame
from pygame.locals import *
import apps
class OSMain:
    def __init__(self):
        #colors
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.GREEN = (0, 255, 0)
        self.RED = (255, 0, 0)

        #Resolution and size + initialize pygame
        self.size = (320,480)
        pygame.init()
        self.screen = pygame.display.set_mode(self.size,pygame.FULLSCREEN)
        self.screen.fill(self.WHITE)

        #topBar
        pygame.draw.rect(self.screen, self.GREEN, (0,0,480,25), 0)

        #First row
        pygame.draw.circle(self.screen, self.RED, (40,180),40, 0)
        pygame.draw.circle(self.screen, self.RED, (120,180),40, 0)
        pygame.draw.circle(self.screen, self.RED, (200,180),40, 0)
        pygame.draw.circle(self.screen, self.RED, (280,180),40, 0)

        #Second row
        pygame.draw.circle(self.screen, self.RED, (40,300),40, 0)
        pygame.draw.circle(self.screen, self.RED, (120,300),40, 0)
        pygame.draw.circle(self.screen, self.RED, (200,300),40, 0)
        pygame.draw.circle(self.screen, self.RED, (280,300),40, 0)

        #Third row
        pygame.draw.circle(self.screen, self.RED, (40,420),40, 0)
        pygame.draw.circle(self.screen, self.RED, (120,420),40, 0)
        pygame.draw.circle(self.screen, self.RED, (200,420),40, 0)
        pygame.draw.circle(self.screen, self.RED, (280,420),40, 0)


#Boot the OS
OS = OSMain()

#load up apps
appController = apps.systemApps()
appController.getAppOrder()

#connect to the GSM module
FONA = serialCon()
FONA.connect()


done = False
clock = pygame.time.Clock()
while not done:
    myfont = pygame.font.SysFont("monospace", 15)
    # render text
    pygame.draw.rect(OS.screen, OS.WHITE, (100,100,200,20), 0)
    label = myfont.render(str(clock.get_fps()), 1, OS.BLACK)
    OS.screen.blit(label, (100, 100))
    
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            print(event.pos)
        if event.type == pygame.QUIT:
            done = True
        if event.type is KEYDOWN and event.key == K_w:
            #Debug to window- uncomment
            pygame.display.set_mode(OS.size)
            #print("YO")
            #done = True
    
    pygame.display.flip()
    clock.tick(60)
print (clock)
pygame.quit()
