# Elabore um programa em Python que leia o nome e duas notas de um aluno do teclado, 
# calcule a média e armazene em um arquivo txt o nome, a média final e se o mesmo foi 
# Aprovado (média >=6) ou Reprovado (média < 6). 

nome = input('Digite o nome do aluno(a): ')
n1 = int(input('Digite a primeira nota do aluno(a): '))
n2 = int(input('Digite a segunda nota do aluno(a): '))
media = (n1+n2) / 2
if media >= 6:
    status = 'APROVADO'
else:
    status = 'REPROVADO'

with open('aluno.txt', 'w', encoding='utf-8') as a:
    a.write(f'NOME: [{nome}]; MÉDIA: [{media}]; STATUS: [{status}]')

with open('aluno.txt', 'r', encoding='utf-8') as a:
    print(a.read())
