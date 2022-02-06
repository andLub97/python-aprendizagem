import numpy as np
import matplotlib.pyplot as plt

def plotVectors(vecs, cols, alpha=1):
    plt.figure()

    plt.axvline(x=0, color='#A9A9A9', zorder=0)
    plt.axhline(y=0, color='#A9A9A9', zorder=0)

    for i in range(len(vecs)):
        x = np.concatenate([[0, 0], vecs[i]])
        plt.quiver([x[0]],
                   [x[1]],
                   [x[2]],
                   [x[3]],
                   angles='xy', scale_units='xy', scale=1, color=cols[i],
                   alpha=alpha)

laranja = '#FF9A13'
azul = '#1190FF'

plotVectors([[2,3], [4,-1]],[laranja,azul])
plt.xlim(-6, 6)
plt.ylim(-6,6)

#testar no colab, para funcionar aqui são necessárias várias modificações