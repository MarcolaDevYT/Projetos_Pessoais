import random
a = int(input('Qual número irá iniciar o sorteio? '))
b = int(input('Qual número ira encerar o sorteio? '))
c = random.randint(a, b)
print('O número sorteado foi {}'.format(c))
