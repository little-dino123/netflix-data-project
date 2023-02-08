import matplotlib.pyplot as plt
import numpy as np
from functions import fileIntoList
def graphTotalSubQuarter(filename,param):
    data=fileIntoList(filename)
    years=[]
    for i in range(2013,2023):
        years.append(str(i)+" Q1")
        years.append("")
        years.append("")
        years.append("")
        i+=1
    years.pop(-1)
    years.pop(-1)
    x=np.array(range(0,39))
    y=np.array(data)
    plt.bar(x,y)
    plt.title("Netflix Total Subs by quarter",fontsize=15)
    plt.xlabel("Quarter",fontsize=15)
    plt.ylabel("Total Subs(Millions)",fontsize=15)
    #xticks setup
    plt.xticks(ticks=range(0,38),labels=years)
    #yticks setup
    plt.yticks(ticks=range(0,251,5),minor=True)
    plt.grid(which="major",axis="y",linestyle=(0,()),linewidth=1.5, color="#545454")
    plt.grid(which="minor",axis="y",linestyle=(0,(5,5)))
    plt.subplot(param)