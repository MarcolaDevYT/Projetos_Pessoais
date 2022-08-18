import random
print('Digite abaixo o nome das pessoas que irão participar do sorteio')
a = str(input('Nome da primeira pessoa: '))
b = str(input('Nome da segunda pessoa: '))
c = str(input('Nome da terceira pessoa: '))
d = str(input('Nome da quarta pessoa: '))
lista = [a, b, c, d]
escolha = random.choice(lista)
print('A pessoa escolhida foi {}'.format(escolha))
