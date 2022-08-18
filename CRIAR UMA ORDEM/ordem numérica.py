import random
print('Escolha os números que você quer ter uma ordem aleatória ')
a = float(input('Escolha um número: '))
b = float(input('Escolha um número: '))
c = float(input('Escolha um número: '))
d = float(input('Escolha um número: '))
lista = [a, b, c, d]
random.shuffle(lista)
print('A ordem ficou {}'.format(lista))
