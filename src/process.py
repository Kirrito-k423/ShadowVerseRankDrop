import sys
import re
import win32api
import win32con
import win32gui
import win32com.client
import global_variable as glv
from tsjPython.tsjCommonFunc import *

def kill_process_by_name(pname):
    cmd = 'taskkill /F /IM ' + pname
    os.system(cmd)

def windows_turn_on_mumu():
    win32api.ShellExecute(0, 'open', r'E:/Desktop/影之诗-MuMu模拟器.lnk', '','',1)

def find_mumu_process():
    origin=glv._get("mumu_start_coordinate")
    if reset_window_pos(origin.x, origin.y, glv._get("mumu_regex_name")) == 0:
        errorPrint("not found process! over")
        return 0
    passPrint("STEP1: find & set mumu simulator")
    return 1

def reset_window_pos(x, y, reName):
    hWndList = []
    win32gui.EnumWindows(lambda hWnd, param: param.append(hWnd), hWndList)
    # print(hWndList)
    count=0
    for hwnd in hWndList:
        clsname = win32gui.GetClassName(hwnd)
        title = win32gui.GetWindowText(hwnd)
        if(re.match("(.)*{}(.)*".format(reName), clsname, re.IGNORECASE) or re.match("(.)*{}(.)*".format(reName), title, re.IGNORECASE)):
            ic(clsname)
            ic(title)
            left, top, right, bottom = win32gui.GetWindowRect(hwnd)
            height = bottom - top
            width = right - left
            ic("height {} width {}".format(height, width))
            ic(glv._get("mumu_hight_width").y)
            ic(glv._get("mumu_hight_width").x)
            if height == glv._get("mumu_hight_width").x and width == glv._get("mumu_hight_width").y:
                count+=1
            win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, x,
                                  y, glv._get("mumu_hight_width").y, glv._get("mumu_hight_width").x, win32con.SWP_SHOWWINDOW)
            win32gui.BringWindowToTop(hwnd)
            # 先发送一个alt事件，否则会报错导致后面的设置无效：pywintypes.error: (0, 'SetForegroundWindow', 'No error message is available')
            shell = win32com.client.Dispatch("WScript.Shell")
            shell.SendKeys('%')
            win32gui.SetForegroundWindow(hwnd)
    if count==0:
        return 0
    else:
        return 1