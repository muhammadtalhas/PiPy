import topBar, serialConn, pygame
from pygame.locals import *

class app():
    def __init__(self, OS, FONA):
        print ("Phone has initiated")
        self.OS = OS
        self.FONA=FONA
        self.topBar = topBar.topBar(OS)
        self.active = False

    def main(self):
        self.OS.screen.fill(self.OS.WHITE)
        
        done = False
        number = ""
        while not done:
            self.topBar.tick()
            self.OS.OSUpdate(self.FONA, events)
            self.screenDraw(number)
            events = self.OS.getEvents()
            for event in events:
                if event.type == MOUSEBUTTONDOWN:
                    clicked = -2
                    print("In Phone App")
                    print(event.pos)
                    clicked = self.readClicks(event)
                    if clicked >= 0 and clicked < 10:
                        number += str(clicked)
                    if clicked == -1:
                        if self.active == True:
                            self.active = False

                            self.FONA.transmit("ATH")
                        if len(number) <=0:
                            done= True
                        else:
                            number = number[:-1]
                    if clicked == 10:
                        self.active = True
                        self.FONA.transmit("ATD"+number+";")
                        
            
    def screenDraw(self, number):
        #First Row
        pygame.draw.rect(self.OS.screen, self.OS.BLUE,  [20, 120, 64, 64])
        pygame.draw.rect(self.OS.screen, self.OS.BLUE,  [128, 120, 64, 64])
        pygame.draw.rect(self.OS.screen, self.OS.BLUE,  [236, 120, 64, 64])
        #Second Row
        pygame.draw.rect(self.OS.screen, self.OS.BLUE,  [20, 200, 64, 64])
        pygame.draw.rect(self.OS.screen, self.OS.BLUE,  [128, 200, 64, 64])
        pygame.draw.rect(self.OS.screen, self.OS.BLUE,  [236, 200, 64, 64])        
        #Third Row
        pygame.draw.rect(self.OS.screen, self.OS.BLUE,  [20, 280, 64, 64])
        pygame.draw.rect(self.OS.screen, self.OS.BLUE,  [128, 280, 64, 64])
        pygame.draw.rect(self.OS.screen, self.OS.BLUE,  [236, 280, 64, 64])  
        #Fourth Row
        pygame.draw.rect(self.OS.screen, self.OS.RED,  [20, 360, 64, 64])
        pygame.draw.rect(self.OS.screen, self.OS.BLUE,  [128, 360, 64, 64])
        pygame.draw.rect(self.OS.screen, self.OS.GREEN,  [236, 360, 64, 64])

        pygame.draw.rect(self.OS.screen, self.OS.WHITE,  [self.OS.size[0]/4, 50, self.OS.size[0], 50])

        #draw number
        timeFont = pygame.font.Font('BebasNeue.otf', 40)
        strLabel = timeFont.render(number, 1, self.OS.BLACK)
        self.OS.screen.blit(strLabel, (self.OS.size[0]/4, 50))

    def readClicks(self, event):
        if event.type == MOUSEBUTTONDOWN:
            print("In Phone App")
            print(event.pos)
            #first col
            if event.pos[0] > 20 and event.pos[0] < 84:
                if event.pos[1] > 120 and event.pos[1] < 184:
                    print(1)
                    return 1
                if event.pos[1] > 200 and event.pos[1] < 264:
                    print(4)
                    return 4
                if event.pos[1] > 280 and event.pos[1] < 344:
                    print(7)
                    return 7
                if event.pos[1] >360 and event.pos[1] < 424:
                    print(-1)
                    return -1
            if event.pos[0] > 128 and event.pos[0]< 192:
                if event.pos[1] > 120 and event.pos[1] < 184:
                    print(2)
                    return 2
                if event.pos[1] > 200 and event.pos[1] < 264:
                    print(5)
                    return 5
                if event.pos[1] > 280 and event.pos[1] < 344:
                    print(8)
                    return 8
                if event.pos[1] >360 and event.pos[1] < 424:
                    print(0)
                    return 0
            if event.pos[0] > 236 and event.pos[0]< 300:
                if event.pos[1] > 120 and event.pos[1] < 184:
                    print(3)
                    return 3
                if event.pos[1] > 200 and event.pos[1] < 264:
                    print(6)
                    return 6
                if event.pos[1] > 280 and event.pos[1] < 344:
                    print(9)
                    return 9
                if event.pos[1] >360 and event.pos[1] < 424:
                    print(10)
                    return 10
            return -2
        return -2