import pyautogui
from tsjPython.tsjCommonFunc import *
import global_variable as glv
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
decideMainIconRegin = (270, 1000, 170, 40)
matchPageImg = "./Img/match.png"
matchPageRegin = (740,1000,150,50)
matchPage2to1Img = "./Img/match2to1.png"
matchPage2to1Regin = (1000,470,150,100)

matchPage2professionImg = "./Img/profession.png"
matchPage2professionRegin = (1000,760,140,80)

matchPage2to1PlusImg = "./Img/match2to1Plus.png"
matchPage2to1PlusRegin = (1550,808,150,30)

reloginImg = "./Img/relogin.png"
reloginRegin = (966, 969, 200, 40)
loginImg = "./Img/login.png"
loginRegin = (242, 768, 67, 67)
userloginImg = "./Img/userlogin.png"
userloginRegin = (1000, 700, 100, 30)

moveCardPageImg = "./Img/moveCardPage.png"
moveCardPageRegin = (255, 670, 20, 30)

chooseCardImg = "./Img/chooseCard.png"
chooseCardRegin = (1790, 270, 50, 40)
OKImg = "./Img/OK.png"
OKRegin = (1212, 812, 120, 40)
matchOKImg = "./Img/matchOK.png"
matchOKRegin = (1700,595,120,57)
rematchImg = "./Img/rematch.png"
rematchRegin = (1150, 990, 180, 40)
matchendImg = "./Img/matchend.png"
matchendRegin = (1717, 580, 130, 55)
matchingImg = "./Img/matching.png"
matchingRegin = (1830, 180, 42, 42)

pairingImg = "./Img/pairing.png"
pairingRegin = (285, 975, 100, 45)
quitImg = "./Img/quit.png"
quitRegin = (1000, 360, 100, 40)
quitConfirmImg = "./Img/quitConfirm.png"
quitConfirmRegin = (1000, 812, 100, 40)

cardImg = "./Img/card.png"
cardRegin = (1190, 1000, 200, 50)

arenaImg = "./Img/arena.png"
arenaRegin = (955, 1000, 200, 50)

wangyiUserImg = "./Img/wangyiUser.png"
wangyiUserRegin = (320, 156, 165, 60)

infoImg = "./Img/info.png"
infoRegin = (466, 180, 180, 40)

otherImg = "./Img/other.png"
otherRegin = (1700, 1000, 150, 40)

cardBuildImg = "./Img/cardBuild.png"
cardBuildRegin = (1785, 888, 40, 40)

def getCurrentState():
    state = "loading"
    whileNums = 15
    while state == "loading" and whileNums > 0:
        whileNums -= 1
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
                moveCardPageImg, region=moveCardPageRegin, confidence=0.8)
        if location is not None:
            state = "moveCardPage"
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

            location2profession = pyautogui.locateCenterOnScreen(
                    matchPage2professionImg, region=matchPage2professionRegin, confidence=0.8)
            if location is not None:
                state = "matchPage2to1"
            elif location2profession is not None:
                state = "matchPage2profession"
            else:
                location = pyautogui.locateCenterOnScreen(
                    matchPage2to1PlusImg, region=matchPage2to1PlusRegin, confidence=0.8)
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
            userloginImg, region=userloginRegin, confidence=0.8)
        if location is not None:
            state = "userloginPage"
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
            quitImg, region=quitRegin, confidence=0.8)
        if location is not None:
            state = "quitPage"
            break
        location = pyautogui.locateCenterOnScreen(
            quitConfirmImg, region=quitConfirmRegin, confidence=0.8)
        if location is not None:
            state = "quitConfirmPage"
            break
        location = pyautogui.locateCenterOnScreen(
            pairingImg, region=pairingRegin, confidence=0.8)
        if location is not None:
            state = "pairing"
            break

        location = pyautogui.locateCenterOnScreen(
            cardImg, region=cardRegin, confidence=0.8)
        if location is not None:
            state = "card"
            break

        location = pyautogui.locateCenterOnScreen(
            arenaImg, region=arenaRegin, confidence=0.8)
        if location is not None:
            state = "arena"
            break
        location = pyautogui.locateCenterOnScreen(
            wangyiUserImg, region=wangyiUserRegin, confidence=0.8)
        if location is not None:
            state = "wangyiUser"
            break
        location = pyautogui.locateCenterOnScreen(
            infoImg, region=infoRegin, confidence=0.8)
        if location is not None:
            state = "info"
            break
        location = pyautogui.locateCenterOnScreen(
            otherImg, region=otherRegin, confidence=0.8)
        if location is not None:
            state = "other"
            break
        location = pyautogui.locateCenterOnScreen(
            cardBuildImg, region=cardBuildRegin, confidence=0.8)
        if location is not None:
            state = "cardBuild"
            break
        location = pyautogui.locateCenterOnScreen(
            matchingImg, region=matchingRegin, confidence=0.8)
        if location is not None:
            state = "matching"
            break
        
    if whileNums == 0:
        state = "flush"
    colorPrint("current state: {}".format(state), "cyan")
    glv._set("currentState",state)
    return state
