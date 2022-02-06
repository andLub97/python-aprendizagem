# lista = [1, 2, 3, 4]
# c = set(lista)
# print(type(c))
# c.add(33)
# print(c)
c1 = set([1, 2, 3])
c2 = set((1,2,100,4))
i = c1.intersection(c2)
u = c1.union(c2)

print(i)
print(u)

print(8 in c1)

