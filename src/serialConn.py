import serial

class serialCon():
    def __init__(self):
        self.baudRate = 115200
        self.connected = False


    def connect(self):
        self.serialPort = serial.Serial("/dev/ttyAMA0", self.baudRate, timeout=0.5)
        self.serialPort.write('AT\r')
        response = self.serialPort.readlines()
        for i in range(len(response)):
            response[i] = response[i].rstrip()

        if 'OK' in response:
            print ("Connected to FONA and received proper response")
            self.connected = True
        else:
            print ("Proper response was not recieved from FONA [on ttyAMA0, baud rate at " + str(self.baudRate) + "timed out after 0.5 seconds")

    def transmit(self, data):
        self.serialPort.write(data + '\r')
        feed = self.serialPort.readlines()
        for i in range(len(feed)):
            feed[i] = feed[i].rstrip()
        return feed

    def terminate(self):
        self.serialPort.close()
        self.connected = False

    def getLines(self):
        response = self.serialPort.readlines()
        #print (response)
        return response
        
        
if __name__ == '__main__':
        # OS = OSMain()

    # connect to the GSM module
    FONA = serialCon()
    FONA.connect()
    FONA.transmit("AT+CMGF=1")

    res = FONA.transmit("AT+CMGR=2")
    print(res)

    #test = serialCon()
    #test.connect()

    #while (True):
    #    test.getLines()
