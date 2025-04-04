# Faça um programa que leia os dados de uma pessoa 
# (Nome, RG, CPF, ano de nascimento e armazene em um arquivo txt, calculando a idade da pessoa. 

import datetime

nome = input('Digite o nome: ')
rg = int(input('Digite o RG: '))
cpf = int(input("Digite o CPF: "))
ano_nasc = int(input("Digite o ano do nascimento: "))

ano_atual = datetime.date.today().year
idade = ano_atual - ano_nasc

with open('cadastro.txt', 'w', encoding='utf-8') as a:
    a.write(f'''Nome: [{nome}]; RG: [{rg}]; CPF: [{cpf}]; Idade: [{idade}]''')
    
with open('cadastro.txt', 'r', encoding='utf-8') as a:
    for linha in a:
        print(linha)
