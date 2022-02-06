string = "O brasil é uma merda"
lista = string.split(' ')
# onde houver espaço, haverá divisão
#print(lista)
#for qtd in lista:
#    print(f"{qtd} apareceu {lista.count(qtd)} vezes")

#string2 = ' '.join(lista)
#print(string2)

for indice, valor in enumerate(lista):
    print(indice, valor)
