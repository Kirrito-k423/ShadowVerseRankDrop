from basicClass import position
import easyocr
import pyautogui

rankScorePosition = position(,)
rankScoreRegion = position(,)

energyPosition = position(,)
energyRegion = position(,)

def rank_score_ocr():
    im = pyautogui.screenshot(region=(rankScorePosition.x, rankScorePosition.y, rankScoreRegion.x, rankScoreRegion.y))
    im.save('./tmp/rank_score.png')
    reader = easyocr.Reader(['ch_sim', 'en'])
    text = reader.readtext('./tmp/rank_score.png')
    ic(text)
    if re.search(r"\d+", text) is not None:
        score = int(re.search(r"\d+", text).group())
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
    if re.search(r"\d+", text) is not None:
        energy = int(re.search(r"\d+", text).group())
        ic(energy)
        return energy
    else:
        errorPrint("energy OCR wrong!!!")
        return 10