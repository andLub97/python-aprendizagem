from matplotlib import pyplot as plt

y = [2, 5, 2, 7, 5, 1]
x = ['N1', 'N2', 'N3', 'N4', 'N5', 'N6']

plt.pie(y, labels=x, radius = 1.5)
plt.show()
