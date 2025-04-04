#Ler todas as linhas de um arquivo com o for e separar as palavras de cada linha com o método split():
f = open('arquivo_teste.txt', 'r')
for linha in f:
    print(linha.split())
f.close()

#Resultado:
#['primeira', 'linha']
#['segunda', 'linha']
#['terceira', 'linha']
#['quarta', 'linha']
#['quinta', 'linha']
#['sexta', 'linha']
