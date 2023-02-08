import statistics
import math
import numpy 
def fileIntoList(file):
    f=open(file,"r")
    l=[]
    f.readline()
    for i in f:
        l.append(float(i.split()[0]))
    return l
def mean(d):
    return sum(d)/len(d)
def median(d):
    d.sort();return (d[int(len(d)/2)]+d[int(len(d)/2-1)])/2 if len(d)%2==0 else d[int((len(d)/2)-0.5)]
def mode(d):
    i={}
    for n in d:
        if n not in i:
            i[n]=1
            continue
        i[n]+=1
    return max(i, key=i.get)
def variance(d):
    m=mean(d)
    x=0
    for i in d:
        x+=(i-m)*(i-m)
    return x/len(d)
def deviation(d):
    return math.sqrt(variance(d))
def covariance(d,d2,bool):
    if len(d)!=len(d2):
        return
    l=len(d)
    md=mean(d)
    md2=mean(d2)
    x=0
    for i in range(l):
        t=d[i]
        t2=d2[i]
        x+=(t-md)*(t2-md2)
    return x/(l-1) if bool else x/l
def corEff(d,d2):
    c=covariance(d,d2,True)
    return c/float((deviation(d))*(deviation(d2)))
def printData(d,d2,varUsed,bool):
    print("mean: ", mean(d if bool else d2))
    print("median: ", median(d if bool else d2))
    print("mode: ", mode(d if bool else d2))
    print("variance: ", variance(d if bool else d2))
    print("deviation: ", deviation(d if bool else d2))
    if bool:
        print("covariance: ", covariance(d,d2, True))
        print("correlation efficent: ", corEff(d,d2))


