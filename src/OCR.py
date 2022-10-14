from basicClass import position
import easyocr
import pyautogui
from tsjPython.tsjCommonFunc import *

rankScorePosition = position(1124, 712)
rankScoreRegion = position(160, 55)

energyPosition = position(1736, 867)
energyRegion = position(56,50)

def rank_score_ocr():
    im = pyautogui.screenshot(region=(rankScorePosition.x, rankScorePosition.y, rankScoreRegion.x, rankScoreRegion.y))
    im.save('./tmp/rank_score.png')
    reader = easyocr.Reader(['ch_sim', 'en'])
    text = reader.readtext('./tmp/rank_score.png')
    ic(text)
    if not text:
        return 0
    ic(text[0][1])
    if re.search(r"\d+", text[0][1]) is not None:
        score = int(re.search(r"\d+", text[0][1]).group())
        ic(score)
        return score
    else:
        errorPrint("rank score OCR wrong!!!")
        return 0
    
def energy_ocr():
    im = pyautogui.screenshot(region=(energyPosition.x, energyPosition.y, energyRegion.x, energyRegion.y))
    im.save('./tmp/energy.png')
    reader = easyocr.Reader(['ch_sim', 'en'])
    text = reader.readtext('./tmp/energy.png')
    ic(text)
    if not text:
        return 0
    ic(text[0][1])
    if re.search(r"\d+", text[0][1]) is not None:
        energy = int(re.search(r"\d+", text[0][1]).group())
        ic(energy)
        return energy
    else:
        errorPrint("energy OCR wrong!!!")
        return 10