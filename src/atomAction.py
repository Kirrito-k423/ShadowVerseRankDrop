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
matchPageImg = "./Img/match.png"
matchPageRegin = (724,1000,210,60)
matchPage2to1Img = "./Img/match2to1.png"
matchPage2to1Regin = (1000,451,300,100)
reloginImg = "./Img/relogin.png"
reloginRegin = (966, 969, 200, 40)
loginImg = "./Img/login.png"
loginRegin = (230, 778, 62, 62)
chooseCardImg = "./Img/chooseCard.png"
chooseCardRegin = (1790, 259, 58, 58)
OKImg = "./Img/OK.png"
OKRegin = (1219, 820, 100, 30)
matchOKImg = "./Img/matchOK.png"
matchOKRegin = (1722,600,100,50)
rematchImg = "./Img/rematch.png"
rematchRegin = (1150, 994, 180, 40)
matchendImg = "./Img/matchend.png"
matchendRegin = (1717, 580, 130, 55)
matchingImg = "./Img/matching.png"
matchingRegin = (1843, 172, 43, 43)

pairingImg = "./Img/pairing.png"
pairingRegin = (, , , )
quitImg = "./Img/quit.png"
quitRegin = (, , , )
quitConfirmImg = "./Img/quitConfirm.png"
quitConfirmRegin = (, , , )

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
                    OKImg, region=OKRegin, confidence=0.8)
        if location is not None:
            state = "OKPage"
            break
        location = pyautogui.locateCenterOnScreen(
                chooseCardImg, region=chooseCardRegin, confidence=0.8)
        if location is not None:
            state = "chooseCardPage"
            break
        location = pyautogui.locateCenterOnScreen(
            matchPageImg, region=matchPageRegin, confidence=0.8)
        if location is not None:
            state = "matchPage"
            location = pyautogui.locateCenterOnScreen(
                    matchPage2to1Img, region=matchPage2to1Regin, confidence=0.8)
            if location is not None:
                state = "matchPage2to1"
            else:
                state = "matchPage3to1"
            break
        location = pyautogui.locateCenterOnScreen(
            reloginImg, region=reloginRegin, confidence=0.8)
        if location is not None:
            state = "reloginPage"
            break  
        location = pyautogui.locateCenterOnScreen(
            loginImg, region=loginRegin, confidence=0.8)
        if location is not None:
            state = "loginPage"
            break 
        location = pyautogui.locateCenterOnScreen(
            matchOKImg, region=matchOKRegin, confidence=0.8)
        if location is not None:
            state = "matchOKPage"
            break
        location = pyautogui.locateCenterOnScreen(
            rematchImg, region=rematchRegin, confidence=0.8)
        if location is not None:
            state = "rematchPage"
            break 
        location = pyautogui.locateCenterOnScreen(
            matchendImg, region=matchendRegin, confidence=0.8)
        if location is not None:
            state = "matchendPage"
            break
        location = pyautogui.locateCenterOnScreen(
            matchingImg, region=matchingRegin, confidence=0.8)
        if location is not None:
            state = "matching"
            break
        location = pyautogui.locateCenterOnScreen(
            pairingImg, region=pairingRegin, confidence=0.8)
        if location is not None:
            state = "pairing"
            break
        location = pyautogui.locateCenterOnScreen(
            quitImg, region=quitRegin, confidence=0.8)
        if location is not None:
            state = "quitPage"
            break
        location = pyautogui.locateCenterOnScreen(
            quitConfirmImg, region=quitConfirmRegin, confidence=0.8)
        if location is not None:
            state = "quitConfirmPage"
            break
        
    colorPrint("current state: {}".format(state), "cyan")
    return state
