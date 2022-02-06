'''
Entrada: int
verificar se é int
informar se é par
'''
#
# num = (input("Digite um número: "))
#
# try:
#     num = int(num)
#     if num % 2 == 0:
#         print('Você digitou um número par')
#     elif num % 2 != 0:
#         print("Valor ímpar")
# except:
#     print("Erro! Valor digitado não é inteiro")
#
# '''
# Perguntar a hora ao usuário e responder com boa tarde, noite ou dia
# '''
# hora = int(input('Que horas são? '))
#
# if hora >= 0 and hora <= 11:
#     print('bom dia')
# elif hora <18:
#     print('boa tarde')
# else:
#     print('boa noite')

'''
perguntar o nome
4 letras ou menos -> curto
5-6 -> normal
>6 muito grande
'''

nome = input('Nome: ')
tam = len(nome)

if tam <= 4:
    print("curto")
elif tam <=6:
    print('normal')
else:
    print("grande")
