#Tuplas:

tupla = ('Homo sapiens', 'Canis familiaris', 'Felis catus')
print(tupla)
print(tupla[0])
print(tupla.index('Canis familiaris'))

for elemento in tupla:
  print(elemento)


#Listas:
l1 = ['Homo sapiens', 'Canis familiaris', 'Felis catus']
l2 = ['Xenopus laevis', 'Ailuropoda melanoleuca']

l3 = l1 + l2
print(l3)

print(l2)

l2_2 = l2 * 2
print(l2_2)

print(l1[0])

print(l1)

print(l1[0:2])

l1.append('Gorila gorila')
print(l1)

l1.remove('Felis catus')
print(l1)

del(l1)

for item in l2_2:
  print(item)


#Dicionários:
coleta = {'Aedes aegypt': 32, 'Aedes albopictus': 22, 'Anopheles darlingi': 14}
print(coleta['Aedes aegypt'])

coleta['Rhodnius montenegrensis'] = 11
print(coleta)

del(coleta)['Aedes albopictus']
print(coleta)

coleta.items()

coleta.keys()

coleta.values()

coleta2 = {'Anopheles gambiae': 13, 'Anopheles deaneorum': 14}
print(coleta2)

coleta.update(coleta2)
print(coleta)

coleta.items()

for especie, num_especimes in coleta.items():
  print(f'Espécie: {especie}, número de espécimes coletados: {num_especimes}')


#Conjuntos:

biomeleculas = ('proteína', 'ácidos nucleicos', 'carboidrato', 'lipídeo',
                'ácidos nucleicos', 'carboidrato', 'carboidrato', 'carboidrato')
print(biomeleculas)
print(set(biomeleculas))

c1 = {1,2,3,4,5}
c2 = {3,4,5,6,7}
c3 = c1.intersection(c2)
print(c3)
print(c1.difference(c2))
print(c2.difference(c1))
