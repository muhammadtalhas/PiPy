import topBar, serialConn
class app():
    def __init__(self, OS, FONA):
        print ("Phone has initiated")
        self.OS = OS
        self.FONA=FONA
    def main(self):
        self.screenDraw()
        exit = False
        while exit!=True:
            topBar.tick()
            
    def screenDraw(self):
        self.OS.screen.fill(self.OS.WHITE)
        
        
