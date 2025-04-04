#Abrir um arquivo txt e escrever elementos de uma lista:

f = open('arquivo_escrever.txt', 'w+')

texto = ['palavra 1', 'palavra 2', 'palavra 3']

for linha in texto:
    f.write(linha)
    f.write('\n')
f.close()