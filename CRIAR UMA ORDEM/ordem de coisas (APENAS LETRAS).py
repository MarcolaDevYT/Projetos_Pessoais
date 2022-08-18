import random
print('Escolha alguma coisa que queira fazer uma ordem. (Favor usar somente letras) ')
a = str(input('Primeiro nome: '))
b = str(input('Segundo nome: '))
c = str(input('Terceiro nome: ')) 
d = str(input('Quarto nome: '))
lista = [a, b, c, d]
random.shuffle(lista)
print('A ordem ficou: {}'.format(lista))
