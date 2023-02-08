import matplotlib.pyplot as plt
import numpy as np
from functions import fileIntoList
filename="Unit_6/netflixProject/files/subGrowthQ.txt"
data=fileIntoList(filename)
years=[]
for i in range(2013,2023):
    years.append(str(i)+"Q1")
    years.append("")
    years.append("")
    years.append("")
    i+=1
years.pop(-1)
years.pop(-1)
x=np.array(range(0,38))
y=np.array(data)
# plt.subplot(param)
plt.bar(x,y)
plt.title("Netflix sub growth by quarter")
plt.xlabel("Quarter")
plt.ylabel("Sub Growth(Millions)")
#xticks setup
plt.xticks(ticks=range(0,38),labels=years)
#yticks setup
plt.yticks(ticks=range(-2,17))
plt.grid(axis="y",linestyle="--")
plt.show()
