import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

master = pd.read_csv("teams_rpi_sos_pe.csv")

season_totals_dict = {}

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
                else:
                    #CREATE
                     season_totals_dict[season + '_' + win_team] = {"fgm" : w_fgm, "fga" : w_fga,
                                                               "3fgm" : w_3fgm, "fta" : w_fta,
                                                               "ftm" : w_ftm, "to" : w_to,
                                                               "orb" : w_orb, "drb" : w_drb}
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
                #CREATE
                else:
                     season_totals_dict[season + '_' + loss_team] = {"fgm" : l_fgm, "fga" : l_fga,
                                                               "3fgm" : l_3fgm, "fta" : l_fta,
                                                               "ftm" : l_ftm, "to" : l_to,
                                                               "orb" : l_orb, "drb" : l_drb}
               
print pd.DataFrame(season_totals_dict).T
