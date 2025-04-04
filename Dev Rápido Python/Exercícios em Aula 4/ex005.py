# Faça um algoritmo em Python que leia dois números inteiros do teclado, faça uma mini calculadora 
# (soma, subtração, multiplicação e divisão) e armazene todos os resultados em um arquivo txt.

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

with open('calculos.txt', 'w', encoding='utf-8') as a:
    a.write(f'SOMA: [{n1+n2}]; SUBTRAÇÃO: [{n1-n2}]; MULTIPLICAÇÃO: [{n1*n2}]; DIVISÃO: [{n1/n2}]')

with open('calculos.txt', 'r', encoding='utf-8') as a:
    print(a.read())
