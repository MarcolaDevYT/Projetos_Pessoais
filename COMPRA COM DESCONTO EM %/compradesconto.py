valor_do_produto = float(input('Qual valor do produto? '))
desconto_em_porcentagem = float(input('Qual é o desconto em %? '))
desconto = valor_do_produto*desconto_em_porcentagem/100
valor_total = valor_do_produto-desconto
print('Você terá {} reais em desconto\nE o valor total do produto ficará {} reais'.format(desconto, valor_total))
