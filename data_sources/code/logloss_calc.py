import csv
import sys
import math

def calc_log(sampsub, actsub):
    """ python implementation of logloss function"""
    sampsubfile = open(sampsub,'rb')
    actsubfile = open(actsub,'rb')

    sampcsvreader = csv.reader(sampsubfile,delimiter=',')
    sampcsvreader.next()
    actcsvreader = csv.reader(actsubfile,delimiter=',')
    actcsvreader.next()

    y = []
    yhat = []

    for row in sampcsvreader:
        y.append(float(row[1]))
    for row in actcsvreader:
        yhat.append(float(row[1]))
    print len(y)
    const = (-float(len(y)))
    print("const = "+str(const))
    stuff = zip(y,yhat)
    thing = 0.0
    for i,k in stuff:
        #print i,k
        thing += i*math.log(k,math.e)+(1.0-i)*math.log(1.0-k,math.e)
    return thing/const
    
    


if __name__ == '__main__':
    """ [1] is sample submission
    [2] is actual submission

    """
    print(calc_log(sys.argv[1],sys.argv[2]))
