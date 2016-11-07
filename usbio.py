import ctypes
import numpy as np
import time
lib = np.ctypeslib.load_library(
    'usbiomodule', '../helium/bin/util/')

lib.setDirection.restype = np.ctypeslib.c_intp
lib.setDirection.argtypes = [
    ctypes.c_void_p,
    ctypes.c_ubyte,
    ctypes.c_ubyte,
]


class Usbio:

    def __init__(self):
        self.usbio = lib.new_usbio()
        if self.usbio == 0:
            raise Exception("Unable to open USBIO")

    def setDirection(self, port, value):
        r = lib.setDirection(self.usbio, port, value)
        if r == -1:
            raise Exception("Error in the execution of setDirection")

    def setOutput(self, port, value):
        r = lib.setOutput(self.usbio, port, value)
        if r == -1:
            raise Exception("Error in the execution of setOutput")


if __name__=="__main__":
    usbio = Usbio()
    for i in range(0,10):
        usbio.setOutput(1, 10*i)
        time.sleep(1)

#usbio.setOutput(1, 100)
