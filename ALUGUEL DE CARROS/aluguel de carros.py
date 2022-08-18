dias = int(input('Quantos dias você ficou como carro? '))
km = float(input('Quantos km foram rodados? '))
custo_por_dia = float(input('Qual o valor cobrado por dia? '))
custo_por_km = float(input('Qual o valor cobrado por km? '))
valor_por_dia = dias*custo_por_dia 
valor_por_km = km*custo_por_km 
total_a_pagar = valor_por_dia+valor_por_km
print('O total a pagar é {:.2f}'.format(total_a_pagar))
