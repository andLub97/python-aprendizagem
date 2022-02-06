import pandas as pd

# base = [1, 3, 5, 7, 9]
#
# data = pd.Series(base)
#
# print(data)

base = {'Nomes':['Ana', 'Carlos'],
       'Fones':[11111111111111, 222222222222]}
data = pd.DataFrame(base)

print(data)
