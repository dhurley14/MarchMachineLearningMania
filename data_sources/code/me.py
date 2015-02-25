import csv

training = open('training1.csv','wb')
test = open('test1.csv', 'wb')

with open('../tourney_compact_results.csv','rb') as readFile:
    for line in readFile:
        if "2005" in line[0:4] or "2006" in line[0:4]:
            test.write(line)
        elif int(line[0:4]) > 2006:
            training.write(line)
        else:
            continue


training.close()
test.close()
