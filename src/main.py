
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

matchPagePostion = position(826,1033)
pageCenterPostion = position(962,600)
matchSpecifiedPagePosiotions = position(1323,541)
matchUnlimitedPagePosiotions = position(1257,761)
reloginPostion = position(1065,993)
confirmPosition = position(1260,842)
matchOKPostion = position(1760,600)
rematchPostion = position(1235,1013)
escPosition = position(1850, 204)
quitButtonPosition = position(1060, 383)
quitConfirmPosition = position(1060, 830)
characterPosition = position(1061,970)
duosiyouPosition = position(1386, 1024)
sorryPosision = position(713, 1016)

def saySorry():
    quickClickAbsolute(characterPosition)
    quickClickAbsolute(duosiyouPosition)
    quickClickAbsolute(characterPosition)
    quickClickAbsolute(sorryPosision)

def start_matching():
    state = getCurrentState()
    while state != "match_start":
        state = getCurrentState()
        if state == 'mainPage':
            quickClickAbsolute(matchPagePostion)
        elif state == 'matchPage3to1':
            quickClickAbsolute(pageCenterPostion)
        elif state == 'matchPage2to1':
            if glv._get("matchMode")=="指定":
                quickClickAbsolute(matchSpecifiedPagePosiotions)
            else:
                quickClickAbsolute(matchUnlimitedPagePosiotions)
        elif state == 'reloginPage' or state=='loginPage':
            quickClickAbsolute(reloginPostion)
        elif state == 'chooseCardPage':
            quickClickAbsolute(pageCenterPostion) #默认选中间的卡组
        elif state == 'OKPage':
            quickClickAbsolute(confirmPosition)
        elif state == 'rematchPage':
            quickClickAbsolute(rematchPostion)
        elif state == 'matchOKPage' or state=='matchendPage':
            quickClickAbsolute(matchOKPostion)
        elif state == 'pairing':
            currentRankScore = int(rank_score_ocr())
            lastRankScore = glv._get("lastRankScore")
            if currentRankScore != lastRankScore:
                passPrint("drop rank score from {} to {}. delta={}".format(currentRankScore, lastRankScore,currentRankScore-lastRankScore))
                glv._set("lastRankScore", currentRankScore)
        elif state == 'matching':
            currentEnergyNum = energy_ocr()
            if currentEnergyNum > 3:
                saySorry()
                quickClickAbsolute(escPosition)
            else:
                quickClickAbsolute(matchOKPostion)
        elif state == 'quitPage':
            quickClickAbsolute(quitButtonPosition)
        elif state == 'quitConfirmPage':
            quickClickAbsolute(quitConfirmPosition)

    # passPrint("Game Already Started!!")

def surrender():
    return

def start_rank_dropping():
    while 1:#分数降低到多少退出
        start_matching()
        surrender()

if __name__ == '__main__':
    args = inputParameters()
    isIceEnable(args.debug)
    find_mumu_process()
    start_rank_dropping()