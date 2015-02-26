import csv

def get_wins(somefile,startyear, endyear):
    """function computes the win percentage
    for each team between startyear and endyear
    then writes the data to a dict file
    use ast.literal_eval(dict) to read dict
    in for future use.

    :param somefile: file to read wins from
    :param startyear: year to begin calculating win percentage
    :param endyear: year to end calculation of win percentage
    """
    
    team_wins_dict = {}
    with open(somefile,'rb') as theFile:
        theReader = csv.reader(theFile,delimiter=',')
        next(theReader,None)
        
        for row in theReader:
            if int(row[0]) > int(startyear) and int(row[0]) < int(endyear): #make sure the year (row[0]) is between our start and end years.
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
			



    print len(team_wins_dict.keys())
    #print team_wins_dict
    #return team_wins_dict

    with open('team_wins_dict_'+str(startyear)+'_'+str(endyear)) as writefile:
        writefile.write(team_wins_dict)

    return None
	

if __name__ == '__main__':
    # [1] is the file we're reading from
    # [2] is the start year to begin gathering win percentages
    # [3] is the end year.
    get_wins(sys.argv[1],sys.argv[2],sys.argv[3])

    
