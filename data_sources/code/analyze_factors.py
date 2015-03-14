import csv

""" this file will read the four_factors_df.csv
and create a win probability based on the Oscar
scores that were built in the 4_factor_analysis.py
file.

"""
year_team_oscar_dict = {}
with open("four_factors_df.csv",'rb') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        year_team_oscar_dict[str(row[1])+"_"+str(row[2])] = row[7]

print(len(year_team_oscar_dict))

def parse_teams(someRow):
    print someRow
    out = someRow.split("_")
    return int(out[0]),int(out[1]),int(out[2])


def gen_probs(year,teamA,teamB):
    """ get Oscar score for teamA, teamB
    return (teamA oscar score)/(teamA oscar score +
        teamB oscar score)

    """
    #return (float(year_team_oscar_dict[str(year)+"_"+str(teamA)]))/(float(year_team_oscar_dict[str(year)+"_"+str(teamA)]) + float(year_team_oscar_dict[str(year)+"_"+str(teamB)]))
    #return float(year_team_oscar_dict[str(year)+"_"+str(teamA)])
    if float(year_team_oscar_dict[str(year)+"_"+str(teamA)]) > float(year_team_oscar_dict[str(year)+"_"+str(teamB)]):
        return float(year_team_oscar_dict[str(year)+"_"+str(teamA)])
    else:
        return 1.0 - float(year_team_oscar_dict[str(year)+"_"+str(teamB)])


""" get matchups from sample sub
and calculate probabilities for matchups
and write output to results.csv

"""
sample_subs_file = open('sample_submission.csv','rb')
target = open('results_from_oscars.csv','wb')
csvwriter = csv.writer(target,delimiter=',')
reader = csv.reader(sample_subs_file,delimiter=',')
reader.next()
for row in reader:
    season, teama, teamb = parse_teams(row[0])
    prob = gen_probs(season, teama, teamb)
    csvwriter.writerow([row[0],prob])

sample_subs_file.close()
target.close()
print "target closed"

