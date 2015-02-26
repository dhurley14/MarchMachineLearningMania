import csv
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
    
    with open(somefile,'rb') as theFile:
        theReader = csv.reader(theFile,delimiter=',')
        next(theReader,None)       
        for row in theReader:
            if int(row[0]) == int(seedyear):
                #print row[2],row[4]
                toappend = 0

                if len(row[2]) == 3: #sometimes the seed has three chars, othertimes it has 4..
                    toappend = int(row[2][1:])

                else:
                    toappend = int(row[2][1:3])

                team_seeds_dict[int(row[2])] = toappend

    print len(team_seeds_dict.keys())
    #print team_wins_dict
    #return team_wins_dict

    with open('team_seeds_dict_'+str(seedyear)) as writefile:
        writefile.write(team_seeds_dict)

    return None

if __name__ == '__main__':
    # [1] - seedfile path
    # [2] - seed year
    build_seed_dict(sys.argv[1],sys.argv[2])
