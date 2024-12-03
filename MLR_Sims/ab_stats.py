stats_dict = {
    "PA": 0,
    "AB": 0,
    "H": 0,
    "BB": 0,
    "1B": 0,
    "2B": 0,
    "3B": 0,
    "HR": 0,
    "R": 0,
    "K": 0,
    "SF": 0,
    "DP": 0,
    "Adv 2nd": 0, #times runner advanced from 2nd to 3rd on an out
    "SA": 0,
    "SB": 0,
}

# "ON BASE CODE"
# 0-Bases Empty
# 1-Runner 1st
# 2-Runner 2nd
# 3-Runner 3rd
# 4-1st and 2nd
# 5-1st and 3rd
# 6-2nd and 3rd
# 7-Bases Loaded

def reset_stats(the_dict):
    the_dict = {key: 0 for key in the_dict}
    return the_dict


def add_ab():
    stats_dict["PA"] += 1
    stats_dict["AB"] += 1
    
def add_hit():
    stats_dict["PA"] += 1
    stats_dict["AB"] += 1
    stats_dict['H'] += 1   

def check_if_DP_chance(obc,outs,ifin=False):
    if outs == 2:
        return
    if obc in {1,4,7} and not(ifin):
        stats_dict["DP Chance"] += 1