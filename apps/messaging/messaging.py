import json
import topBar, serialConn, pygame
from pygame.locals import *

class app():
    def __init__(self, OS, FONA):
    #def __init__(self):
        self.OS = OS
        self.FONA=FONA
        self.msgObjs = []

        self.font=pygame.font.Font('Roboto-Regular.ttf', 40)
        self.fontBold=pygame.font.Font('Roboto-Bold.ttf', 40)

        self.currentScroll=0

        self.openedConvo=""

    def main(self):
        done = False
        self.OS.screen.fill(self.OS.WHITE)
        while not done:
            self.topBar.tick()
            self.OS.OSUpdate(self.FONA)
            if self.openedConvo != "":
                self.drawMain(self.currentScroll)



    def drawMain(self,firstIndex):
        #scroll up here
        #pos[0] 0 - 320
        #pos[1] 25-50
        pygame.draw.line(self.OS.screen,self.OS.BLACK,(0,50),(320,50),4)
        #pos[0] 0 - 320
        #pos[1] 50-252.5
        phoneNumberOne = self.fontBold.render(self.msgObjs[firstIndex].phone_number, 1, self.BLACK)
        self.OS.screen.blit(phoneNumberOne, (160, 151.25))

        pygame.draw.line(self.OS.screen,self.OS.BLACK,(0,252.5),(320,252.5),1)
        #pos[0] 0 - 320
        #pos[1] 252.5-455
        if len(msgObjs) > 1 and len(msgObjs) != firstIndex+1:
            phoneNumberTwo = self.fontBold.render(self.msgObjs[firstIndex+1].phone_number, 1, self.BLACK)
            self.OS.screen.blit(phoneNumberTwo, (160, 353.75))
        pygame.draw.line(self.OS.screen,self.OS.BLACK,(0,455),(320,455),4)
        #scroll down here
        #pos[0] 0 - 320
        #pos[1] 455-480


    def loadDB(self):
        with open('messageDB.json') as data_file:
            data = json.load(data_file)
            for convo in data["messages"]:
                self.msgObjs.append(convo)

if __name__ == "__main__":
    app = app()
    print(app.msgObjs)
    app.loadDB()
    print(app.msgObjs)

#note
#AT+CMGF=1 enters text mode
#AT+CMGR=X gets texts from slots

#click between