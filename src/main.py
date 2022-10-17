
from turtle import goto
import config
from process import find_mumu_process
import global_variable as glv
from input_process import inputParameters, isIceEnable
from atomAction import getCurrentState
from click import quickClickAbsolute
from basicClass import position
from tsjPython.tsjCommonFunc import *
from OCR import energy_ocr, rank_score_ocr
import time

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
cardBuildCancelPosition = position(1819,216)


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
            quickClickAbsolute(matchPagePostion)
        elif state == 'matchPage3to1':
            quickClickAbsolute(pageCenterPostion)
        elif state == 'matchPage2to1':
            if glv._get("matchMode")=="1": #指定
                quickClickAbsolute(matchSpecifiedPagePosiotions)
            else:
                quickClickAbsolute(matchUnlimitedPagePosiotions)
        elif state == 'reloginPage' or state=='loginPage':
            quickClickAbsolute(reloginPosition)
        elif state == 'chooseCardPage':
            quickClickAbsolute(pageCenterPostion) #默认选中间的卡组
        elif state == 'OKPage':
            quickClickAbsolute(confirmPosition)
        elif state == 'rematchPage':
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
                glv._set("lastRankScore", currentRankScore)
            if drop2end():
                break
        elif state == 'matching':
            currentEnergyNum = energy_ocr()
            matchingCount += 1
            if currentEnergyNum > 2 or matchingCount > 15:
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

def surrender():
    return

def start_rank_dropping():
    while not drop2end():#分数降低到多少退出
        start_matching()
        surrender()

if __name__ == '__main__':
    args = inputParameters()
    isIceEnable(args.debug)
    find_mumu_process()
    start_rank_dropping()