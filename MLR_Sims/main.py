
import ab_stats
import game_sim
import pandas as pd
import numpy as np

#check that batters sum to 250 and pitchers to 251
#check that batters and pitchers have the same results in the same order

#generate a diff - we're going to go with random for now, but it'd be interesting to see if there's any correlation with like lower diffs following lower diffs.

#check game situation - if there is a tier 1 or 2 stealer able to steal (obc of 1 or 5), diff is used for a steal attempt
#   how are we tracking what type is on first
#   could be fun to add a percent chance that each tier would go... like tier 1 goes 90%, 2 80%, 3 50% etc, but not rn

#batter types change each AB, pitchers each inning

#check game situation - call infield in if:
#    - obc of 3 (3rd) and 0 or 1 outs
#    - obc of 5 (1st/3rd) and 0 outs
#    - obc of 6 (2nd/3rd) and 0 or 1 outs
#    - obc of 7 (loaded) and 0 outs

# calculate result with ranges
# idk how to handle infield in affecting RGO/LGO vs GO yet, but we'll cross that bridge when we get there

# take result and calculate new game state
# log result

df = pd.DataFrame(columns=['bType','pType','ranges',"PA","AB","H","BB","1B","2B","3B","HR","R","K","SF","DP","Adv 2nd","SA","SB"])

pTypes = ['BB','BS','BF','NH','FP','TT','TD','EG','1B','EN','WC','NT','SF']
bTypes = ['BN','BP','BC','MH','S','XB','1B','EN','WC','HK','TT','SM','SF']
numInnings = 100000

old_ranges = [True,True,True,True,True,False,False,False,False,False]

for range_type in old_ranges:

    for batter in bTypes:
        print("Testing batter", batter)
        game_sim.testBatterType(batter,range_type,numInnings)
        new_row = ab_stats.stats_dict
        new_row['bType'] = batter
        new_row['pType'] = 'All'
        if range_type:
            new_row['ranges'] = 'OLD'
        else:
            new_row['ranges'] = 'NEW'
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        ab_stats.stats_dict = ab_stats.reset_stats(ab_stats.stats_dict)

    for pitcher in pTypes:
        print("Testing pitcher", pitcher)
        game_sim.testPitcherType(pitcher,range_type,numInnings)
        new_row = ab_stats.stats_dict
        new_row['bType'] = 'All'
        new_row['pType'] = pitcher
        if range_type:
            new_row['ranges'] = 'OLD'
        else:
            new_row['ranges'] = 'NEW'
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        ab_stats.stats_dict = ab_stats.reset_stats(ab_stats.stats_dict)
        
    print("Testing League")
    game_sim.testLeague(range_type,numInnings)
    new_row = ab_stats.stats_dict
    new_row['bType'] = 'All'
    new_row['pType'] = 'All'
    if range_type:
        new_row['ranges'] = 'OLD'
    else:
        new_row['ranges'] = 'NEW'
    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    ab_stats.stats_dict = ab_stats.reset_stats(ab_stats.stats_dict)

df = df.sort_values(by=['bType','pType','ranges'])

df['AVG'] = (df['H'] / df['AB'])

df['OBP'] = (df['H'] + df['BB']) / df['PA']

df['ER6'] = (df['R'] / numInnings) * 6

print(df)
df.to_csv('results.csv')