import pygame, time, json
from pygame.locals import *
import apps, topBar, serialConn


class OSMain:
    def __init__(self):
        # colors
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.GREEN = (0, 255, 0)
        self.RED = (255, 0, 0)
        self.BLUE = (0, 0, 255)

        self.incomingAcknowledged = False
        self.acknowledgedTime = -1
        self.internalTimer = 0
        self.incomingNumber = ""

        # Resolution and size + initialize pygame
        self.size = (320, 480)
        pygame.init()
        self.screen = pygame.display.set_mode(self.size, pygame.FULLSCREEN)
        # self.screen.fill(self.WHITE)

    def drawMainMenu(self):
        # topBar
        # pygame.draw.rect(self.screen, self.GREEN, (0,0,480,25), 0)
        # First row
        self.screen.fill(self.WHITE)

        #incoming call popup
        if self.incomingAcknowledged == True:
            #self.callPopUp(self.incomingNumber)
            # print("call from " + str(incomingNumber))
            # main popup area
            print("PLACING POPUP")
            pygame.draw.rect(OS.screen, OS.BLACK, (0, 50, 480, 80), 0)
            pygame.draw.rect(OS.screen, (5, 220, 185), (0, 55, 480, 70), 0)

            # answer and ignore buttons
            pygame.draw.rect(OS.screen, OS.GREEN, (0, 90, 160, 35), 0)
            pygame.draw.rect(OS.screen, OS.RED, (160, 90, 160, 35), 0)

            # Incming label
            Font = pygame.font.Font('BebasNeue.otf', 20)
            incomingCallLbl = Font.render("Incoming Call: " + str(self.incomingNumber), 1, self.BLACK)
            self.screen.blit(incomingCallLbl, (0, 65))
        else:
            self.incomingNumber = ""

        pygame.draw.circle(self.screen, self.RED, (40, 180), 40, 0)
        pygame.draw.circle(self.screen, self.RED, (120, 180), 40, 0)
        pygame.draw.circle(self.screen, self.RED, (200, 180), 40, 0)
        pygame.draw.circle(self.screen, self.RED, (280, 180), 40, 0)

        # Second row
        pygame.draw.circle(self.screen, self.RED, (40, 300), 40, 0)
        pygame.draw.circle(self.screen, self.RED, (120, 300), 40, 0)
        pygame.draw.circle(self.screen, self.RED, (200, 300), 40, 0)
        pygame.draw.circle(self.screen, self.RED, (280, 300), 40, 0)

        # Third row
        pygame.draw.circle(self.screen, self.RED, (40, 420), 40, 0)
        pygame.draw.circle(self.screen, self.RED, (120, 420), 40, 0)
        pygame.draw.circle(self.screen, self.RED, (200, 420), 40, 0)
        pygame.draw.circle(self.screen, self.RED, (280, 420), 40, 0)

        # test area


    def callPopUp(self, incomingNumber):
        # print("call from " + str(incomingNumber))
        # main popup area
        pygame.draw.rect(OS.screen, OS.BLACK, (0, 50, 480, 80), 0)
        pygame.draw.rect(OS.screen, (5, 220, 185), (0, 55, 480, 70), 0)

        # answer and ignore buttons
        pygame.draw.rect(OS.screen, OS.GREEN, (0, 90, 160, 35), 0)
        pygame.draw.rect(OS.screen, OS.RED, (160, 90, 160, 35), 0)

        # Incming label
        Font = pygame.font.Font('BebasNeue.otf', 20)
        incomingCallLbl = Font.render("Incoming Call: " + str(incomingNumber), 1, self.BLACK)
        self.screen.blit(incomingCallLbl, (0, 65))


    def OSUpdate(self, FONA):
        pygame.display.flip()
        clock.tick(60)
        if self.internalTimer == 0:
            self.checkIncoming(FONA)
        elif int(time.time()) - self.internalTimer > 10 and self.incomingAcknowledged == False:
            print("running Check")
            self.internalTimer = int(time.time())
            self.checkIncoming(FONA)

    def getEvents(self):
        return pygame.event.get()

    def checkIncoming(self, FONA):
        lines = FONA.getLines()
        print(lines)
        #if self.incomingAcknowledged == True:
        #    self.incomingAcknowledged = False
        #    lines = []
        #    return None
        if "RING\r\n" in lines:
            print("CALL")
            self.incomingAcknowledged = True
            starting = int(time.time())

            extractedRawStr = lines[3]
            extractedNumber = extractedRawStr[6:]
            extractedNumber = extractedNumber[:-1]
            self.incomingNumber=extractedNumber
            #print("Starting loop for popup")
            #while int(time.time()) - starting < 45:
            #    self.callPopUp(extractedNumber)
            #    pygame.display.flip()
            #    for event in events:
            #        print(str(event.type) + str(event.pos))
            #        if event.type == MOUSEBUTTONDOWN:
            #            if event.pos[0] > 0 and event.pos[0] < 160:
            #                if event.pos[1] > 90 and event.pos[1] < 125:
            #                    FONA.transmit("ATA")
            #            if event.pos[0] > 160 and event.pos[0] < 320:
            #                if event.pos[1] > 90 and event.pos[1] < 125:
            #                    FONA.transmit("ATH")
            #                    break
            #    clock.tick(60)
                # Call
        if any("+CMTI" in data for data in lines):
            # Text
            print("Text recieved")
            #todo temp solution. sucks
            done = False
            pointer = 1
            while not done:
                print("AT+CMGR="+str(pointer))
                res = FONA.transmit("AT+CMGR="+str(pointer))
                print("res "+ str(res))
                if len(res) == 2:
                    done = True
                else:
                    print("this is proper")
                    print(str(res))
                    print("res 3: "+str(res[3]))
                    msgIndex = (len(res)-1)-2
                    msgData = res[msgIndex]
                    number = res[2]
                    dbLoad = self.getDBObj()
                    self.updateDB(dbLoad, number,msgData)
                    pointer +=1
        #else:
            #print("nothing of value in " + str(lines))
    def getDBObj(self):
        with open('../apps/messaging/messageDB.json') as data_file:
            data = json.load(data_file)
        return data

    def updateDB(self,db, number, data):
        entry ={"time":"0","data":data,"type":"IN"}
        foundAt = -1
        for index in range(0, len(db["messages"])-1):
            if db["messages"][index]["phone_number"] == str(number):
                foundAt = index
                break
            else:
                pass

        if foundAt == -1:
            print("new number")
            newObj = {"phone_number":str(number),"msgs":[entry]}
            db["messages"].append(newObj)
        else:
            print("old number")
            db["messages"][foundAt]["msgs"].append(entry)

        print("new db " + str(db))
        with open("../apps/messaging/messageDB.json", "w") as data_file:
            data_file.seek(0)  # rewind
            json.dump(db, data_file)
            data_file.truncate()

