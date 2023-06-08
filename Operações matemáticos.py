a = 5
b = 3
print(a, b)

#soma:
print('A soma é', a + b)
#subtração:
print('A subtração é', a - b)
#divisão:
print('A divisão é', a / b)
#multiplicação:
print('A multiplicação é', a * b)

#divisão:
print('O resto da divisão é', 10 % 3)

#exponenciação:  #exemplo: 5*5*5*5
print('5 elevado a 4 é', 5**4)

#Arredondamentos:
casos_doenca = 134
numero_habitantes = 34432
casos_por_habitante = casos_doenca / numero_habitantes
print(casos_por_habitante)
#para arrendondar o resultado do código acima:
print('O número de casos por habitante é de', round(casos_por_habitante, 4)) #4 é a quantidade de números que quero que apareça no resultado

#raiz quadrada:
#importação da biblioteca 'math' para usar a função de raiz quadrada 'sqrt'
import math
print(math.sqrt(81))
#outro exemplo:
n = int(input('Digite um número: '))
r = math.sqrt(n)
print('A raiz de {} é {}'.format(n, math.ceil(r)))