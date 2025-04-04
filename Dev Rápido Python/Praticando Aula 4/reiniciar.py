#Código para reiniciar o txt vendas

#Lê todas as linhas
with open('vendas.txt', 'r') as a:
    linhas = a.readlines()

#Guarda as linhas numa variável
linhas = linhas[:8]

#Escreve as linhas no arquivo
with open('vendas.txt', 'w') as a:
    a.writelines(linhas)

#Lê o arquivo
with open('vendas.txt', 'r') as a:
    print(a.read())
