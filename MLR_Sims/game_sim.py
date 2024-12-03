import random
import ranges
import results
import ab_stats
import sys

def getRandomPitcher():
    return random.choice(['BB','BS','BF','NH','FP','TT','TD','EG','1B','EN','WC','NT','SF'])

def getRandomBatter():
    return random.choice(['BN','BP','BC','MH','S','XB','1B','EN','WC','HK','TT','SM','SF'])

def checkStealAttempt(obc,batterType):
    t1_and_t2 = ["S","XB","SM"]
    t3 = ["BC","EN","BN","BP","SF","WC"]
    if obc == 1 or obc == 5:
        if batterType in t1_and_t2:
            return True
        elif batterType in t3 and random.choice([True,False]):
            return True
        else:
            return False
    else:
        return False

def checkifin(outs,obc):
    if outs == 0 and obc in [3,5,6,7]:
        return True
    elif outs == 1 and obc in [3,6]:
        return True
    else:
        return False

def testBatterType(batterType,old=True,numInnings=100): #have one batter type bat against randomly selected pitcher types each inning
    inning = 0
    outs = 0
    obc = 0
    pitcherType = getRandomPitcher()
    while inning < numInnings:
        percent_done = (inning/numInnings) * 100
        sys.stdout.write(f"\rLoop {percent_done:.2f}% complete")
        sys.stdout.flush()
        ifin = checkifin(outs,obc)
        stealing = checkStealAttempt(obc,batterType)
        diff = random.randint(0, 500)
        if stealing:
            ab_result = ranges.getStealResult(batterType,diff)
        elif old:
            ab_ranges = ranges.getOldRanges(batterType,pitcherType,ifin)
            ab_result = ranges.getOldResult(ab_ranges,diff)
        else:
            ab_ranges = ranges.getNewRanges(batterType,pitcherType,ifin)
            ab_result = ranges.getNewResult(ab_ranges,diff)
        # print(outs,"Outs, OBC:", obc,"->", ab_result)
        obc,outs = getattr(results, ab_result)(obc, outs, ifin)
        if outs >= 3:
            inning = inning + 1
            obc = 0
            outs = 0
            pitcherType = getRandomPitcher()
            # print("New Inning, batting against", pitcherType)
    print('\n')
    # print(batterType, "Results:")
    # print(ab_stats.stats_dict)

def testPitcherType(pitcherType,old=True,numInnings=100): #have one pitcher type pitch to randomly selected batter types each AB
    inning = 0
    outs = 0
    obc = 0
    lastBatter = ''
    while inning < numInnings:
        percent_done = (inning/numInnings) * 100
        sys.stdout.write(f"\rLoop {percent_done:.2f}% complete")
        batterType = getRandomBatter()
        ifin = checkifin(outs,obc)
        stealing = checkStealAttempt(obc,lastBatter)
        diff = random.randint(0, 500)
        if stealing:
            ab_result = ranges.getStealResult(lastBatter,diff)
        elif old:
            ab_ranges = ranges.getOldRanges(batterType,pitcherType,ifin)
            ab_result = ranges.getOldResult(ab_ranges,diff)
        else:
            ab_ranges = ranges.getNewRanges(batterType,pitcherType,ifin)
            ab_result = ranges.getNewResult(ab_ranges,diff)
        # print(outs,"Outs, OBC:", obc,"->", ab_result)
        obc,outs = getattr(results, ab_result)(obc, outs, ifin)
        lastBatter = batterType
        if outs >= 3:
            inning = inning + 1
            obc = 0
            outs = 0
            # print("New Inning")
    print('\n')
    # print(pitcherType, "Results:")
    # print(ab_stats.stats_dict)

def testLeague(old=True,numInnings=100): #randomly select a batter per AB and a pitcher per inning to get a sense of overall league offense
    inning = 0
    outs = 0
    obc = 0
    pitcherType = getRandomPitcher()
    lastBatter = ''
    while inning < numInnings:
        percent_done = (inning/numInnings) * 100
        sys.stdout.write(f"\rLoop {percent_done:.2f}% complete")
        batterType = getRandomBatter()
        ifin = checkifin(outs,obc)
        stealing = checkStealAttempt(obc,lastBatter)
        diff = random.randint(0, 500)
        if stealing:
            ab_result = ranges.getStealResult(lastBatter,diff)
        elif old:
            ab_ranges = ranges.getOldRanges(batterType,pitcherType,ifin)
            ab_result = ranges.getOldResult(ab_ranges,diff)
        else:
            ab_ranges = ranges.getNewRanges(batterType,pitcherType,ifin)
            ab_result = ranges.getNewResult(ab_ranges,diff)
        # print(outs,"Outs, OBC:", obc,"->", ab_result)
        obc,outs = getattr(results, ab_result)(obc, outs, ifin)
        lastBatter = batterType
        if outs >= 3:
            inning = inning + 1
            obc = 0
            outs = 0
            pitcherType = getRandomPitcher()
            # print("New Inning, batting against", pitcherType)
    print('\n')
    # print(batterType, "Results:")
    # print(ab_stats.stats_dict)


# testBatterType("SM",True,1000)