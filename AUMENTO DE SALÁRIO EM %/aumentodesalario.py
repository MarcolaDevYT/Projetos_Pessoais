salário_inicial = float(input('Quanto é o seu salário atual? '))
porcentagem_de_aumento = float(input('Qual será o seu aumento em %? '))
aumento = salário_inicial*porcentagem_de_aumento/100
salário_final = salário_inicial+aumento
print('Seu aumento foi de {:.2f} reais\nE seu salário final ficou de {:.2f} reais'.format(aumento, salário_final))
