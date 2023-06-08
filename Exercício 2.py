#Exercício 2)

tempo = float(input('insira o tempo gasto na viagem: '))
velocidade = float(input('insira a velocidade média da viagem: '))

distancia = tempo * velocidade
litros_usados = distancia/12

print('Velocidade média: ', velocidade)
print('Tempo gasto na viagem: ', tempo)
print('Distância percorrida:', distancia)
print('Quantidade de litros:', round(litros_usados,1))