# Boot the OS
OS = OSMain()

# connect to the GSM module
FONA = serialConn.serialCon()
FONA.connect()

# setup FONA
FONA.transmit("AT+CHFA=1")
FONA.transmit("AT+CMIC=0,15")#test headphones
FONA.transmit("AT+CMGF=1")

# load up apps
appController = apps.systemApps(OS, FONA)
appController.getAppOrder()
appController.importApps()

topBar = topBar.topBar(OS)

done = False
clock = pygame.time.Clock()
while not done:
    # fps data--debug
    # myfont = pygame.font.SysFont("monospace", 15)
    # pygame.draw.rect(OS.screen, OS.WHITE, (100,100,200,20), 0)
    # label = myfont.render(str(clock.get_fps()), 1, OS.BLACK)
    # OS.screen.blit(label, (100, 100))
    events = OS.getEvents()
    OS.drawMainMenu()
    topBar.tick()
    for event in events:
        if event.type == MOUSEBUTTONDOWN:
            if OS.incomingAcknowledged:
                print("events relayed to popup")
                appController.incomingCallInput(event)
            else:
                appController.appClick(event)
            print(event.pos)
        if event.type == pygame.QUIT:
            done = True
        if event.type is KEYDOWN and event.key == K_w:
            # Debug to window- uncomment
            pygame.display.set_mode(OS.size)
            # done = True

    # pygame.display.flip()
    OS.OSUpdate(FONA)
print(clock)
pygame.quit()


