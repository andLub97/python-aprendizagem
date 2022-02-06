var = ['André', 'João', 'Maria']
for valor in var:
    if valor.lower().startswith('j'):
        break
else:
    print('Não existe palavra que começa com J')
