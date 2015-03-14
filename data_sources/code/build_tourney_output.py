import csv
import collections
def get_matchups():
    subsfile = open("sample_submission.csv",'rb')
    csvreader = csv.reader(subsfile,delimiter=',')
    csvreader.next()
    toreturn = collections.OrderedDict()
    for row in csvreader:
        toreturn[str(row[0])] = 0
    return toreturn

def main():
    """ generate a sample submission file with 1 for 
    teamA beating teamB and 0 vice versa

    """
    thedict = get_matchups()
    tourney = open("tourney_compact_results.csv",'rb')
    csvreader = csv.reader(tourney,delimiter=',')
    csvreader.next()
    for row in csvreader:
        #get matchup
        if int(row[0]) == 2011 and (int(row[2]) == 1139 or int(row[4]) == 1139) and (int(row[2]) == 1458 or int(row[4]) == 1458):
            print(str(row[0])+"_"+str(row[2])+"_"+str(row[4]))
        if int(row[0]) >= 2011:
            try:
                if thedict[str(row[0])+"_"+str(row[2])+"_"+str(row[4])] != None:
                    thedict[str(row[0])+"_"+str(row[2])+"_"+str(row[4])] = 1
                if thedict[str(row[0])+"_"+str(row[4])+"_"+str(row[2])] != None:
                    thedict[str(row[0])+"_"+str(row[4])+"_"+str(row[2])] = 1
                
            except Exception, e:
                print(" ")
    target = open("tourney_outs.csv",'wb')
    csvwriter = csv.writer(target,delimiter=',')
    for key in thedict.keys():
        csvwriter.writerow([key,thedict[key]])
    target.close()
    tourney.close()
    print("closed stuff")

if __name__ == '__main__':
    main()
