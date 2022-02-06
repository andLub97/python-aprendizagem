import numpy as np
import pandas as pd
#inFile = 'data.txt'
#df = pd.read_csv(inFile)
# print(df.head()) #checando se a primeira linha está ok
# print(df.tail1-()) #última linha

# data = np.loadtxt('data.txt', delimiter=',')
# print(data)

df = pd.read_csv('data.txt', header=None)
print(df)
