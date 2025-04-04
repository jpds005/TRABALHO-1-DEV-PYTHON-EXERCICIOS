#Criando e escrevendo um arquivo
f = open('teste.txt', 'w') #Criando no modo de escrita
f.write('texto 1') #Write para escrever dentro do arquivo
f.close() #Fecha

#Lendo o arquivo
f = open('teste.txt', 'r')
print(f.read())
f.close()
