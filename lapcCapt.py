import numpy as np
import time
import win32com
import win32com.client
import win32gui
from PIL import ImageGrab
import datetime


def callback(hwnd,cbData):
    tit=win32gui.GetWindowText(hwnd)
    if tit.startswith(cbData.title):
        cbData.handle=hwnd
       
def getWindowHandle(title):
    class CbData:
        pass
    cbData=CbData()
    cbData.title=title
    cbData.handle=None
    win32gui.EnumWindows(callback, cbData)
    return cbData.handle



def getStatus(hwnd):
    rect = win32gui.GetWindowRect(hwnd)
    dx=-182
    dy=-26
    sx=70
    sy=19
    # print(rect)
    bbox=(rect[2]+dx,rect[3]+dy,rect[2]+dx+sx,rect[3]+dy+sy)
    img=ImageGrab.grab(bbox)
    # img.save("c:/out/screen.png")
    return np.array(img)


def getLoadingWin(hwnd):
    rect = win32gui.GetWindowRect(hwnd)
    dx=0
    dy=0
    sx=100
    sy=100

    x=(rect[0]+rect[2])/2+dx
    y=(rect[1]+rect[3])/2+dy
    
    # print(rect)
    bbox=(x-sx/2,y-sy/2,x+sx/2,y+sy/2)
    img=ImageGrab.grab(bbox)
    # img.save("c:/out/screen.png")
    return np.array(img)


def imgDiff(im1,im2):
     return np.sum(np.abs(im1-im2))


def waitDisappearance(hwnd,getter,refImg,label=""):
    while imgDiff(getter(hwnd),refImg)<10:
        time.sleep(0.2)
    print(label+" started")
    while imgDiff(getter(hwnd),refImg)>10:
        time.sleep(0.2)
    print(label+" ended")

def acquire(shell,hwnd):
    imEnd=getStatus(hwnd)
    shell.SendKeys("{F5}", 0)
    waitDisappearance(hwnd,getStatus,imEnd,"acquisition")


def save(shell,hwnd,filename):
    imGraph=getLoadingWin(hwnd)
    print("opening")
    shell.SendKeys("^+E")
    time.sleep(1)
    print("sending filename",filename)
    for i in range(0,6):        
        shell.SendKeys("{TAB}")
    for c in filename:
        shell.SendKeys(c)
    shell.SendKeys("{ENTER}")
    waitDisappearance(hwnd,getLoadingWin,imGraph,"save")
    
title="ZEROPLUS-LAP-C"
shell = win32com.client.Dispatch('WScript.Shell')
shell.AppActivate(title)
hwnd=getWindowHandle(title)

suffix=datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

time.sleep(0.4)
acquire(shell,hwnd)
save(shell,hwnd,"hello"+suffix)



