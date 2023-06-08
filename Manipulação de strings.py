#Manipulação de strings

a = 'casaco'
print(a)

#Maiúscula, minúscula, e somente primeira letra em maiúscula:

#O método upper copia uma string com todas as letras minúsculas convertidas em letras maiúsculas.
maiuscula = a.upper()
print(maiuscula)

#o método lower copia uma string convertendo todas as letras maiúsculas em letras minúsculas.
minuscula = maiuscula.lower()
print(minuscula)

#o método capitalize copia uma string com a primeira palavra iniciando em maiúscula, e as demais em letras minúsculas.
capital = a.capitalize()
print(capital)

#Buscando apenas uma parte da palavra:

#é preciso inserir o indíce da quantidade de letras desejadas dentro do [ : ]
metade_palavra = a[0:4]
print(metade_palavra)

#para buscar da 3ª letra adiante:
ultimas_letras = a[3:]
print(ultimas_letras)

#Substituição de trechos de uma palavra:

#o método replace é usado para substituir trechos de uma string
#exemplo:
b = a.replace('aco', 'inha') #o replace trocará a parte 'aco' da palavra 'casaco' por 'inha'
print(a)
print(b)
#outro exemplo:
c = a.replace('o', 'a') ##o replace trocará a letra 'o' da palavra casaco por 'a'
print(c)


#Dividindo duas variáveis:

n1 = 14
n2 = 16
print(f'Dividindo {n1} por {n2} o resultado é {n1/n2}') #o 'f' é usado para acessar o valor das variáveis