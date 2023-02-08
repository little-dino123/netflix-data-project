import matplotlib.pyplot as plt
import numpy as np
from functions import fileIntoList
def graphSubGainYear(filename,param):
    data=fileIntoList(filename)
    x=np.array(range(2013,2023))
    y=np.array(data)
    plt.subplot(param)
    plt.bar(x,y)
    plt.title("Netflix sub growth by year")
    plt.xlabel("Year")
    plt.ylabel("Sub Growth(Millions)")
    plt.xticks(ticks=range(2013,2023))
    plt.grid(axis="y",linestyle="--")