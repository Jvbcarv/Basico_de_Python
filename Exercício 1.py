#Exercício 1)

a = 10
b = 20

print('a soma de a e b é:', a + b)
print('a subtração de a e b é:', a - b)
print('a multiplicação de a e b é:', a * b)
print('a divisão de a e b é:', a / b)

#outra forma de fazer o exercício 1:

numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))
print(numero1, numero2)

adicao = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2

print('Adição: ', adicao)
print('Subtração: ', subtracao)
print('Multiplicação: ', multiplicacao)
print('Divisão: ', round(divisao, 2))