
import global_variable as glv
from tsjPython.tsjCommonFunc import *
from OCR import loginUser_ocr,matchType_ocr,rank_score_ocr
import sys
from process import kill_process_by_name

def matchfinishCheck():
    score = rank_score_ocr()
    currentMatchType = getMatchType()
    if currentMatchType == "Unlimited":
        index = 1
    elif currentMatchType == "Specified":
        index = 0
    else:
        index = int(glv._get("matchMode"))-1
    currentUserScore = glv._get("currentUserScore")
    glv._set("lastRankScore",currentUserScore[index])
    currentUserScore[index]=score
    glv._set("currentUserScore",currentUserScore)
    ic(glv._get("currentUserScore"))
    if score == 1200 or score == 4500:
        return 1
    else:
        return 0

def checkChangeUserLogin():
    currentUserName = getCurrentUserName()
    if len(glv._get("finishedUserList"))== 2:
        passPrint("All job is finished".format(currentUserName))
        kill_process_by_name("NemuPlayer.exe")
        sys.exit()
    if currentUserName in glv._get("finishedUserList"):
        passPrint("{}'s job is finished".format(currentUserName))
        return 1
    else:
        return 0

def getCurrentUserName():
    if glv._get("currentUser") != "?":
        return glv._get("currentUser")
    elif glv._get("currentState") == "userloginPage":
        currentUserName = loginUser_ocr()
        glv._set("currentUser",currentUserName)
        return currentUserName
    else:
        return "unknownUser"

def getMatchType():
    savedType = glv._get("currentMatchType")
    if savedType != "None":
        return savedType
    elif glv._get("currentState") == "rematchPage":
        typeName = matchType_ocr()
        if typeName == "无限制":
            glv._set("currentMatchType","Unlimited")
            return "Unlimited"
        elif typeName == "指定系列":
            glv._set("currentMatchType","Specified")
            return "Specified"
        else:
            errorPrint("unknown match type")
    else:
        errorPrint("unknown match type")
        

def ifNeedCollectInfo():
    currentUserScoreList = glv._get("currentUserScore") 
    if getCurrentUserName() == "unknownUser":
        errorPrint("need to collect user info - Name")
        return 1
    elif currentUserScoreList[0] == sys.maxsize or\
        currentUserScoreList[1] == sys.maxsize:
        errorPrint("need to collect user info - Score")
        return 2
    else:
        return 0

def ifNeedDropScore():
    currentUserScoreList = glv._get("currentUserScore")
    passPrint("current score {} {}".format(currentUserScoreList[0],currentUserScoreList[1]))
    if ifNeedCollectInfo():
        return 0
    elif currentUserScoreList[1] != 1200 and  currentUserScoreList[1] != 4500:
        glv._set("currentMatchType","Unlimited")
        return 2  # 无限
    elif currentUserScoreList[0] != 1200 and  currentUserScoreList[0] != 4500:
        glv._set("currentMatchType","Specified")
        return 1 # 指定
    else:
        errorPrint(glv._get("finishedUserList"))
        List = glv._get("finishedUserList")
        List.append(glv._get("currentUser"))
        ic(List)
        glv._set("finishedUserList",List)
        errorPrint(glv._get("finishedUserList"))
        return 0

def ifNeedSwitchUser():
    ic(glv._get("currentUser"))
    ic(glv._get("finishedUserList"))
    if glv._get("currentUser") in glv._get("finishedUserList"):
        return 1
    else:
        return 0