import csv


def compute_log5_probability(pa,pb):
    result = (pa - (pa*pb))/(pa + pb - 2*(pa*pb))
    print result
    return result

def compute_seed_probability(seedA, seedB):
    result = .5+(seedB - seedA)*.03
    return result

def get_wins(somefile):
    # function computes the win percentage
    # for each team between 2006 and 2011
    # not really utilizing this method much anymore.
    team_wins_dict = {}
    with open('regular_season_compact_results.csv','rb') as theFile:
        theReader = csv.reader(theFile,delimiter=',')
        next(theReader,None)
        
        for row in theReader:
            if int(row[0]) > 2005 and int(row[0]) < 2011:
                #print row[2],row[4]
                try:
                    team_wins_dict[int(row[2])] = [int(team_wins_dict[int(row[2])][0])+1,int(team_wins_dict[int(row[2])][1])+1]
                except Exception, e:
                    print("error,"+str(e))
                    team_wins_dict[int(row[2])] = [1,1]
                try:
                    team_wins_dict[int(row[4])] = [int(team_wins_dict[int(row[4])][0]),int(team_wins_dict[int(row[4])][1])+1]
                except Exception, e:
                    print("error,"+str(e))
                    team_wins_dict[int(row[4])] = [0,1]
                #team_wins_dict[row[2]] = [1,1]
                #team_wins_dict[row[4]] = [0,1]
			
    print len(team_wins_dict.keys())
    print team_wins_dict
    return team_wins_dict
	
	
def print_percentages(aDict):

    team_keys = aDict.keys()
    print "in print_percentages"
    output = []
    pOne = 0.0
    pTwo = 0.0
    for team_one in team_keys:
        print aDict[team_one][0]
        pOne = float(aDict[team_one][0])/float(aDict[team_one][1])
        #print pOne

        for team_two in team_keys:

    	        if team_one != team_two and ((str(team_one)+"_"+str(team_two)) not in output or (str(team_two)+"_"+str(team_one)) not in output):
    	            pTwo = float(aDict[team_two][0])/float(aDict[team_two][1])
                print pTwo
                final_prob = compute_seed_probability(#compute_log5_probability(pOne,pTwo)
                output.append((str(team_one)+"_"+str(team_two),final_prob))


    target = open('results.csv','wb')
    for i in xrange(4):
        year = "201"+str((i+1))
        for item in output:
            target.write(str(year)+"_"+str(item[0])+", "+str(item[1])+'\n')
			
    target.close()
    print "target closed"
		
if __name__ == '__main__':
    print_percentages(get_wins("hi"))

