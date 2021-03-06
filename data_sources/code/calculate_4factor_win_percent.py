import csv

"""
season = 2011
team_id = 1104
print four_factors_df2.query('id == @team_id & Year == @season').Year.values
"""
winners_win = 0
count = 0
with open('tourney_compact_results.csv','rb') as theFile:
    theReader = csv.reader(theFile,delimiter=',')
    next(theReader,None)
    for row in theReader:
        if int(row[0]) > 2002:
             
            season = int(row[0])
            winning_team = int(row[2])
            losing_team = int(row[4])
            win_team_df = four_factors_df2.query("Year == @season & id == @winning_team")
            loss_team_df = four_factors_df2.query("Year == @season & id == @losing_team")
            win_team_sos = master.query("year == @season & id == @winning_team")
            loss_team_sos = master.query("year == @season & id == @losing_team")
            #MULTIPLY BY SOS TO SEE HOW IT REALLY WORKS. THIS ISNT THE NBA. EVERY TEAM
            #DOES NOT PLAY EVERY TEAM. SO 13 SEEDS ARE BEATING UP ON CRAP TEAMS AND PADDING
            #THEIR STATS
            win_team_efg = win_team_df.efg.values[0] * float(win_team_sos.SOS.values[0])
            loss_team_efg = loss_team_df.efg.values[0] *float(loss_team_sos.SOS.values[0])
            
            #print win_team_efg, loss_team_efg
            if win_team_efg > loss_team_efg:
                winners_win_efg += 1

            #CALCULATE TOV PER POSSESSION
            win_team_tov_per_poss = win_team_df.tov_per_poss.values[0] * float(1/float(win_team_sos.SOS.values[0]))
            loss_team_tov_per_poss = loss_team_df.tov_per_poss.values[0] * float(1/float(loss_team_sos.SOS.values[0]))
            
            #SEE IF WINNING TEAM HAD LOWER TURNOVERS PER POSSESSION
            if win_team_tov_per_poss < loss_team_tov_per_poss:
                winners_win_tov_per_poss += 1
            
            #CALCULATE OFFENSIVE REBOUND %
            win_team_off_reb_percent = win_team_df.off_reb_percent.values[0] * float(win_team_sos.SOS.values[0])
            loss_team_off_reb_percent = loss_team_df.off_reb_percent.values[0] *float(loss_team_sos.SOS.values[0])

            #CALCULATE OFF REB PERCENT WIN PERCENTAGE
            if win_team_off_reb_percent > loss_team_off_reb_percent:
                winners_win_off_reb_percent += 1
            
            #CALCULATE FTM PER FGA
            win_team_ftm_per_fga = win_team_df.ftm_per_fga.values[0] * float(win_team_sos.SOS.values[0])
            loss_team_ftm_per_fga = loss_team_df.ftm_per_fga.values[0] *float(loss_team_sos.SOS.values[0])
            
            #print win_team_efg, loss_team_efg
            if win_team_ftm_per_fga > loss_team_ftm_per_fga:
                winners_win_ftm_per_fga += 1
            
            count += 1
print "EFG" ,float(winners_win_efg)/float(count)
print "TOV" ,float(winners_win_tov_per_poss)/float(count)
print "ORB%" ,float(winners_win_off_reb_percent)/float(count)
print "FTM per FGA" ,float(winners_win_ftm_per_fga)/float(count)
