import random
print('Escolha os números inteiros que deseja para ser escolhido um deles aleatoriamente (SOMENTE NÚMEROS INTEIROS)')
a = int(input('Escolha um número: '))
b = int(input('Escolha um número: '))
c = int(input('Escolha um número: '))
d = int(input('Escolha um número: '))
e = [a, b, c, d]
escolha = random.choice(e)
print('O número sorteado foi {}'.format(escolha))
