from math import sqrt
cateto_oposto = float(input('Qual o comprimento do cateto oposto? '))
cateto_adjacente = float(input('Qual o comprimento do cateto adjacente? '))
hipotenusa = cateto_oposto**2+cateto_adjacente**2
print('A hipotenusa desse triângulo mede {:.2f}'.format(sqrt(hipotenusa)))
