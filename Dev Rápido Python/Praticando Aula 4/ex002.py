f = open('vendas.txt', 'a')
f.write('teste de write')
f.close()

f = open('vendas.txt', 'r', encoding='utf-8')
print(f.read())
f.close()