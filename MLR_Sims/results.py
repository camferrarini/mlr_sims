# "ON BASE CODE"
# 0-Bases Empty
# 1-Runner 1st
# 2-Runner 2nd
# 3-Runner 3rd
# 4-1st and 2nd
# 5-1st and 3rd
# 6-2nd and 3rd
# 7-Bases Loaded

import ab_stats

# TODO increment hit and hit type counts

###### RESULTS ########
def HR(obc,outs,ifin=False): #DONE
    ab_stats.add_hit()
    ab_stats.stats_dict["HR"] += 1
    new_outs = outs
    new_obc = 0
    match obc:
        case 0:
            ab_stats.stats_dict["R"] += 1
        case 1:
            ab_stats.stats_dict["R"] += 2
        case 2:
            ab_stats.stats_dict["R"] += 2
        case 3:
            ab_stats.stats_dict["R"] += 2
        case 4:
            ab_stats.stats_dict["R"] += 3
        case 5:
            ab_stats.stats_dict["R"] += 3
        case 6:
            ab_stats.stats_dict["R"] += 3
        case 7:
            ab_stats.stats_dict["R"] += 4
    return new_obc, new_outs

def B3(obc,outs,ifin=False): #DONE #triple because python is stupid and 3b isn't a valid function name
    ab_stats.add_hit()
    ab_stats.stats_dict["3B"] += 1
    new_outs = outs
    new_obc = 3
    match obc:
        case 0:
            ab_stats.stats_dict["R"] += 0
        case 1:
            ab_stats.stats_dict["R"] += 1
        case 2:
            ab_stats.stats_dict["R"] += 1
        case 3:
            ab_stats.stats_dict["R"] += 1
        case 4:
            ab_stats.stats_dict["R"] += 2
        case 5:
            ab_stats.stats_dict["R"] += 2
        case 6:
            ab_stats.stats_dict["R"] += 2
        case 7:
            ab_stats.stats_dict["R"] += 3
    return new_obc, new_outs

def B2(obc,outs,ifin=False): #DONE
    ab_stats.add_hit()
    ab_stats.stats_dict["2B"] += 1
    new_outs = outs
    match outs:
        case 2:
            match obc:
                case 0:
                    new_obc = 2
                case 1:
                    new_obc = 2
                    ab_stats.stats_dict["R"] += 1
                case 2:
                    new_obc = 2
                    ab_stats.stats_dict["R"] += 1
                case 3:
                    new_obc = 2
                    ab_stats.stats_dict["R"] += 1
                case 4:
                    new_obc = 2
                    ab_stats.stats_dict["R"] += 2
                case 5:
                    new_obc = 2
                    ab_stats.stats_dict["R"] += 2
                case 6:
                    new_obc = 2
                    ab_stats.stats_dict["R"] += 2
                case 7:
                    new_obc = 2
                    ab_stats.stats_dict["R"] += 1
        case _:
            match obc:
                case 0:
                    new_obc = 2
                case 1:
                    new_obc = 6
                case 2:
                    new_obc = 2
                    ab_stats.stats_dict["R"] += 1
                case 3:
                    new_obc = 2
                    ab_stats.stats_dict["R"] += 1
                case 4:
                    new_obc = 6
                    ab_stats.stats_dict["R"] += 1
                case 5:
                    new_obc = 6
                    ab_stats.stats_dict["R"] += 1
                case 6:
                    new_obc = 2
                    ab_stats.stats_dict["R"] += 2
                case 7:
                    new_obc = 6
                    ab_stats.stats_dict["R"] += 2
    return new_obc, new_outs
# "ON BASE CODE"
# 0-Bases Empty
# 1-Runner 1st
# 2-Runner 2nd
# 3-Runner 3rd
# 4-1st and 2nd
# 5-1st and 3rd
# 6-2nd and 3rd
# 7-Bases Loaded
def B1(obc,outs,ifin=False): #DONE
    ab_stats.add_hit()
    ab_stats.stats_dict["1B"] += 1
    new_outs = outs
    match outs:
        case 2:
            match obc:
                case 0:
                    new_obc = 1
                case 1:
                    new_obc = 5
                case 2:
                    new_obc = 1
                    ab_stats.stats_dict["R"] += 1
                case 3:
                    new_obc = 1
                    ab_stats.stats_dict["R"] += 1
                case 4:
                    new_obc = 5
                    ab_stats.stats_dict["R"] += 1
                case 5:
                    new_obc = 5
                    ab_stats.stats_dict["R"] += 1
                case 6:
                    new_obc = 1
                    ab_stats.stats_dict["R"] += 2
                case 7:
                    new_obc = 5
                    ab_stats.stats_dict["R"] += 2
        case _:
            match obc:
                case 0:
                    new_obc = 1
                case 1:
                    new_obc = 4
                case 2:
                    new_obc = 5
                case 3:
                    new_obc = 1
                    ab_stats.stats_dict["R"] += 1
                case 4:
                    new_obc = 7
                case 5:
                    new_obc = 4
                    ab_stats.stats_dict["R"] += 1
                case 6:
                    new_obc = 5
                    ab_stats.stats_dict["R"] += 1
                case 7:
                    new_obc = 7
                    ab_stats.stats_dict["R"] += 1
    return new_obc, new_outs

