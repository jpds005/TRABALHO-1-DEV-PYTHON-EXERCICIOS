with open('vendas.txt', 'a') as a:
    a.write('\ntexto 1')
    a.write('\ntexto 2')

with open('vendas.txt', 'r') as a:
    print(a.read())
