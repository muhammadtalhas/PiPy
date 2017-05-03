import json
import pygame
#TODO FIX
import topBar, serialConn
from pygame.locals import *

class app():
    def __init__(self, OS, FONA):
    #def __init__(self):
        self.OS = OS
        self.FONA=FONA
        # todo FOR DRAW DEBUG
        self.topBar = topBar.topBar(OS)

        self.msgObjs = []

        self.font = pygame.font.Font('Roboto-Regular.ttf', 40)
        self.fontSmall = pygame.font.Font('Roboto-Regular.ttf', 10)
        self.fontSmallBold = pygame.font.Font('Roboto-Bold.ttf', 10)

        self.fontBold=pygame.font.Font('Roboto-Bold.ttf', 40)
        self.fontBoldSmall=pygame.font.Font('Roboto-Bold.ttf', 20)

        self.fontThirty=pygame.font.Font('Roboto-Bold.ttf', 30)

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
            else:
                self.initConvoScreen(self.msgObjs[self.openedConvo])
            # todo FOR DRAW DEBUG
            events = self.OS.getEvents()
            for event in events:
                if event.type == MOUSEBUTTONDOWN:
                    self.tapBuffer=self.clickManagerMain(event)
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
    def initConvoScreen(self,convoObj):
        done = False
        currentScroll = 0
        unloadedMsgs = convoObj["msgs"]
        pagedMsgs=[]

        tempChunk = []
        for msg in unloadedMsgs[::-1]:
            if len(tempChunk) == 13:
                pagedMsgs.append(tempChunk)
                tempChunk = []
                tempChunk.append(msg)
            else:
                tempChunk.append(msg)
        pagedMsgs.append(tempChunk)
        self.OS.screen.fill(self.OS.WHITE)
        while not done:
            #todo FOR DRAW DEBug
            self.topBar.tick()
            self.OS.OSUpdate(self.FONA)
            self.OS.screen.fill(self.OS.WHITE)
            self.drawConvoView(convoObj["phone_number"],pagedMsgs,currentScroll)
            events = self.OS.getEvents()
            tap = None
            for event in events:
                if event.type == MOUSEBUTTONDOWN:
                    tap = self.clickManagerConvo(event)
                    if tap == 0:
                        done = True
                    if tap == 1:
                        #TODO invoke new msg view
                        self.initMsgView(convoObj["phone_number"])
                    if tap == 2:
                        if currentScroll +1 <= len(pagedMsgs)-1:
                            currentScroll +=1
                    if tap == 3:
                        if currentScroll-1 >= 0:
                            currentScroll -=1

    def clickManagerConvo(self, event):
        #0 for back
        #1 for new msg
        #2 for up
        #3 for down
        if event.type == MOUSEBUTTONDOWN:
            if event.pos[0] > 0 and event.pos[0] < 320:
                # back button
                if event.pos[0] > 0 and event.pos[0] < 50:
                    if event.pos[1] > 25 and event.pos[1] < 50:
                        return 0
                #new msg
                if event.pos[0] > 270 and event.pos[0]<320:
                    if event.pos[1] > 25 and event.pos[1] < 50:
                        return 1
                #up
                if event.pos[1] > 50 and event.pos[1] < 100:
                    return 2
                #down
                if event.pos[1] > 425 and event.pos[1] <480:
                    return 3
    def drawConvoView(self,number,msgs,scroll):
        #number label
        phoneNumberLbl = self.fontBoldSmall.render(number, 1, self.OS.BLACK)
        phoneNumberLblSize = (phoneNumberLbl.get_width(), phoneNumberLbl.get_height())
        self.OS.screen.blit(phoneNumberLbl, ( (320/2)-(phoneNumberLblSize[0]/2),25))
        #back
        pygame.draw.rect(self.OS.screen, self.OS.RED,  [0, 25, 50, 25])
        #new msg
        pygame.draw.rect(self.OS.screen, self.OS.GREEN,  [275, 25, 50, 25])

        #lines
        pygame.draw.line(self.OS.screen,self.OS.BLACK,(0,50),(320,50),4)
        pygame.draw.line(self.OS.screen,self.OS.BLACK,(0,100),(320,100),1)
        pygame.draw.line(self.OS.screen,self.OS.BLACK,(0,125),(320,125),1)
        pygame.draw.line(self.OS.screen,self.OS.BLACK,(0,150),(320,150),1)
        pygame.draw.line(self.OS.screen,self.OS.BLACK,(0,175),(320,175),1)
        pygame.draw.line(self.OS.screen,self.OS.BLACK,(0,200),(320,200),1)
        pygame.draw.line(self.OS.screen,self.OS.BLACK,(0,225),(320,225),1)
        pygame.draw.line(self.OS.screen,self.OS.BLACK,(0,250),(320,250),1)
        pygame.draw.line(self.OS.screen,self.OS.BLACK,(0,275),(320,275),1)
        pygame.draw.line(self.OS.screen,self.OS.BLACK,(0,300),(320,300),1)
        pygame.draw.line(self.OS.screen,self.OS.BLACK,(0,325),(320,325),1)
        pygame.draw.line(self.OS.screen,self.OS.BLACK,(0,350),(320,350),1)
        pygame.draw.line(self.OS.screen,self.OS.BLACK,(0,375),(320,375),1)
        pygame.draw.line(self.OS.screen,self.OS.BLACK,(0,400),(320,400),1)

        pygame.draw.line(self.OS.screen,self.OS.BLACK,(0,425),(320,425),1)

        offset = 7
        lineToWriteBelow = 400
        for msg in msgs[scroll]:
            if msg["type"]== "IN":
                msgLbl = self.fontSmallBold.render(msg["data"], 1, self.OS.RED)
            if msg["type"] == "OUT":
                msgLbl = self.fontSmall.render(msg["data"], 1, self.OS.BLUE)
            self.OS.screen.blit(msgLbl, (0,lineToWriteBelow+offset))
            lineToWriteBelow -=25

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

    def clickManagerMain(self,event):
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
    def initMsgView(self, number):
        msgStr = ""
        done = False
        while not done:
            tap = -1
            self.OS.OSUpdate(self.FONA)
            self.OS.screen.fill(self.OS.WHITE)
            self.drawMsgView(msgStr)
            events = self.OS.getEvents()
            tap = None
            for event in events:
                if event.type == MOUSEBUTTONDOWN:
                    tap = self.clickManagerType(event)
                    #if tap == "__ENTER__":
                    if tap == "__DEL__":
                        msgStr = msgStr[:-1]
                    elif tap == "__SPACE__":
                        msgStr += " "
                    elif tap == "__SHIFT__":
                        pass
                    elif tap == None:
                        pass
                    else:
                        msgStr += tap




    def drawMsgView(self,msgLbl):
        kb = pygame.image.load("../keyboard.jpg")
        kb.convert()
        self.OS.screen.blit(kb, (0, 0))
        lbl = self.fontThirty.render(msgLbl, 1, self.OS.RED)
        self.OS.screen.blit(pygame.transform.rotate(lbl, -90), (280, 0))

    def clickManagerType(self,event):
        if event.type == MOUSEBUTTONDOWN:
            #kb top row
            if event.pos[0] > 223 and event.pos[0] < 280:
                if event.pos[1] > 0 and event.pos[1] < 50:
                    return "1"
                if event.pos[1] > 50 and event.pos[1] < 97:
                    return "2"
                if event.pos[1] > 97 and event.pos[1] < 145:
                    return "3"
                if event.pos[1] > 145 and event.pos[1] < 193:
                    return "4"
                if event.pos[1] > 193 and event.pos[1] < 242:
                    return "5"
                if event.pos[1] > 242 and event.pos[1] < 296:
                    return "6"
                if event.pos[1] > 296 and event.pos[1] < 336:
                    return "7"
                if event.pos[1] > 336 and event.pos[1] < 385:
                    return "8"
                if event.pos[1] > 385 and event.pos[1] < 433:
                    return "9"
                if event.pos[1] > 433 and event.pos[1] < 480:
                    return "0"
            #kb second row
            if event.pos[0] > 163 and event.pos[0] < 223:
                if event.pos[1] > 0 and event.pos[1] < 50:
                    return "q"
                if event.pos[1] > 50 and event.pos[1] < 97:
                    return "w"
                if event.pos[1] > 97 and event.pos[1] < 145:
                    return "e"
                if event.pos[1] > 145 and event.pos[1] < 193:
                    return "r"
                if event.pos[1] > 193 and event.pos[1] < 242:
                    return "t"
                if event.pos[1] > 242 and event.pos[1] < 296:
                    return "y"
                if event.pos[1] > 296 and event.pos[1] < 336:
                    return "u"
                if event.pos[1] > 336 and event.pos[1] < 385:
                    return "i"
                if event.pos[1] > 385 and event.pos[1] < 433:
                    return "o"
                if event.pos[1] > 433 and event.pos[1] < 480:
                    return "p"
            #kb thrid row
            if event.pos[0] > 101 and event.pos[0] < 163:
                if event.pos[1] > 0 and event.pos[1] < 73.5:
                    return "a"
                if event.pos[1] > 73.5 and event.pos[1] < 121:
                    return "s"
                if event.pos[1] > 121 and event.pos[1] < 169:
                    return "d"
                if event.pos[1] > 169 and event.pos[1] < 217.5:
                    return "f"
                if event.pos[1] > 217.5 and event.pos[1] < 269:
                    return "g"
                if event.pos[1] > 269 and event.pos[1] < 316:
                    return "h"
                if event.pos[1] > 316 and event.pos[1] < 360.5:
                    return "j"
                if event.pos[1] > 360.5 and event.pos[1] < 409:
                    return "k"
                if event.pos[1] > 409 and event.pos[1] < 480:
                    return "l"
            #kb fourth row
            if event.pos[0] > 45 and event.pos[0] < 101:
                if event.pos[1] > 0 and event.pos[1] < 73.5:
                    return "__SHIFT__"
                if event.pos[1] > 73.5 and event.pos[1] < 121:
                    return "z"
                if event.pos[1] > 121 and event.pos[1] < 169:
                    return "x"
                if event.pos[1] > 169 and event.pos[1] < 217.5:
                    return "c"
                if event.pos[1] > 217.5 and event.pos[1] < 269:
                    return "v"
                if event.pos[1] > 269 and event.pos[1] < 316:
                    return "b"
                if event.pos[1] > 316 and event.pos[1] < 360.5:
                    return "n"
                if event.pos[1] > 360.5 and event.pos[1] < 409:
                    return "m"
                if event.pos[1] > 409 and event.pos[1] < 480:
                    return "__DEL__"
            #kb last row
            if event.pos[0] > 0 and event.pos[0] < 45:
                if event.pos[1] > 121 and event.pos[1] < 360.5:
                    return "__SPACE__"
                if event.pos[1] > 360.5 and event.pos[1] < 480:
                    return "__ENTER__"




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

        def getEvents(self):
            return pygame.event.get()
    os = OS()
    fona = None
    app = app(os,fona)
    pygame.display.set_mode(os.size)
    while True:
        os.screen.fill(os.WHITE)
        app.initConvoScreen({
      "phone_number":"7032033596",
      "msgs":[
        {"time":"1493093368","data":"hey","type":"IN"},
        {"time":"1493093401","data":"Hey","type":"OUT"},
        {"time":"1493093402","data":"Come over","type":"IN"},
        {"time":"1493093403","data":"I can't im making a fuckin phone","type":"OUT"},
        {"time":"1493093404","data":"My Parents are't home","type":"IN"},
        {"time":"1493093405","data":"ok so?","type":"OUT"},
        {"time":"1493093368","data":"hey","type":"IN"},
        {"time":"1493093401","data":"Hey","type":"OUT"},
        {"time":"1493093402","data":"Come over","type":"IN"},
        {"time":"1493093403","data":"I can't im making a fuckin phone","type":"OUT"},
        {"time":"1493093404","data":"My Parents are't home","type":"IN"},
        {"time":"1493093405","data":"ok so?","type":"OUT"},
        {"time":"1493093368","data":"hey","type":"IN"},
        {"time":"1493093401","data":"Hey","type":"OUT"},
        {"time":"1493093402","data":"Come over","type":"IN"},
        {"time":"1493093403","data":"I can't im making a fuckin phone","type":"OUT"},
        {"time":"1493093404","data":"My Parents are't home","type":"IN"},
        {"time":"1493093405","data":"ok so?","type":"OUT"},

      ]
    })
        #app.drawConvoView("7032033596",[
        #{"time":"1493093368","data":"hey","type":"IN"},
        #{"time":"1493093401","data":"Hey","type":"OUT"},
        #{"time":"1493093402","data":"Come over","type":"IN"},
        #{"time":"1493093403","data":"I can't im making a fuckin phone","type":"OUT"},
        #{"time":"1493093404","data":"My Parents are't home","type":"IN"},
        #{"time":"1493093405","data":"ok so?","type":"OUT"}
      #],1)
        pygame.display.flip()



#notes
#AT+CMGF=1 enters text mode
#AT+CMGR=X gets texts from slots

#click between