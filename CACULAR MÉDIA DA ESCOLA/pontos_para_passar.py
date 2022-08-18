print('ATENÇÃO: COLOQUE SUAS NOTAS NORMALMENTE E AS QUE AINDA NÃO SABE OU NÃO TEM COLOQUE O VALOR 0')
n1 = float(input('Coloque a sua nota do primeiro bimestre: '))
n2 = float(input('Coloque sua nota do segundo bimestre: '))
n3 = float(input('Coloque sua nota do terceiro bimestre: '))
n4 = float(input('Coloque sua nota do quarto bimestre: '))
soma_das_notas = n1+n2+n3+n4
falta_passar = 24 - soma_das_notas
print(f'Para você passar falta {falta_passar} pontos')
