with open('teste2.txt', 'w') as a:
    a.write('04/04/2025')
    a.write('\n')
    a.write('03/04/2025')
    a.write('\n')
    a.write('02/04/2025')
    a.write('\n')

with open('teste2.txt', 'r') as a:
    print(a.read())