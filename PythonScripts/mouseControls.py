import win32con, win32api
import time

time.sleep(5)
print("Moving Mouse Now")
win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 100, 1, 0, 0)