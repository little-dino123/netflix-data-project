import matplotlib.pyplot as plt
import numpy as np
from functions import fileIntoList
filename="Unit_6/netflixProject/files/spending1622.txt"
data=fileIntoList(filename)
years=range(2016,2023)
x=np.array(years)
y=np.array(data)
plt.bar(x,y)
plt.subplot(121)
plt.title("Netflix Spending by Year")
plt.xlabel("Year")
plt.ylabel("Spending")
#xticks setup
# plt.xticks(ticks=range(0,7),labels=years)
#yticks setup
# plt.yticks(ticks=range(-2,17))
plt.grid(axis="y",linestyle="--")

filename="Unit_6/netflixProject/files/subGrowth1622.txt"
data=fileIntoList(filename)
years=range(2016,2023)
x1=np.array(years)
y1=np.array(data)
plt.bar(x1,y1)
plt.subplot(122)
plt.title("Netflix Sub Growth by Year")
plt.xlabel("Year")
plt.ylabel("Sub Growth(Millions)")
#xticks setup
# plt.xticks(ticks=range(0,7),labels=years)
#yticks setup
# plt.yticks(ticks=range(-2,17))
plt.grid(axis="y",linestyle="--")
plt.show()
