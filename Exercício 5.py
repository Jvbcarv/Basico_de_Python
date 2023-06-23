#---------------utilizando For

nota = media = soma = 0
print(nota, media, soma)

for _ in range(1, 6):
  nota = float(input('Digite a nota '))
  soma += nota

print(soma)

media = soma / 5

print('A média é ', media)

#---------------utilizando While

nota = soma = 0
numero = 1
while numero <= 5:
  nota = float(input('Digite a nota:'))
  soma += nota
  numero += 1
print('A média é ', soma / 5)
