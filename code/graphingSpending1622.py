import matplotlib.pyplot as plt
import numpy as np
from functions import fileIntoList
def graphSpending1622(filename, param):
    data=fileIntoList(filename)
    data2=fileIntoList(filename)
    years=range(2016,2023)
    x=np.array(years)
    y=np.array(data)
    plt.subplot(param)
    plt.bar(x,y)
    plt.title("Netflix Spending by Year")
    plt.xlabel("Year")
    plt.ylabel("Spending")
    #xticks setup
    # plt.xticks(ticks=range(0,7),labels=years)
    #yticks setup
    # plt.yticks(ticks=range(-2,17))
    plt.grid(axis="y",linestyle="--")   