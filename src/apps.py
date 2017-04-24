import pygame
import imp
from pygame.locals import *


class systemApps:
    def __init__(self, OS, FONA):
        self.openedApp = None
        self.openingApp = None
        self.appOrder = self.getAppOrder()
        self.appInstances = []  # wil hold app instances
        self.loadedAppObjects = []
        self.OS = OS
        self.FONA = FONA

    def appClick(self, event):
        if event.type == MOUSEBUTTONDOWN:
            if event.pos[0] > 0 and event.pos[0] < 80:
                if event.pos[1] > 140 and event.pos[1] < 220:
                    print(1)
                    #TODO add these in for other options CONFIRM THAT APP IS LOADED
                    self.loadedAppObjects[0].main()
                    return 1
                if event.pos[1] > 260 and event.pos[1] < 340:
                    print(5)
                    return 5
                if event.pos[1] > 380 and event.pos[1] < 460:
                    print(9)
                    return 9
            if event.pos[0] > 80 and event.pos[0] < 160:
                if event.pos[1] > 140 and event.pos[1] < 220:
                    print(2)
                    return 2
                if event.pos[1] > 260 and event.pos[1] < 340:
                    print(6)
                    return 6
                if event.pos[1] > 380 and event.pos[1] < 460:
                    print(10)
                    return 10
            if event.pos[0] > 160 and event.pos[0] < 240:
                if event.pos[1] > 140 and event.pos[1] < 220:
                    print(3)
                    return 3
                if event.pos[1] > 260 and event.pos[1] < 340:
                    print(7)
                    return 7
                if event.pos[1] > 380 and event.pos[1] < 460:
                    print(11)
                    return 11
            if event.pos[0] > 240 and event.pos[0] < 320:
                if event.pos[1] > 140 and event.pos[1] < 220:
                    print(4)
                    return 4
                if event.pos[1] > 260 and event.pos[1] < 340:
                    print(8)
                    return 8
                if event.pos[1] > 380 and event.pos[1] < 460:
                    print(12)
                    return 12

    def getAppOrder(self):
        fileToRead = open('../apps/order.txt', 'r')
        order = fileToRead.readlines()
        return order

    def importApps(self):
        for string in self.appOrder:
            self.appInstances.append(imp.load_source(string + '.app', '../apps/' + string + '/' + string + '.py'))
        for apps in self.appInstances:
            self.loadedAppObjects.append(apps.app(self.OS, self.FONA))

    def incomingCallInput(self, event):
        if event.type == MOUSEBUTTONDOWN:
            if event.pos[0] > 0 and event.pos[0] < 160:
                if event.pos[1] > 90 and event.pos[1] < 125:
                    self.OS.incomingAcknowledged = False
                    FONA.transmit("ATA")
                    return "ANSWER"
            if event.pos[0] > 160 and event.pos[0] < 320:
                if event.pos[1] > 90 and event.pos[1] < 125:
                    self.OS.incomingAcknowledged = False
                    FONA.transmit("ATH")
                    return "IGNORE"