def BB(obc,outs,ifin=False): #DONE
    ab_stats.stats_dict["PA"] += 1
    ab_stats.stats_dict["BB"] += 1
    new_outs = outs
    match obc:
        case 0:
            new_obc = 1
        case 1:
            new_obc = 4
        case 2:
            new_obc = 4
        case 3:
            new_obc = 5
        case 4:
            new_obc = 7
        case 5:
            new_obc = 7
        case 6:
            new_obc = 7
        case 7:
            new_obc = 7
            ab_stats.stats_dict["R"] += 1
    return new_obc, new_outs

def FO(obc,outs,ifin=False): #DONE
    new_outs = outs + 1
    if outs < 2 and obc in {3,5,6,7}:
        ab_stats.stats_dict["PA"] += 1
        ab_stats.stats_dict["SF"] += 1
        ab_stats.stats_dict["R"] += 1
        match obc:
            case 3:
                new_obc = 0
            case 5:
                new_obc = 1
            case 6:
                new_obc = 2
            case 7:
                new_obc = 4
    else:
        ab_stats.add_ab()
        new_obc = obc
    return new_obc, new_outs

def K(obc,outs,ifin=False): #DONE
    ab_stats.add_ab()
    ab_stats.stats_dict["K"] += 1
    new_obc = obc
    new_outs = outs + 1
    return new_obc, new_outs

def PO(obc,outs,ifin=False): #DONE
    ab_stats.add_ab()
    new_obc = obc
    new_outs = outs + 1
    return new_obc, new_outs

def RGO(obc,outs,ifin=False):
    ab_stats.add_ab()
    if outs == 2:
        new_obc = 0
        new_outs = outs + 1
    else:
        match obc:
            case 0:
                new_outs = outs + 1
                new_obc = 0
            case 1:
                new_outs = outs + 2
                new_obc = 0
                ab_stats.stats_dict["DP"] += 1
            case 2:
                new_outs = outs + 1
                new_obc = 3
                ab_stats.stats_dict["Adv 2nd"] += 1
            case 3:
                if ifin:
                    new_outs = outs + 1
                    new_obc = 3
                else:
                    new_outs = outs + 1
                    new_obc = 0
                    ab_stats.stats_dict["R"] += 1
            case 4:
                new_outs = outs + 2
                new_obc = 3
                ab_stats.stats_dict["DP"] += 1
            case 5:
                if ifin:
                    new_outs = outs + 1
                    new_obc = 6
                else:
                    new_outs = outs + 2
                    new_obc = 0
                    ab_stats.stats_dict["DP"] += 1
                    if new_outs < 3:
                        ab_stats.stats_dict["R"] += 1
            case 6:
                if ifin:
                    new_obc = obc
                    new_outs = outs + 1
                else:
                    new_outs = outs + 1
                    ab_stats.stats_dict["R"] += 1
                    new_obc = 3
                    ab_stats.stats_dict["Adv 2nd"] += 1
            case 7:
                if ifin:
                    new_obc = 7
                    new_outs = outs + 1
                else:
                    new_outs = outs + 2
                    new_obc = 3
                    if new_outs < 3:
                        ab_stats.stats_dict["R"] += 1
    return new_obc, new_outs

def LGO(obc,outs,ifin=False):
    ab_stats.add_ab()
    if outs == 2:
        new_obc = 0
        new_outs = 3
        return new_obc, new_outs
    match obc:
        case 0:
            new_obc = 0
            new_outs = outs + 1
        case 1:
            new_outs = outs + 2
            new_obc = 0
            ab_stats.stats_dict["DP"] += 1
        case 2:
            new_obc = 2
            new_outs = outs + 1
        case 3:
            if ifin:
                new_outs = outs + 1
                new_obc = 3
            else:
                new_outs = outs + 1
                new_obc = 0
                ab_stats.stats_dict["R"] += 1
        case 4:
            new_outs = outs + 2
            new_obc = 3
            ab_stats.stats_dict["DP"] += 1
        case 5:
            if ifin:
                new_outs = outs + 1
                new_obc = 6
            else:
                new_outs = outs + 2
                new_obc = 0
                ab_stats.stats_dict["DP"] += 1
                if new_outs < 3:
                    ab_stats.stats_dict["R"] += 1
        case 6:
            if ifin:
                new_obc = 6
                new_outs = outs + 1
            else:
                new_outs = outs + 1
                new_obc = 2
                ab_stats.stats_dict["R"] += 1
        case 7:
            if ifin:
                new_outs = outs + 1
                new_obc = 7
            else:
                new_outs = outs + 2
                new_obc = 3
                ab_stats.stats_dict["DP"] += 1
                if new_outs < 3:
                    ab_stats.stats_dict["R"] += 1
    return new_obc, new_outs
