import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from bokeh.sampledata.iris import flowers as dados

#print(dados.shape)

print(dados.head(3))

#média
print(np.mean(dados['sepal_length']))
#mediana
print(np.median(dados['sepal_length']))

moda_sl = dados['sepal_length'].mode()
print(moda_sl)
# 0 -> só há uma moda
# e no exemplo, a moda é 5

