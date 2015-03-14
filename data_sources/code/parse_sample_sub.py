import csv

def parse_teams(someRow):
    print someRow
    out = someRow.split("_")
    return int(out[0]),int(out[1]),int(out[2])


def open_subs(csvfile="sample_submission.csv"):
    csvfile = open('sample_submission.csv','rb') #open file for reading and writing
    csvreader = csv.reader(csvfile,delimiter=',')
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
