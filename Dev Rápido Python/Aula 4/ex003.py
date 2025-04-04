#Criando e escrevendo um arquivo
with open('teste.txt', 'w') as f:
#with: Essa palavra-chave garante que o arquivo será automaticamente fechado ao final do bloco, mesmo se ocorrer um erro.
#as f: A variável f é um alias para o objeto do arquivo, permitindo que você interaja com ele dentro do bloco with.
#open('teste.txt', 'w'): Abre ou cria o arquivo chamado teste.txt no modo de escrita ('w').
    f.write('texto 1\n')
    f.write('texto 2')

#Lendo o arquivo
with open('teste.txt', 'r') as f:
    print(f.read())

with open('teste.txt', 'a') as f:
#Adicionar elementos no arquivo com o modo 'a'
    f.write('\ntexto 3')