# "ON BASE CODE"
# 0-Bases Empty
# 1-Runner 1st
# 2-Runner 2nd
# 3-Runner 3rd
# 4-1st and 2nd
# 5-1st and 3rd
# 6-2nd and 3rd
# 7-Bases Loaded
def SB(obc,outs,ifin=False):
    ab_stats.stats_dict["SA"] += 1
    ab_stats.stats_dict["SB"] += 1
    new_outs = outs
    match obc:
        case 1:
            new_obc = 2
        case 5:
            new_obc = 6
            
    return new_obc, new_outs

def CS(obc, outs,ifin=False):
    ab_stats.stats_dict["SA"] += 1
    new_outs = outs + 1
    match obc:
        case 1:
            new_obc = 0
        case 5: 
            new_obc = 3
    return new_obc, new_outs

# NEW STUFF
def RFO(obc,outs,ifin=False):
    if outs == 2:
        new_obc = 0
        new_outs = 3
        ab_stats.add_ab()
        return new_obc,new_outs
    match obc:
        case 0:
            new_obc = 0
            new_outs = outs + 1
            ab_stats.add_ab()
        case 1:
            new_obc = 1
            new_outs = outs + 1
            ab_stats.add_ab()
        case 2:
            new_obc = 3
            new_outs = outs + 1
            ab_stats.stats_dict["Adv 2nd"] += 1
            ab_stats.add_ab()
        case 3:
            new_obc = 0
            new_outs = outs + 1
            ab_stats.stats_dict["R"] += 1
            ab_stats.stats_dict["SF"] += 1
            ab_stats.stats_dict["PA"] += 1
        case 4:
            new_obc = 5
            new_outs = outs + 1
            ab_stats.stats_dict["Adv 2nd"] += 1
            ab_stats.add_ab()
        case 5:
            new_obc = 1
            new_outs = outs + 1
            ab_stats.stats_dict["R"] += 1
            ab_stats.stats_dict["SF"] += 1
            ab_stats.stats_dict["PA"] += 1
        case 6:
            new_obc = 3
            new_outs = outs + 1
            ab_stats.stats_dict["R"] += 1
            ab_stats.stats_dict["SF"] += 1
            ab_stats.stats_dict["PA"] += 1
            ab_stats.stats_dict["Adv 2nd"] += 1
        case 7:
            new_obc = 5
            new_outs = outs + 1
            ab_stats.stats_dict["R"] += 1
            ab_stats.stats_dict["SF"] += 1
            ab_stats.stats_dict["PA"] += 1
            ab_stats.stats_dict["Adv 2nd"] += 1
    return new_obc, new_outs

def LFO(obc,outs,ifin=False):
    new_outs = outs + 1
    if outs < 2 and obc in {3,5,6,7}:
        ab_stats.stats_dict["PA"] += 1
        ab_stats.stats_dict["SF"] += 1
        ab_stats.stats_dict["R"] += 1
        match obc:
            case 3:
                new_obc = 0
            case 5:
                new_obc = 1
            case 6:
                new_obc = 2
            case 7:
                new_obc = 4
    else:
        ab_stats.add_ab()
        new_obc = obc
    return new_obc, new_outs
# "ON BASE CODE"
# 0-Bases Empty
# 1-Runner 1st
# 2-Runner 2nd
# 3-Runner 3rd
# 4-1st and 2nd
# 5-1st and 3rd
# 6-2nd and 3rd
# 7-Bases Loaded
def GO(obc,outs,ifin=False):
    ab_stats.add_ab()
    if outs == 2:
        new_obc = 0
        new_outs = 3
        return new_obc, new_outs
    match obc:
        case 0:
            new_obc = 0
            new_outs = outs + 1
        case 1:
            new_outs = outs + 2
            new_obc = 0
            ab_stats.stats_dict["DP"] += 1
        case 2:
            new_obc = 2
            new_outs = outs + 1
        case 3:
            if ifin:
                new_outs = outs + 1
                new_obc = 3
            else:
                new_outs = outs + 1
                new_obc = 0
                ab_stats.stats_dict["R"] += 1
        case 4:
            new_outs = outs + 2
            new_obc = 3
            ab_stats.stats_dict["DP"] += 1
        case 5:
            if ifin:
                new_outs = outs + 1
                new_obc = 6
            else:
                new_outs = outs + 2
                new_obc = 0
                ab_stats.stats_dict["DP"] += 1
                if new_outs < 3:
                    ab_stats.stats_dict["R"] += 1
        case 6:
            if ifin:
                new_obc = 6
                new_outs = outs + 1
            else:
                new_outs = outs + 1
                new_obc = 2
                ab_stats.stats_dict["R"] += 1
        case 7:
            if ifin:
                new_outs = outs + 1
                new_obc = 7
            else:
                new_outs = outs + 2
                new_obc = 3
                ab_stats.stats_dict["DP"] += 1
                if new_outs < 3:
                    ab_stats.stats_dict["R"] += 1
    return new_obc, new_outs