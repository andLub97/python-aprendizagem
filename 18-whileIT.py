frase = 'o rato roeu a  roupa do rei de roma'

tamanho_frase = len(frase)
contador = 0
novaStr = ''

while contador < tamanho_frase:
    #print(frase[contador], contador)
    letra = frase[contador]
    novaStr += letra
    contador += 1

print(novaStr)

