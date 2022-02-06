import numpy as np

u = [1, 2]
v = [5, 7]

u = np.array(u)
v = np.array(v)

print(u + v)
print(u * v) # produto elemento a elemento
# p escalar
print(u.dot(v))
#módulo
moduloDeU = np.linalg.norm(u)
print(moduloDeU)


