#Estrutura de repetição - for:

#sem o for terá que digitar print várias vezes:
print(1)
print(2)
print(3)
print(4)
print(5)

#com for você simplifica o código:
for numero in range(1, 6):
  print(numero)

#for colocando os números em ordem decrescente:
for numero in range(5, 0, -1):
  print(numero)

#somatório de valores com for:
5 + 4 + 3 + 2 + 1

soma = 0
for numero in range(1, 6):
  soma = soma + numero
print(soma)

#para percorrer strings:
palavra = 'sorvete'
for letra in palavra:
  if letra == 'v':
    print('Achou a letra v')

#for aninhado:
for i in range(0,5):
  print(i)
  print('---')
  for j in range(0,3):
    print(j)
  print()

#----------------------------------------
#Estrutura de repetição - While:

numero = 1
while numero < 6:
  print(numero)
  numero += 1
print('---')

#while colocando os números em ordem decrescente:
numero = 5
while numero > 0:
  print(numero)
  numero -= 1

#somatório com while:
1 + 2 + 3 + 4 + 5

soma = 0
numero = 1
while numero < 6:
  soma += numero
  numero += 1
print(soma)

#while com input
numero = 12
while numero < 1 or numero > 10:
  numero = int(input('Digite um número de 1 a 10: '))
