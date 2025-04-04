#Ler todas as linhas de um arquivo em uma list com o readlines().
f = open('arquivo_teste.txt', 'r')
print(f.readlines())
f.close()

#RESULTADO::
#['primeira linha\n', 'segunda linha\n', 'terceira linha\n', 'quarta linha\n', 'quinta linha\n', 'sexta linha']
