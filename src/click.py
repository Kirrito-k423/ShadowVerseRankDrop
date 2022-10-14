
import pyautogui
import random
from tsjPython.tsjCommonFunc import *
from basicClass import position

def randomShift(pixel):
    return position(random.randint(-pixel, pixel), random.randint(-pixel, pixel))

def clickAbsolute(absolutePos):
    ic(absolutePos)
    sleepRandom(1)
    absolutePos = absolutePos + randomShift(5)
    pyautogui.click(absolutePos.x, absolutePos.y, clicks=1,
                    interval=0.2, duration=0.2, button="left")
    mouseMoveAway()

def mouseMoveAway():
    pyautogui.moveTo(1, 1, 0.1)

def quickClickAbsolute(absolutePos):
    ic(absolutePos)
    sleepRandom(0.5)
    absolutePos = absolutePos + randomShift(5)
    pyautogui.click(absolutePos.x, absolutePos.y, clicks=1,
                    interval=0.2, duration=0.2, button="left")
    mouseMoveAway()

# def mouseMove(x, y):
#     sleepRandom(1)
#     centerPos = origin + shiftCenter + randomShift(15)
#     moveDirection = position(x, y) + randomShift(15)
#     beginPos = centerPos - moveDirection
#     finalPos = centerPos + moveDirection
#     print(centerPos)
#     # 800,900表示鼠标拖拽的起始位置，0.2设置鼠标移动快慢
#     pyautogui.moveTo(beginPos.x, beginPos.y, 0.2)
#     # 200,200表示鼠标拖拽的终点位置，0.2设置鼠标拖拽的快慢，“easeOutQuad”表示鼠标拖动先快后慢（多种拖拽方式可选）
#     pyautogui.dragTo(finalPos.x, finalPos.y, 2, pyautogui.easeOutQuad)
#     # pyautogui.click(centerPos.x, centerPos.y)  # 鼠标移动到