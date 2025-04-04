texto = ['palavra 1', 'palavra 2', 'palavra 3']

with open('vendas.txt', 'a') as a:
    for linha in texto:
        a.write(linha)
        a.write('\n')

with open('vendas.txt', 'r') as a:
    for linhas in a:
        print(linhas.split())