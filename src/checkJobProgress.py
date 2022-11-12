
import global_variable as glv
from tsjPython.tsjCommonFunc import *
from OCR import loginUser_ocr
import sys
def checkChangeUserLogin():
    currentUserName = getCurrentUserName()
    if currentUserName in glv._get("finishedUserList"):
        passPrint("{}'s job is finished".format(currentUserName))

def getCurrentUserName():
    if glv._get("currentUser") != "?":
        return glv._get("currentUser")
    elif glv._get("currentState") == "userloginPage":
        currentUserName = loginUser_ocr()
        glv._set("currentUser",currentUserName)
        return currentUserName
    else:
        return "unknownUser"

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
    elif currentUserScoreList[1] != 1200 or  currentUserScoreList[1] != 4500:
        return 2  # 无限
    elif currentUserScoreList[0] != 1200 or  currentUserScoreList[0] != 4500:
        return 1 # 指定
    else:
        glv._set("finishedUserList",glv._get("finishedUserList").append(glv._get("currentUser")))
        ic(glv._get("finishedUserList"))
        return 0

def ifNeedSwitchUser():
    if glv._get("currentUser") in glv._get("finishedUserList"):
        return 1
    else:
        return 0