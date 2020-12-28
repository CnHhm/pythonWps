import threading

# def SetTimer():
# 	print('the time is up. my time is now.')

# timer = threading.Timer(5, SetTimer);
# timer.start();

def SetTimers():
	print('the time is up. my time is now.')
	global timer;
	timer = threading.Timer(1,SetTimers);
	timer.start();

timer = threading.Timer(1,SetTimers);
timer.start();

import time
time.sleep(5) # 15秒后停止定时器
# import sys
# sys.exit(0);
import os
os._exit(0);
# timer.cancel()