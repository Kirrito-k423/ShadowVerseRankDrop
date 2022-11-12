from basicClass import position
import easyocr
import pyautogui
from tsjPython.tsjCommonFunc import *
import global_variable as glv

rankScorePosition = position(1124, 712)
rankScoreRegion = position(160, 55)

SpecifiedScorePosition = position(800, 647)
SpecifiedScoreRegion = position(160,45)

UnlimitedScorePosition = position(800, 766)
UnlimitedScoreRegion = position(155,45)

energyPosition = position(1736, 867)
energyRegion = position(56,50)

loginUserPosition = position(856, 536)
loginUserRegion = position(400,48)

wangyiUserPosition = position(390, 309)
wangyiUserRegion = position(333,47)

matchTypePosition = position(443, 815)
matchTypeRegion = position(160,45)

def rank_score_ocr():
    im = pyautogui.screenshot(region=(rankScorePosition.x, rankScorePosition.y, rankScoreRegion.x, rankScoreRegion.y))
    im.save('./tmp/rank_score.png')
    reader = easyocr.Reader(['ch_sim', 'en'])
    text = reader.readtext('./tmp/rank_score.png')
    ic(text)
    if not text:
        errorPrint("rank score OCR wrong!!!")
        return -1
    ic(text[0][1])
    if re.search(r"\d+", text[0][1]) is not None:
        score = int(re.search(r"\d+", text[0][1]).group())
        ic(score)
        return score
    else:
        errorPrint("rank score OCR wrong!!!")
        return -1
    
def info_score_ocr():
    im = pyautogui.screenshot(region=(SpecifiedScorePosition.x, SpecifiedScorePosition.y, SpecifiedScoreRegion.x, SpecifiedScoreRegion.y))
    im.save('./tmp/Specified_score.png')
    im2 = pyautogui.screenshot(region=(UnlimitedScorePosition.x, UnlimitedScorePosition.y, UnlimitedScoreRegion.x, UnlimitedScoreRegion.y))
    im2.save('./tmp/Unlimited_score.png')
    reader = easyocr.Reader(['ch_sim', 'en'])
    text = reader.readtext('./tmp/Specified_score.png')
    text2 = reader.readtext('./tmp/Unlimited_score.png')
    ic(text,text2)
    if not text or not text2:
        errorPrint("rank score OCR wrong!!!")
        info_score_ocr()
    ic(text[0][1],text2[0][1])
    if re.search(r"\d+", text[0][1]) is not None and re.search(r"\d+", text2[0][1]) is not None:
        score = int(re.search(r"\d+", text[0][1]).group())
        score2 = int(re.search(r"\d+", text2[0][1]).group())
        passPrint("{} {}".format(score,score2))
        glv._set("currentUserScore",[score,score2])
    else:
        errorPrint("rank score OCR wrong!!!")
        info_score_ocr()

def energy_ocr():
    im = pyautogui.screenshot(region=(energyPosition.x, energyPosition.y, energyRegion.x, energyRegion.y))
    im.save('./tmp/energy.png')
    reader = easyocr.Reader(['ch_sim', 'en'])
    text = reader.readtext('./tmp/energy.png')
    ic(text)
    if not text:
        errorPrint("energy OCR wrong!!!")
        return -1
    ic(text[0][1])
    if re.search(r"\d+", text[0][1]) is not None:
        energy = int(re.search(r"\d+", text[0][1]).group())
        ic(energy)
        return energy
    else:
        errorPrint("energy OCR wrong!!!")
        return -1
    
def loginUser_ocr():
    im = pyautogui.screenshot(region=(loginUserPosition.x, loginUserPosition.y, loginUserRegion.x, loginUserRegion.y))
    im.save('./tmp/loginUser.png')
    reader = easyocr.Reader(['ch_sim', 'en'])
    text = reader.readtext('./tmp/loginUser.png')
    ic(text)
    if not text:
        errorPrint("loginUser OCR wrong!!!")
        return -1
    ic(text[0][1])
    if text[0][1] is not None:
        loginUser = text[0][1]
        passPrint(loginUser)
        return loginUser
    else:
        errorPrint("loginUser OCR wrong!!!")
        return -1

def wangyiUser_ocr():
    im = pyautogui.screenshot(region=(wangyiUserPosition.x, wangyiUserPosition.y, wangyiUserRegion.x, wangyiUserRegion.y))
    im.save('./tmp/wangyiUser.png')
    reader = easyocr.Reader(['ch_sim', 'en'])
    text = reader.readtext('./tmp/wangyiUser.png')
    ic(text)
    if not text:
        errorPrint("wangyiUser OCR wrong!!!")
        return -1
    ic(text[0][1])
    if text[0][1] is not None:
        wangyiUser = text[0][1]
        passPrint(wangyiUser)
        return wangyiUser
    else:
        errorPrint("wangyiUser OCR wrong!!!")
        return -1

def matchType_ocr():
    im = pyautogui.screenshot(region=(matchTypePosition.x, matchTypePosition.y, matchTypeRegion.x, matchTypeRegion.y))
    im.save('./tmp/matchType.png')
    reader = easyocr.Reader(['ch_sim', 'en'])
    text = reader.readtext('./tmp/matchType.png')
    ic(text)
    if not text:
        errorPrint("matchType OCR wrong!!!")
        return -1
    ic(text[0][1])
    if text[0][1] is not None:
        matchType = text[0][1]
        passPrint(matchType)
        return matchType
    else:
        errorPrint("matchType OCR wrong!!!")
        return -1