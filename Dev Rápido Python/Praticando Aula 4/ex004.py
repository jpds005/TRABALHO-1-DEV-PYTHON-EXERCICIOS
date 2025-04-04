with open('vendas.txt', 'r', encoding='utf-8') as a:
    print(a.readline())
    print(a.readline())
    print(a.readline())
    print(a.readline())
    print(a.readline())
    print(a.readline())

with open('vendas.txt', 'r', encoding='utf-8') as a:
    print(a.readline(5))
