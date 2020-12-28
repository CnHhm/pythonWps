import win32api
import win32con
# import win32gui
import pyperclip
import time
#int = ShellExecute(hwnd, op , file , params , dir , bShow )
win32api.ShellExecute(0, 'open', r'C:\Users\hmhu\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Google Chrome','','',win32con.SW_SHOWMAXIMIZED);
time.sleep(2);
# 获取鼠标当前位置的坐标
print(win32api.GetCursorPos());
# 将鼠标移动到坐标处
win32api.SetCursorPos((468, 52));
# 左点击
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 468, 52, 0, 0)
# # 右点击
# win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 100, 100, 0, 0)

pyperclip.copy("www.baidu.com");
win32api.keybd_event(17,0,0,0) # Ctrl
win32api.keybd_event(86,0,0,0) # v
win32api.keybd_event(86,0,win32con.KEYEVENTF_KEYUP,0) #释放按键
win32api.keybd_event(17,0,win32con.KEYEVENTF_KEYUP,0) #释放按键

win32api.keybd_event(13,0,0,0) # v
win32api.keybd_event(13,0,win32con.KEYEVENTF_KEYUP,0) #释放按键
time.sleep(5);
# 将鼠标移动到坐标处
win32api.SetCursorPos((735, 353));
time.sleep(1);
# # 左点击,这里左点击时百度搜索框失去了激活状态
# win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 870, 358, 0, 0);
# time.sleep(3);
pyperclip.copy("test");
win32api.keybd_event(17,0,0,0) # Ctrl
win32api.keybd_event(86,0,0,0) # v
win32api.keybd_event(86,0,win32con.KEYEVENTF_KEYUP,0) #释放按键
win32api.keybd_event(17,0,win32con.KEYEVENTF_KEYUP,0) #释放按键

win32api.keybd_event(13,0,0,0) # v
win32api.keybd_event(13,0,win32con.KEYEVENTF_KEYUP,0) #释放按键
print("program finish.");
# pyperclip.paste();