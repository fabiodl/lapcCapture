#from usbio import Usbio
from lapcCapt import  LapcCapt

class Usbio:
    PORTB=1
    PORTC=2
    def setDirection(self,port,val):
        pass

    def setOutput(self,port,val):
        pass


class UsbioNum:
    def __init__(self):
        self.usbio=Usbio()
        self.usbio.setDirection(Usbio.PORTB,0x3F)
        self.usbio.setDirection(Usbio.PORTC,0x0C)

    def put(self,val):
        self.usbio.setOutput(Usbio.PORTB,val&0x3F)
        self.usbio.setOutput(Usbio.PORTC,(val&0xC0)>>4)


unum=UsbioNum()
for i in range(0,256):
    unum.put(i)
