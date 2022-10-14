import global_variable as glv
from collections import defaultdict
import time
from basicClass import position
#, const, job, team, COMBO

glv._init()

glv._set("HistoryDataFile", "/home/shaojiemike/blockFrequency/Summary_BHiveCount5002022-08-03-10-47-17_tsj.xlsx") # for test
glv._set("mumu_start_coordinate",position(100,100))
glv._set("mumu_regex_name","影之诗 - MuMu模拟器")
glv._set("mumu_hight_width",position(int(1.5*700),int(1.5*1280)))
glv._set("lastRankScore", 6000)

def pasteFullFileName(taskfilenameWithoutPath):
    taskfilePath=glv._get("taskfilePath")
    taskfilename="{}/{}".format(taskfilePath,taskfilenameWithoutPath)
    return taskfilename


