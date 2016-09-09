import win32gui
flags, hcursor, (x,y) = win32gui.GetCursorInfo()
print(x,y)
