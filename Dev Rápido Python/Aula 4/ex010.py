#Ler um arquivo com caracteres acentuados:

f = open('arquivo_portugues.txt', 'r', encoding='utf-8')

print(f.read())
f.close()
