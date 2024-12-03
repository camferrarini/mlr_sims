import pandas as pd
import numpy as np
import random


def getStealResult(batterType,diff):
    t1 = ["S"]
    t2 = ["XB","SM"]
    t3 = ["BC","EN","BN","BP","SF","WC"]
    t4 = ["1B","TT","HK"]
    t5 = ["MH","P"]
    if batterType in t1:
        success = diff <= 335
    elif batterType in t2: 
        success = diff <= 320
    elif batterType in t3: 
        success = diff <= 300
    elif batterType in t4: 
        success = diff <= 280
    elif batterType in t5: 
        success = diff <= 265
    if success:
        return "SB"
    else: return "CS"


num_to_old_result = {
    0: 'HR',
    1: 'B3',
    2: 'B2',
    3: 'B1',
    4: 'BB',
    5: 'FO',
    6: 'K',
    7: 'PO',
    8: 'RGO',
    9: 'LGO',
}

def getBatterOldRanges(batterType):
    match batterType:
        case 'BN': return np.array([11,3,20,37,20,51,49,10,24,25])
        case 'BP': return np.array([21,1,14,20,20,60,60,6,24,24])
        case 'BC': return np.array([8,3,16,52,20,45,31,10,32,33])
        case 'MH': return np.array([34,1,10,8,12,15,5,5,80,80])
        case 'S': return np.array([6,16,21,20,14,62,34,58,10,9])
        case 'XB': return np.array([15,8,27,10,14,16,55,55,25,25])
        case '1B': return np.array([8,2,14,41,40,35,20,11,35,44])
        case 'EN': return np.array([15,15,15,15,15,35,35,35,35,35])
        case 'WC': return np.array([12,4,14,16,56,45,40,23,20,20])
        case 'HK': return np.array([27,1,12,21,10,20,90,10,30,29])
        case 'TT': return np.array([25,1,7,7,45,20,120,5,10,10])
        case 'SM': return np.array([10,2,15,34,30,99,10,10,30,10])
        case 'SF': return np.array([7,1,10,70,10,20,10,75,24,23])
        case 'P': return np.array([8,2,8,16,21,20,85,20,35,35])

def getPitcherOldRanges(pitcherType):
    match pitcherType:
        case 'BB': return np.array([13,1,14,35,19,57,45,13,28,26])
        case 'BS': return np.array([11,2,16,34,19,57,62,8,20,22])
        case 'BF': return np.array([13,1,14,38,18,46,34,16,34,37])
        case 'NH': return np.array([1,9,24,33,21,53,41,26,21,22])
        case 'FP': return np.array([20,4,18,13,13,89,21,21,26,26])
        case 'TT': return np.array([23,1,9,13,30,23,121,8,11,12])
        case 'TD': return np.array([5,11,23,27,15,59,19,15,39,38])
        case 'EG': return np.array([8,4,29,32,16,25,11,8,59,59])
        case '1B': return np.array([7,1,12,40,38,50,28,22,25,28])
        case 'EN': return np.array([14,14,14,14,14,36,36,36,36,37])
        case 'WC': return np.array([9,2,25,29,13,26,11,111,13,12])
        case 'NT': return np.array([11,2,13,24,42,45,31,9,37,37])
        case 'SF': return np.array([6,1,8,69,10,25,11,69,25,27])
        case 'POS': return np.array([18,1,22,47,31,55,11,27,20,19])

num_to_new_result = {
    0: 'HR',
    1: 'B3',
    2: 'B2',
    3: 'B1',
    4: 'BB',
    5: 'RFO',
    6: 'LFO',
    7: 'K',
    8: 'PO',
    9: 'GO',
}
####### ORIGINAL RANGES #########################################################
# def getBatterNewRanges(batterType):
#     match batterType:
#         case 'BN': return np.array([11,3,20,37,20,26,25,49,10,49]) 
#         case 'BP': return np.array([21,1,14,20,20,30,30,60,6,48])
#         case 'BC': return np.array([8,3,16,52,20,23,22,31,10,65])
#         case 'MH': return np.array([34,1,10,8,12,8,7,5,5,160])
#         case 'S': return np.array([6,16,21,20,14,31,31,34,58,19])
#         case 'XB': return np.array([15,8,27,10,14,8,8,55,55,50])
#         case '1B': return np.array([8,2,14,41,40,18,17,20,11,79])
#         case 'EN': return np.array([15,15,15,15,15,18,17,35,35,70])
#         case 'WC': return np.array([12,4,14,16,56,23,22,40,23,40])
#         case 'HK': return np.array([27,1,12,21,10,10,10,90,10,59])
#         case 'TT': return np.array([25,1,7,7,45,10,10,120,5,20])
#         case 'SM': return np.array([10,2,15,34,30,50,49,10,10,40])
#         case 'SF': return np.array([7,1,10,70,10,10,10,10,75,47])
#         case 'P': return np.array([8,2,8,16,21,10,10,85,20,70])


# def getPitcherNewRanges(pitcherType):
#     match pitcherType:
#         case 'BB': return np.array([13,1,14,35,19,29,28,45,13,54])
#         case 'BS': return np.array([11,2,16,34,19,29,28,62,8,42])
#         case 'BF': return np.array([13,1,14,38,18,23,23,34,16,71])
#         case 'NH': return np.array([1,9,24,33,21,27,26,41,26,43])
#         case 'FP': return np.array([20,4,18,13,13,45,44,21,21,52])
#         case 'TT': return np.array([23,1,9,13,30,12,11,121,8,23])
#         case 'TD': return np.array([5,11,23,27,15,30,29,19,15,77])
#         case 'EG': return np.array([8,4,29,32,16,13,12,11,8,118])
#         case '1B': return np.array([7,1,12,40,38,25,25,28,22,53])
#         case 'EN': return np.array([14,14,14,14,14,18,18,36,36,73])
#         case 'WC': return np.array([9,2,25,29,13,13,13,11,111,25])
#         case 'NT': return np.array([11,2,13,24,42,23,22,31,9,74])
#         case 'SF': return np.array([6,1,8,69,10,13,12,11,69,52])
#         case 'POS': return np.array([18,1,22,47,31,28,27,11,27,39])
#################################################################################
        
