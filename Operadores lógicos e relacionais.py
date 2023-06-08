#operadores lógicos:
a = True
b = False
print(a, b)

#duas maneiras de usar o operador and: and e &
#O teste vai retornar TRUE somente se as DUAS condições forem TRUE.
#Se uma delas for falsa, o retorno é falso.
print(a and b)
print(a & b)
#outro exemplo:
c = a and b
print("'A' e 'B' são iguais é", c)

#duas maneiras de usar o operador 'or':
#Basta que uma dessas condições seja verdadeira, para o teste condicional ser verdadeiro.
print(a or b)
print(a | b)
#outro exemplo:
d = a or b
print("'A' ou 'B' é igual a", d)

#operador 'not' retorna o valor contrário:
#ele reverte a expressão.
print(not a)
print(not b)

#Operadores relacionais:
print(5 > 3)
print(5 < 3)
print(5 >= 5)
print(5 <= 3)
print(5 == 3) # == significa 'igual a'
print(5 != 3) # != significa 'diferente de'

