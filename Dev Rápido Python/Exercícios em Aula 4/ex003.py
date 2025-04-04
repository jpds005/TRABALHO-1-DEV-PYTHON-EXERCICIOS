#Faça um programa que leia um arquivo txt e insere cada linha em uma lista.

lista = []

with open('vendas.txt', 'r', encoding='utf-8') as a:
    for linha in a:
        lista.append(linha.split())

print(lista)
