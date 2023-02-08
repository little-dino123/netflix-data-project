import matplotlib.pyplot as plt
import numpy as np
from functions import fileIntoList
from graphingGrowthQ import graphSubGainQuarter
from graphingGrowthY import graphSubGainYear
from graphingTotalQ import graphTotalSubQuarter
from graphingSubGrowth1622 import graphSubGrowth1622
from graphingSpending1622 import graphSpending1622
def graph(func,file,param):
    func(file,param)