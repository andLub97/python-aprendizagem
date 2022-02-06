from matplotlib import pyplot as plt
import seaborn as sns

y = [2,5,2,7,5,1]
x = ['n1','n2','n3','n4','n5','n6']

plt.bar(x, y, color = 'g')
plt.xlabel('var eixo x',size = 15)
plt.ylabel('var eixo y',size = 15)
plt.title('título aqui')

#plt.show()
#plt.barh(x,y)
#plt.show()

sns.barplot(x, y)
plt.show()