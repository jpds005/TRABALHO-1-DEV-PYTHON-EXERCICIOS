# Elabore um programa em Python que insere a tabuada de multiplicação de 9 em um arquivo txt. 

with open('tabuada.txt', 'w', encoding='utf-8') as a:
    for c in range(1, 11):
        a.write(f'[9 x {c} = {9*c}]\n')

with open('tabuada.txt', 'r', encoding='utf-8') as a:
    for linha in a:
        print(linha)
