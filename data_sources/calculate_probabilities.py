import csv
import ast
import sys



def build_seed_dict(seedfile,seedyear):
    """ create a python dict and write
    to text file so that info on team seeds
    per year is readily accessible

    :param seedfile: file containing the tourney seeds
    :param seedyear: year for which we are looking for seeds.
    
    """
    seed_csv = open('tourney_seeds.csv','rb')
    team_seeds_dict = {}
    
    with open(seedfile,'rb') as theFile:
        theReader = csv.reader(theFile,delimiter=',')
        next(theReader,None)       
        for row in theReader:
            if int(row[0]) == int(seedyear):
                #print row[2],row[4]
                toappend = 0

                if len(row[1]) == 3: #sometimes the seed has three chars, othertimes it has 4..
                    print row[1][1:]
                    toappend = int(row[1][1:])

                else:
                    print row[1][1:3]
                    toappend = int(row[1][1:3])

                team_seeds_dict[int(row[2])] = toappend

    print len(team_seeds_dict.keys())
    #print team_wins_dict
    #return team_wins_dict

    with open('team_seeds_dict_'+str(seedyear)+'.csv','wb') as writefile:
        writefile.write(str(team_seeds_dict))

    return None


def computeProbability(pa,pb):
    result = (pa - (pa*pb))/(pa + pb - 2*(pa*pb))
    print result
    return result

def compute_seeds_probability(seedA, seedB):
    #initial_pred = (0.5 + ((seedB - seedA)*.03))
    return (0.5 + ((seedB - seedA)*.02))

def parse_teams(someRow):
    print someRow
    out = someRow.split("_")
    return int(out[0]),int(out[1]),int(out[2])



	
def print_percentages_seeds(aDictFile, seedyear):
    """ compute probability of wins using the 
    seed based method suggested in the kaggle 
    leaderboard

    :param aDictFile: dict file containing team id's and associated seeds
    
    """
    dictfile = open(aDictFile).read()
    team_keys = ast.literal_eval(dictfile)
    csvfile = open('sample_submission.csv','rb') #open file for reading and writing
    csvreader = csv.reader(csvfile,delimiter=',')
    csvwritefile = open('seed_results.csv','ab') #output.
    csvwriter = csv.writer(csvwritefile,delimiter=',')
    csvreader.next()

    for row in csvreader:
        year, teama, teamb = parse_teams(row[0])
        if year == int(seedyear):
            prob = 0.0
            prob = compute_seeds_probability(team_keys[teama],team_keys[teamb])
            print prob
            csvwriter.writerow([row[0],prob])


    csvfile.close()
    csvwritefile.close()
    print "target closed"

def calc_probs(teamA, teamB):
    the_prob = ((teamA*(1-teamB))/((teamA*(1-teamB)+(1-teamA)*teamB)))
    if the_prob == 1.0:
        the_prob = .98
    if the_prob == 0.0:
        the_prob = 0.02
    return the_prob
    
def print_percentages_winProb(aDictFile):

    dictfile = open(aDictFile).read()
    team_keys = ast.literal_eval(dictfile)
    csvfile = open('sample_submission.csv','rb') #open file for reading and writing
    csvreader = csv.reader(csvfile,delimiter=',')
    csvwritefile = open('kalman_results.csv','wb') #output.
    csvwriter = csv.writer(csvwritefile,delimiter=',')
    csvreader.next()

    for row in csvreader:
        year, teama, teamb = parse_teams(row[0])
        print team_keys[teama], team_keys[teamb]
        prob = 0.0
        pOne = float(team_keys[teama][0])/float(team_keys[teama][1])
        pTwo = float(team_keys[teamb][0])/float(team_keys[teamb][1])
        prob = calc_probs(float(pOne),float(pTwo))
        print prob
        csvwriter.writerow([row[0],prob])


    csvfile.close()
    csvwritefile.close()
    print "target closed"

def print_percentages_log5(aDictFile):

    team_keys = aDict.keys()
    print "in print_percentages"
    """parse the team identifiers from the sample submission
    then do some stuff
    """
    csvfile = open('sample_submission.csv','rb') #open file for reading and writing
    csvreader = csv.reader(csvfile,delimiter=',')
    csvwritefile = open('results.csv','wb') #output.
    csvwriter = csv.writer(csvwritefile,delimiter=',')
    csvreader.next()
    for row in csvreader:
        year, team1, team2 = parse_teams(row[0])
        pOne = float(aDict[team1][0])/float(aDict[team1][1])
        pTwo = float(aDict[team2][0])/float(aDict[team2][1])
        final_prob = computeProbability(pOne,pTwo)
        csvwriter.writerow([row[0],final_prob])
			
    """target = open('results.csv','wb')
    for i in xrange(4):
        year = "201"+str((i+1))
        for item in output:
            target.write(year+"_"+item[0]+", "+item[1])
            
    target.close()
    """
    csvfile.close()
    csvwritefile.close()
    print "target closed"
        
if __name__ == '__main__':
    # make a few dicts for the seeds
    yearlist = ast.literal_eval(sys.argv[2])
    tourney_seed_file = sys.argv[1]
    for year in yearlist:
        #build_seed_dict(tourney_seed_file,year)
        print_percentages_winProb('team_wins_dict_'+str(year))
    #print_percentages(sys.argv[1])

    
