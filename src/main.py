
from turtle import goto
import config
from process import find_mumu_process
import global_variable as glv
from input_process import inputParameters, isIceEnable
from atomAction import getCurrentState
from click import quickClickAbsolute
from basicClass import position
from tsjPython.tsjCommonFunc import *

matchPagePostion = position(826,1033)
pageCenterPostion = position(962,600)
matchSpecifiedPagePosiotions = position(1323,541)
matchUnlimitedPagePosiotions = position(1257,761)
reloginPostion = position(1065,993)
confirmPosition = position(1260,842)
matchOKPostion = position(1760,600)
rematchPostion = position(1235,1013)

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
        elif state == 'matchOKPage':
            quickClickAbsolute(matchOKPostion)
            break
        elif state == 'matching':
            break
    passPrint("Game Already Started!!")

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