#Ler a linha de um arquivo com o readline().
f = open('arquivo_teste', 'r')
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
f.close()

f = open('arquivo_teste', 'r')
print(f.readline(5))
#Se for passado algum parâmetro inteiro dentro do readline(),
#será lido uma quantidade n de caracteres da linha lida.
f.close()