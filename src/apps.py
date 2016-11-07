import pygame
import imp
from pygame.locals import *

class systemApps:
    def __init__(self):
        self.openedApp = None
        self.openingApp = None
        self.appOrder = self.getAppOrder()
        self.appInstances = None #wil hold app instances

    def appClick(self, event):
        if event.type == MOUSEBUTTONDOWN:
            if event.pos[0] > 0 and event.pos[0] < 80:
                if event.pos[1] > 140 and event.pos[1] < 220:
                    print(1)
                if event.pos[1] > 260 and event.pos[1] < 340:
                    print(5)
                if event.pos[1] > 380 and event.pos[1] < 460:
                    print(9)
    def getAppOrder(self):
        fileToRead = open('../apps/order.txt', 'r')
        order = fileToRead.readlines()
        return order

#    def importApps(self):
 #       for string in self.appOrder:
            #imps go here
