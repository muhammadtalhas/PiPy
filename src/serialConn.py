import serial

class serialCon():
    def __init__(self):
        self.baudRate = 115200
        self.connected = False

    def connect(self):

        self.serialPort = serial.Serial("/dev/ttyAMA0", self.baudRate, timeout=0.5)
        self.serialPort.write('AT\r')
        response = self.serialPort.readlines()
        for i in range(len(reply)):
            reply[i] = reply[i].rstrip()
        
        if 'OK' in response:
            print ("Conected to FONA and recieved proper response")
            self.connected = True
        else:
            print ("Proper response was not recieved from FONA [on ttyAMA0, baud rate at " + self.baudRate + "timed out after 0.5 seconds")

    def transmit(self, data):
        self.serialPort.write(data + '\r')
        feed = self.serialPort.readlines()
        for i in range(len(feed)):
            feed[i] = feed[i].rstrip()
        return feed

    def terminate(self):
        self.serialPort.close()
        
if __name__ == '__main__':
    test = serialCon()
    test.connect()
