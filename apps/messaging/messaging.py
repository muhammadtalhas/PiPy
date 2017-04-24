import topBar, serialConn, pygame
from pygame.locals import *

class app():
    def __init__(self, OS, FONA):
        self.OS = OS
        self.FONA=FONA

    def main(self):
        self.OS.screen.fill(self.OS.WHITE)
        while not done:
            self.topBar.tick()