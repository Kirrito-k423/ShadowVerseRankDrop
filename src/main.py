
from turtle import goto
import config
from process import find_mumu_process
import global_variable as glv
from input_process import inputParameters, isIceEnable
from atomAction import getCurrentState

def start_matching():
    state = getCurrentState()
    
def start_rank_dropping():
    start_matching()
if __name__ == '__main__':
    args = inputParameters()
    isIceEnable(args.debug)
    find_mumu_process()
    start_rank_dropping()