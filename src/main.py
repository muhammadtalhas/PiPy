import pygame, time
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
        print("call from " + str(incomingNumber))
        #main popup area
        pygame.draw.rect(OS.screen, OS.BLACK, (0, 50, 480, 80), 0)
        pygame.draw.rect(OS.screen, (5, 220, 185), (0, 55, 480, 70), 0)

        #answer and ignore buttons
        pygame.draw.rect(OS.screen, OS.GREEN, (0, 90, 160, 35), 0)
        pygame.draw.rect(OS.screen, OS.RED, (160, 90, 160, 35), 0)

        #Incming label
        Font = pygame.font.Font('BebasNeue.otf', 20)
        incomingCallLbl = Font.render("Incoming Call: " + str(incomingNumber), 1, self.BLACK)
        self.screen.blit(incomingCallLbl, (0, 65))


    def OSUpdate(self, FONA):
        pygame.display.flip()
        clock.tick(60)
        self.checkIncoming(FONA)

    def getEvents(self):
        return pygame.event.get()

    def checkIncoming(self, FONA):
        lines = FONA.getLines()
        if self.incomingAcknowledged == True:
            self.incomingAcknowledged = False
            lines = []
            return None
        if "RING\r\n" in lines:
            print("CALL")
            self.incomingAcknowledged = True
            starting = int(time.time())

            extractedRawStr = lines[3]
            extractedNumber = extractedRawStr[6:]
            extractedNumber = extractedNumber[:-1]
            while (int(time.time()) - starting < 45):
                self.callPopUp(extractedNumber)
                pygame.display.flip()
                # Call
        if "+CMTI" in lines:
            # Text
            print("TEXT")
        else:
            print("nothing of value in " + str(lines))


# Boot the OS
OS = OSMain()

# connect to the GSM module
FONA = serialConn.serialCon()
FONA.connect()

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
