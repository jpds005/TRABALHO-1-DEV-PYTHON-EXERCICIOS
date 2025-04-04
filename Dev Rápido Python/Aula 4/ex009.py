#É possível ler cada linha diretamente do arquivo sem readline() e/ou readlines(): 

f = open('arquivo_escrever.txt', 'r')

for linha in f:
    print(linha)

f.close()
