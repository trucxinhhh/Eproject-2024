from cProfile import label
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

n=5

Y=[1,2,3,4,5]
Y1= pd.DataFrame(Y[::-1]).transpose()
print(Y1)
a = [7,8,9,10,11,12]

for i in range (n):
    Y.append(a[i])
    print(Y)
    del Y[0]

print(Y1)

