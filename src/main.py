
from turtle import goto
import config
from process import find_mumu_process, windows_turn_on_mumu
import global_variable as glv
from input_process import inputParameters, isIceEnable
from atomAction import getCurrentState
from click import quickClickAbsolute
from basicClass import position
from tsjPython.tsjCommonFunc import *
from OCR import energy_ocr, rank_score_ocr, info_score_ocr, wangyiUser_ocr
import time
import sys
from checkJobProgress import getMatchType,checkChangeUserLogin,ifNeedCollectInfo,ifNeedDropScore,ifNeedSwitchUser,matchfinishCheck
from OCR import loginUser_ocr

matchPagePostion = position(826,1033)
pageCenterPostion = position(962,600)
matchSpecifiedPagePosiotions = position(1323,541)
matchUnlimitedPagePosiotions = position(1257,761)
reloginPosition = position(1065,993)
centerConfirmPosition = position(1065,830)
confirmPosition = position(1260,842)
matchOKPostion = position(1760,600)
rematchPostion = position(1235,1013)
escPosition = position(1850, 204)
quitButtonPosition = position(1060, 383)
quitConfirmPosition = position(1060, 830)
characterPosition = position(1061,970)
duosiyouPosition = position(1386, 1024)
sorryPosision = position(713, 1016)
rightOKPosition = position(1264, 968)
leftOKPosition = position(857, 962)
returnPosition = position(353,207)
wangyiReturnPosition = position(255,181)
cardBuildCancelPosition = position(1819,216)
userloginPosition = position(1049,708)
otherPagePosition = position(1765,1024)
scoreInfoPosition = position(516,410)
userCenterPosition = position(1246,786)
returnMainPosition = position(1658,1005)
switchAccountPosition = position(1771,328)
switch1Position = position(1065,593)
switch2Position = position(1065,714)


def drop2end():
    if glv._get("lastRankScore") == 4500 or glv._get("lastRankScore") == 1200:
        return 1
    else:
        return 0

def saySorry():
    quickClickAbsolute(characterPosition)
    quickClickAbsolute(duosiyouPosition)
    quickClickAbsolute(characterPosition)
    quickClickAbsolute(sorryPosision)

def flushOKClick():
    quickClickAbsolute(rightOKPosition)
    quickClickAbsolute(leftOKPosition)
    quickClickAbsolute(reloginPosition)
    quickClickAbsolute(centerConfirmPosition)
    quickClickAbsolute(returnPosition)
    quickClickAbsolute(pageCenterPostion)
    quickClickAbsolute(pageCenterPostion)

def start_matching():
    state = getCurrentState()
    beforeState = state
    stateUnchangedCount=0
    matchingCount = 0
    while state != "match_start":
        state = getCurrentState()
        if state==beforeState:
            stateUnchangedCount += 1
        else:
            stateUnchangedCount = 0
        beforeState = state
        if stateUnchangedCount > 8:
            flushOKClick()
            stateUnchangedCount = 0
        if state == 'mainPage' or state == 'card' or state == 'arena':
            if ifNeedCollectInfo():
                quickClickAbsolute(otherPagePosition)
            else:
                quickClickAbsolute(matchPagePostion)
        if state == 'other':
            flag = ifNeedCollectInfo()
            if flag==1 or ifNeedSwitchUser():
                quickClickAbsolute(userCenterPosition)
            elif flag==2:
                quickClickAbsolute(scoreInfoPosition)
                time.sleep(1)
            elif ifNeedDropScore():
                quickClickAbsolute(matchPagePostion)
            else:
                quickClickAbsolute(userCenterPosition)

        if state == 'info':
            info_score_ocr()
            flag = ifNeedCollectInfo()
            if flag==1:
                quickClickAbsolute(returnPosition)
            elif flag==2:
                info_score_ocr()
            elif ifNeedDropScore():
                quickClickAbsolute(matchPagePostion)
            else:
                quickClickAbsolute(otherPagePosition)
        if state == 'wangyiUser':
            flag = ifNeedCollectInfo()
            if flag==1:
                currentUserName = wangyiUser_ocr()
                glv._set("currentUser",currentUserName)
                quickClickAbsolute(wangyiReturnPosition)
            elif flag==2:
                quickClickAbsolute(wangyiReturnPosition)
            elif ifNeedSwitchUser():
                quickClickAbsolute(switchAccountPosition)
            else:
                quickClickAbsolute(matchPagePostion)
        elif state == 'matchPage3to1':
            quickClickAbsolute(pageCenterPostion)
        elif state == 'matchPage2to1':
            flag = ifNeedDropScore()
            if flag == 1:
                quickClickAbsolute(matchSpecifiedPagePosiotions)
            elif  flag == 2:
                quickClickAbsolute(matchUnlimitedPagePosiotions)
            else:
                quickClickAbsolute(otherPagePosition)
        elif state == 'userloginPage':
            if checkChangeUserLogin():
                # clean & switch switchAccount
                glv._set("currentUserScore",[sys.maxsize,sys.maxsize])
                quickClickAbsolute(switch1Position)
                quickClickAbsolute(switch2Position)
                currentUserName = loginUser_ocr()
                glv._set("currentUser",currentUserName)
            else:
                quickClickAbsolute(userloginPosition)
        elif state == 'reloginPage' or state=='loginPage':
            quickClickAbsolute(reloginPosition)
        elif state == 'chooseCardPage':
            quickClickAbsolute(pageCenterPostion) #默认选中间的卡组
        elif state == 'OKPage':
            quickClickAbsolute(confirmPosition)
        elif state == 'rematchPage':
            flag = matchfinishCheck()
            if flag:
                quickClickAbsolute(returnMainPosition)
            else:
                quickClickAbsolute(rematchPostion)
            time.sleep(0.7)
        elif state == 'matchOKPage' or state=='matchendPage':
            quickClickAbsolute(matchOKPostion)
        elif state == 'cardBuild':
            quickClickAbsolute(cardBuildCancelPosition)
        elif state == 'pairing':
            currentRankScore = int(rank_score_ocr())
            if currentRankScore == -1:
                flushOKClick()
                continue
            lastRankScore = glv._get("lastRankScore")
            if currentRankScore != lastRankScore:
                passPrint("drop rank score from {} to {}. delta={}".format(lastRankScore, currentRankScore,currentRankScore-lastRankScore))
            if drop2end():
                break
        elif state == 'matching':
            currentEnergyNum = energy_ocr()
            matchingCount += 1
            if currentEnergyNum > 0 or matchingCount > 15:
                matchingCount = 0
                saySorry()
                quickClickAbsolute(escPosition)
            elif currentEnergyNum == -1:
                flushOKClick()
                quickClickAbsolute(matchOKPostion)
            else:
                quickClickAbsolute(matchOKPostion)
        elif state == 'quitPage':
            quickClickAbsolute(quitButtonPosition)
        elif state == 'quitConfirmPage':
            quickClickAbsolute(quitConfirmPosition)
        elif state == 'flush':
            flushOKClick()

    # passPrint("Game Already Started!!")

def finishedAccountNum():
    if len(glv._get("finishedUserList"))== 2:
        return 0
    else:
        return 1

def start_rank_dropping():
    # while not drop2end():#分数降低到多少退出
    while finishedAccountNum():
        start_matching()


if __name__ == '__main__':
    args = inputParameters()
    isIceEnable(args.debug)
    windows_turn_on_mumu()
    while not find_mumu_process():
        time.sleep(1)
        find_mumu_process()
    time.sleep(2)
    find_mumu_process()
    time.sleep(2)
    find_mumu_process()
    start_rank_dropping()