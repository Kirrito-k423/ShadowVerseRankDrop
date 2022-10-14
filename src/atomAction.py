import pyautogui
from tsjPython.tsjCommonFunc import *

# def openMap():
#     splitLine("openMap")
#     clickShift(shiftMap)
#     waitPageChangeTo("map")


# def openJobPage():
#     splitLine("openJobPage")
#     clickShift(shiftJobIcon)
#     waitPageChangeTo("jobPage")


# def exitJobPage():
#     splitLine("exitJobPage")
#     keyExit()
#     waitPageChangeTo("mainPage")


# def checkPicExists(Img, region, confidence):
#     # ,region 4-integer tuple of (left, top, width, height))
#     location = pyautogui.locateCenterOnScreen(
#         Img, region=region, confidence=confidence)
#     if location is not None:
#         passPrint("{} is Existed ({},{})".format(Img, location.x, location.y))
#     else:
#         errorPrint("{} is NOT Existed".format(Img))
#     return location


# def waitPageChangeTo(page):
#     while getState() != page:
#         print("waitPageChangeTo {}".format(page))


# def posDistance(a, b):
#     return (a.x-b.x)*(a.x-b.x)+(a.y-b.y)*(a.y-b.y)


# def awakeJob():
#     splitLine("awakeJob")
#     quickClickAbsolute(absoluteAwakeJob)
#     mouseClear()

decideMainIconImg = "./Img/main.png"
decideMainIconRegin = (247, 1006, 200, 50)
matchImg = "./Img/match.png"
matchRegin = ()

def getCurrentState():
    state = "loading"
    while state == "loading":
        ic("state check…………")
        location = pyautogui.locateCenterOnScreen(
            decideMainIconImg, region=decideMainIconRegin, confidence=0.8)
        if location is not None:
            state = "mainPage"
            break
        location = pyautogui.locateCenterOnScreen(
            matchImg, region=matchRegin, confidence=0.8)
        if location is not None:
            state = "jobPage"
            break
        
    colorPrint("current state: {}".format(state), "cyan")
    return state
