import numpy as np
import matplotlib.pyplot as plt
# v = np.array([1, 2, 3, 4])
# print(v)
'''cos x = vet1*vet2/mod vet1 * mod vet2'''

def ang(v,u):
    v_interno_u = v.dot(u)

    vn = np.linalg.norm(v)
    un = np.linalg.norm(u)

    r = v_interno_u/(vn*un)

    ang = np.arccos(r)

    return 180/np.pi*ang
u = np.array([0,1])
v = np.array([1,0])
print(ang(v,u))
