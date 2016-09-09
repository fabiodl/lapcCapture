import ctypes
import numpy as np
lib = np.ctypeslib.load_library(
    'usbiomodule', '../helium/bin/util/usbiomodule.so')

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


usbio = Usbio()
usbio.setDirection(1, 0xFF)
usbio.setOutput(1, 0xFF)
