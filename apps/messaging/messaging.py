import json
import pygame
import topBar, serialConn
from pygame.locals import *

class app():
    def __init__(self, OS, FONA):
    #def __init__(self):
        self.OS = OS
        self.FONA=FONA
        #todo FOR DRAW DEBUG
        self.topBar = topBar.topBar(OS)

        self.msgObjs = []

        self.font=pygame.font.Font('Roboto-Regular.ttf', 40)
        self.fontBold=pygame.font.Font('Roboto-Bold.ttf', 40)
        self.fontBoldSmall=pygame.font.Font('Roboto-Bold.ttf', 10)


        self.currentScroll=0
        self.tapBuffer = -2

        self.openedConvo=-1

    def main(self):
        self.loadDB()
        done = False
        self.OS.screen.fill(self.OS.WHITE)
        while not done:
            # todo FOR DRAW DEBUG
            self.topBar.tick()
            self.OS.OSUpdate(self.FONA)
            self.OS.screen.fill(self.OS.WHITE)
            if self.openedConvo == -1:
                self.drawMain(self.currentScroll)
            #TODO other views
            # todo FOR DRAW DEBUG
            events = self.OS.getEvents()
            for event in events:
                if event.type == MOUSEBUTTONDOWN:
                    self.tapBuffer=self.clickManager(event)
                    if self.tapBuffer == -1:
                        self.tapBuffer = -2
                        done = True
                    if self.tapBuffer == 0:
                        self.currentScroll -= 2
                        if self.currentScroll < 0:
                            self.currentScroll = 0
                        self.tapBuffer = -2
                    if self.tapBuffer == 1:
                        self.openedConvo = self.currentScroll
                        self.tapBuffer = -2
                    if self.tapBuffer == 2:
                        if(len(self.msgObjs)<self.currentScroll+1):
                            self.openedConvo = self.currentScroll+1
                        self.tapBuffer = -2
                    if self.tapBuffer == 3:
                        if(len(self.msgObjs)>self.currentScroll+2):
                            self.currentScroll += 2
                        else:
                            self.currentScroll = 0
                        self.tapBuffer = -2

    def drawMain(self,firstIndex):
        #scroll up here
        #pos[0] 0 - 320
        #pos[1] 25-50
        upArrow = self.fontBoldSmall.render(u"\u25B2", 1, self.OS.BLACK)
        self.OS.screen.blit(upArrow, (37.5, 151.25))

        #back button
        pygame.draw.rect(self.OS.screen, self.OS.RED,  [0, 25, 50, 25])

        pygame.draw.line(self.OS.screen,self.OS.BLACK,(0,50),(320,50),4)
        #pos[0] 0 - 320
        #pos[1] 50-252.5

        phoneNumberOne = self.fontBold.render(self.msgObjs[firstIndex]['phone_number'], 1, self.OS.BLACK)
        self.OS.screen.blit(phoneNumberOne, (0, 151.25))

        pygame.draw.line(self.OS.screen,self.OS.BLACK,(0,252.5),(320,252.5),1)
        #pos[0] 0 - 320
        #pos[1] 252.5-455

        if len(self.msgObjs) > 1 and len(self.msgObjs) != firstIndex+1:
            phoneNumberTwo = self.fontBold.render(self.msgObjs[firstIndex+1]['phone_number'], 1, self.OS.BLACK)
            self.OS.screen.blit(phoneNumberTwo, (0, 353.75))

        pygame.draw.line(self.OS.screen,self.OS.BLACK,(0,455),(320,455),4)
        #scroll down here
        #pos[0] 0 - 320
        #pos[1] 455-480
        downArrow = self.fontBoldSmall.render(u"\u25BC", 1, self.OS.BLACK)
        self.OS.screen.blit(downArrow, (467.5, 151.25))

    def clickManager(self,event):
        #-1 is back
        #0 is scroll up
        #1 is first box
        #2 is second box
        #3 is scroll down
          if event.type == MOUSEBUTTONDOWN:
            if event.pos[0] >= 0 and event.pos[0] <= 320:
                #special case for back
                if event.pos[0]>0 and event.pos[0]<50:
                    if event.pos[1]>25 and event.pos[1]<50:
                        return -1
                if event.pos[1] > 0 and event.pos[1] < 50:
                    return 0
                if event.pos[1] > 50 and event.pos[1] < 252.50:
                    return 1
                if event.pos[1] > 252.50 and event.pos[1] < 455:
                    return 2
                if event.pos[1] > 455 and event.pos[1] < 480:
                    return 3
            else:
                return -2

    def loadDB(self):
        #TODO do a search for ".." and make everything full path. Relative will break stuff dependign on enviorment
        with open('../apps/messaging/messageDB.json') as data_file:
            data = json.load(data_file)
            for convo in data["messages"]:
                self.msgObjs.append(convo)

if __name__ == "__main__":
    class OS():
        def __init__(self):
            self.size = (320, 480)
            pygame.init()
            self.screen = pygame.display.set_mode(self.size, pygame.FULLSCREEN)
            self.BLACK = (0, 0, 0)
            self.WHITE = (255, 255, 255)
            self.GREEN = (0, 255, 0)
            self.RED = (255, 0, 0)
            self.BLUE = (0, 0, 255)
            self.clock = pygame.time.Clock()

        def OSUpdate(self, FONA):
            pygame.display.flip()
            self.clock.tick(60)
    os = OS()
    fona = None
    app = app(os,fona)
    pygame.display.set_mode(os.size)
    while True:
        app.main()



#notes
#AT+CMGF=1 enters text mode
#AT+CMGR=X gets texts from slots

#click between