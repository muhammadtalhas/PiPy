import pygame
from datetime import datetime


class topBar:
    def __init__(self, OS):
        self.OSConnector = OS
        pygame.draw.rect(OS.screen, OS.GREEN, (0,0,480,25), 0)
        
    def tick(self):
        if self.OSConnector.incomingAcknowledged == True:
            pygame.draw.rect(self.OSConnector.screen, self.OSConnector.BLUE, (0,0,480,25), 0)
        else:
            pygame.draw.rect(self.OSConnector.screen, self.OSConnector.GREEN, (0,0,480,25), 0)
        now = datetime.now()
        strTim = now.strftime('%H:%M')
        timeFont = pygame.font.Font('alarm clock.ttf', 15)
        strLabel = timeFont.render(strTim, 1, self.OSConnector.BLACK)
        self.OSConnector.screen.blit(strLabel, (250, 5))
