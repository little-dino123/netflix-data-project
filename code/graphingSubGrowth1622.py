import matplotlib.pyplot as plt
import numpy as np
from functions import fileIntoList
def graphSubGrowth1622(filename1, param):
    data=fileIntoList(filename1)
    data2=fileIntoList(filename1)
    years=range(2016,2023)
    x=np.array(years)
    y=np.array(data)
    plt.subplot(param)
    plt.bar(x,y)
    plt.title("Netflix Sub Growth by Year")
    plt.xlabel("Year")
    plt.ylabel("Sub Growth(Millions)")
    #xticks setup
    # plt.xticks(ticks=range(0,38),labels=years)
    #yticks setup
    # plt.yticks(ticks=range(-2,17))
    plt.grid(axis="y",linestyle="--")