def getBatterNewRanges(batterType):
    match batterType:
        case 'BN': return np.array([11,3,20,37,20,23,22,49,10,55])
        case 'BP': return np.array([21,1,14,20,20,30,30,60,6,48])
        case 'BC': return np.array([8,3,16,52,20,23,22,31,10,65])
        case 'MH': return np.array([34,1,10,8,12,11,10,5,5,154])
        case 'S': return np.array([6,16,21,20,14,28,28,37,58,22])
        case 'XB': return np.array([15,8,27,10,14,11,10,55,55,45])
        case '1B': return np.array([8,2,14,41,40,15,16,20,13,81])
        case 'EN': return np.array([15,15,15,15,15,15,15,35,35,75])
        case 'WC': return np.array([12,4,14,16,56,25,20,40,23,40])
        case 'HK': return np.array([27,1,12,21,10,10,10,90,10,59])
        case 'TT': return np.array([25,1,7,7,45,7,13,120,5,20])
        case 'SM': return np.array([10,2,15,34,30,45,54,10,10,40])
        case 'SF': return np.array([7,1,10,70,10,10,10,10,75,47])
        case 'P': return np.array([8,2,8,16,21,10,10,85,20,70])



def getPitcherNewRanges(pitcherType):
    match pitcherType:
        case 'BB': return np.array([13,1,14,35,19,27,30,45,13,54])
        case 'BS': return np.array([11,2,16,34,19,25,30,62,10,42])
        case 'BF': return np.array([13,1,14,38,18,25,25,32,14,71])
        case 'NH': return np.array([1,9,24,33,21,27,26,41,26,43])
        case 'FP': return np.array([20,4,18,13,13,45,44,21,21,52])
        case 'TT': return np.array([23,1,9,13,30,11,11,121,8,24])
        case 'TD': return np.array([5,11,23,27,15,30,29,19,15,77])
        case 'EG': return np.array([8,4,29,32,16,17,16,11,8,110])
        case '1B': return np.array([7,1,12,40,38,22,28,28,22,53])
        case 'EN': return np.array([14,14,14,14,14,22,22,34,34,69])
        case 'WC': return np.array([9,2,25,29,13,13,13,11,111,25])
        case 'NT': return np.array([11,2,13,24,42,23,22,31,9,74])
        case 'SF': return np.array([6,1,8,69,10,13,12,11,69,52])
        case 'PO': return np.array([18,1,22,47,31,28,27,11,27,39])


        
def getOldRanges(batterType,pitcherType,infin=False):
    bRanges = getBatterOldRanges(batterType)
    pRanges = getPitcherOldRanges(pitcherType)
    if random.choice([True,False]): #50/50 chance at hand bonus
        bonus = random.choice(['H','S','B']) #this isn't perfect, I'm sure certain types pick specific hand bonuses significantly more than others... but it'll work.
        match bonus:
            case 'H':
                handRanges = np.array([-4,-1,-3,-2,-1,1,6,0,2,2]) 
            case 'S':
                handRanges = np.array([-2,-1,-3,-7,-1,2,8,2,1,1]) 
            case 'B':
                handRanges = np.array([-3,-1,-3,-4,-1,2,5,1,2,2]) 
    else:
        handRanges = [0] * 10
    if infin:
        infinRanges = np.array([0,0,0,18,0,0,0,0,-9,-9]) 
    else:
        infinRanges = [0] * 10

    ranges = bRanges + pRanges + handRanges + infinRanges
    # print(ranges)
    if (sum(ranges)) != 501:
        raise ValueError('Ranges do not sum to 501.')
    return ranges

def getOldResult(ranges,diff):
    total_range = 0
    for i in range(10):
        total_range = total_range + ranges[i]
        if diff < total_range:
            # print(num_to_old_result[i])
            return num_to_old_result[i]


def getNewRanges(batterType,pitcherType,infin=False):
    bRanges = getBatterNewRanges(batterType)
    pRanges = getPitcherNewRanges(pitcherType)
    if random.choice([True,False]): #50/50 chance at hand bonus
        bonus = random.choice(['H','S','B']) #this isn't perfect, I'm sure certain types pick specific hand bonuses significantly more than others... but it'll work.
        match bonus:
            case 'H':
                handRanges = np.array([-4,-1,-3,-2,-1,1,0,6,0,4]) 
            case 'S':
                handRanges = np.array([-2,-1,-3,-7,-1,1,1,8,2,2]) 
            case 'B':
                handRanges = np.array([-3,-1,-3,-4,-1,1,1,5,1,4]) 
    else:
        handRanges = [0] * 10
    if infin:
        infinRanges = np.array([0,0,0,18,0,0,0,0,0,-18]) 
    else:
        infinRanges = [0] * 10

    ranges = bRanges + pRanges + handRanges + infinRanges
    # print(ranges)
    if (sum(ranges)) != 501:
        raise ValueError('Ranges do not sum to 501.')
    return ranges

def getNewResult(ranges,diff):
    total_range = 0
    for i in range(10):
        total_range = total_range + ranges[i]
        if diff < total_range:
            # print(num_to_old_result[i])
            return num_to_new_result[i]

# test_range = getOldRanges('S','BS')
# test_result = getOldResult(test_range,475)