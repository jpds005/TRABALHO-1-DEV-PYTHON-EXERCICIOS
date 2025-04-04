#Ler todas as linhas de um arquivo com laço de repetição for:
f = open('arquivo_teste.txt', 'r')
for linha in f:
    print(linha)
f.close()
