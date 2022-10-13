import global_variable as glv
from collections import defaultdict
import time

glv._init()

glv._set("HistoryDataFile", "/home/shaojiemike/blockFrequency/Summary_BHiveCount5002022-08-03-10-47-17_tsj.xlsx") # for test



def pasteFullFileName(taskfilenameWithoutPath):
    taskfilePath=glv._get("taskfilePath")
    taskfilename="{}/{}".format(taskfilePath,taskfilenameWithoutPath)
    return taskfilename


