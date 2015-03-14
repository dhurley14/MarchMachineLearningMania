import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#master = pd.read_csv("teams_rpi_sos_pe.csv")
#csvreader = csv.reader("teams_rpi_sos_pe.csv")
# BUILD DICT FOR GETTING SOS
team_id_year_sos_dict = {}
with open("teams_rpi_sos_pe.csv",'rb') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    for row in csvreader:
        team_id_year_sos_dict[str(row[1])+"_"+str(row[2])] = row[5]

print team_id_year_sos_dict

season_totals_dict = {}


def find_sos(ateam,aseason):
    return float(team_id_year_sos_dict[str(aseason)+"_"+str(ateam)])

with open('regular_season_detailed_results.csv','rb') as theFile:
        theReader = csv.reader(theFile,delimiter=',')
        next(theReader,None)
        for row in theReader:
            if int(row[0]) > 2002:
                
                #GET DATA FOR WINNING TEAM
                win_team = row[2]
                season = row[0]
                #temp = master.query("id == @win_team & year == @season")
                w_fgm = int(row[8])
                w_fga = int(row[9])
                w_3fgm = int(row[10])
                w_ftm = int(row[12])
                w_fta = int(row[13])
                w_orb = int(row[14])
                w_drb = int(row[15])
                w_to = int(row[17])
                opp_drb = int(row[28])
    
                #CHECK TO SEE IF KEY EXISTS
                if season + '_' + win_team in season_totals_dict.keys():
                    #UPDATE
                    season_totals_dict[season + '_' + win_team]["fgm"] += w_fgm
                    season_totals_dict[season + '_' + win_team]["fga"] += w_fga
                    season_totals_dict[season + '_' + win_team]["3fgm"] += w_3fgm
                    season_totals_dict[season + '_' + win_team]["fta"] += w_fta
                    season_totals_dict[season + '_' + win_team]["ftm"] += w_ftm
                    season_totals_dict[season + '_' + win_team]["to"] += w_to
                    season_totals_dict[season + '_' + win_team]["orb"] += w_orb
                    season_totals_dict[season + '_' + win_team]["drb"] += w_drb
                    season_totals_dict[season + '_' + win_team]["opp_drb"] += opp_drb
                else:
                    #CREATE
                     season_totals_dict[season + '_' + win_team] = {"fgm" : w_fgm, "fga" : w_fga,
                                                               "3fgm" : w_3fgm, "fta" : w_fta,
                                                               "ftm" : w_ftm, "to" : w_to,
                                                               "orb" : w_orb, "drb" : w_drb,
                                                               "opp_drb" : opp_drb}
                #NOW FOR THE LOSING TEAM
                        #Probably could've reused the w_variables. Shit.
                loss_team = row[4]
                #temp = master.query("id == @win_team & year == @season")
                l_fgm = int(row[21])
                l_fga = int(row[22])
                l_3fgm = int(row[23])
                l_ftm = int(row[25])
                l_fta = int(row[26])
                l_orb = int(row[27])
                l_drb = int(row[28])
                l_to = int(row[30])
                l_opp_drb = w_drb
    
                #UPDATE
                if season + '_' + loss_team in season_totals_dict.keys():
                    season_totals_dict[season + '_' + loss_team]["fgm"] += l_fgm
                    season_totals_dict[season + '_' + loss_team]["fga"] += l_fga
                    season_totals_dict[season + '_' + loss_team]["3fgm"] += l_3fgm
                    season_totals_dict[season + '_' + loss_team]["fta"] += l_fta
                    season_totals_dict[season + '_' + loss_team]["ftm"] += l_ftm
                    season_totals_dict[season + '_' + loss_team]["to"] += l_to
                    season_totals_dict[season + '_' + loss_team]["orb"] += l_orb
                    season_totals_dict[season + '_' + loss_team]["drb"] += l_drb
                    season_totals_dict[season + '_' + loss_team]["opp_drb"] += l_opp_drb
                #CREATE
                else:
                     season_totals_dict[season + '_' + loss_team] = {"fgm" : l_fgm, "fga" : l_fga,
                                                               "3fgm" : l_3fgm, "fta" : l_fta,
                                                               "ftm" : l_ftm, "to" : l_to,
                                                               "orb" : l_orb, "drb" : l_drb,
                                                               "opp_drb": l_opp_drb}
               
four_factors_df = pd.DataFrame(columns = ['Year', 'id', 'Tov per Poss', 
                                          'EFG','Off Reb %',
                                          'FTM per FGA'])

for team in season_totals_dict:
   
    season = team[:4]
    team_id = team[-4:]
    try:
        sos = find_sos(team_id,season)
    except Exception, e:
        print(e)
    #PUT DICT INTO TEMP VARIABLE TO REDUCE CONFUSION OF EXTRA BRACKETS
    temp = season_totals_dict[team]
    
    #TURNOVERS PER POSSESION. THATS MY PSUEDO POSSESION COUNT. ITS A FREAKING ESTIMATE.
    poss = temp['fga'] + temp['fta']/2 + temp['to'] - temp['orb']
    tov_per_poss = float(temp['to']) / float(poss)
    
    #EFFECTIVE FIELD GOAL %
    efg = (float(temp['fgm']) + .5 * float(temp['3fgm'])) / float(temp['fga'])
    
    #OFFENSIVE REBOUND PERCENTAGE
    orb_percent = float(temp['orb']) / float(temp['orb'] + temp['opp_drb'])
    
    #FTM PER FGA
    ftm_per_fga = float(temp['ftm']) / float(temp['fga'])

    # WEIGHT OSCAR SCORE BY SOS - DEVIN
    oscar_score = ftm_per_fga*sos + orb_percent*sos + efg*sos + tov_per_poss*sos
    if oscar_score >= 1.0 or oscar_score <= 0.0:
        print("oscar score: "+str(oscar_score))
    some_list = pd.Series([season, team_id, tov_per_poss, efg, orb_percent, ftm_per_fga, oscar_score], index = 
                          ['Year', 'id', 'Tov per Poss', 
                                          'EFG','Off Reb %',
                                          'FTM per FGA','Oscar score'])
    four_factors_df = four_factors_df.append(some_list, ignore_index = True)

# save four_factors_df to csv.
#print(four_factors_df)
four_factors_df.to_csv("four_factors_df.csv")
print("wrote to csv")

    

