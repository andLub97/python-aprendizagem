num1 = 10
num2 = 3
div = num1/num2
x = 123
y = 12345
print(f'{div:.2f}')
print(f'{x:0>10}')
print(f'{y:0<10}')
print(f'{y:0^10}')
print(f'{y:#^10}')
print('{:@>30}'.format(x))
nome = 'andré'
print(f'{nome:s}')
nome = nome.ljust(20, '&')
print(nome)
