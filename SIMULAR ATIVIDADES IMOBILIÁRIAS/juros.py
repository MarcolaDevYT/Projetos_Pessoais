#montante=capital_aplicado*(1+taxa_de_juros_compostos)tempo_de_aplicação

escolha = int(input('O que você vai querer simular? [1] Financiamento [2] Investimento [3] Empréstimo '))

if escolha == 1:
    valor_financiado = float(input('Qual o valor total do imóvel? '))
    entrada = float(input('Qual o valor da sua entrada? '))
    taxa_de_juros = float(input('Qual a porcentagem mensal em números decimais? '))
    tempo_de_aplicação = int(input('Quantos parcelas você vai pagar ? '))
    fatura = 12*tempo_de_aplicação
    valor_total = valor_financiado-entrada
    total_a_pagar = valor_total*(1+taxa_de_juros/100)**tempo_de_aplicação
    parcelas = total_a_pagar/tempo_de_aplicação
    print(f'Você vai pagar {total_a_pagar:.2f} em {tempo_de_aplicação} parcelas\nAs parcelas vão ter um valor mensal de aproximadamente R$ {parcelas:.2f}')

if escolha == 2:
    #montante=capital_investido*(1+taxa_de_juros_compostos)tempo_de_aplicação
    capital_investido = float(input('Quanto foi o seu investimento? '))
    taxa_de_juros = float(input('Qual a porcentagem mensal em números decimais? '))
    tempo_de_aplicação = int(input('Quantos meses o dinheiro vai render? '))
    taxa_total = 1+taxa_de_juros
    potencia = taxa_total**tempo_de_aplicação
    rentabilidade = capital_investido*potencia
    rendimento = rentabilidade-capital_investido
    print(f'Seu investimento de R$ {capital_investido:.2f} rendeu R$ {rendimento:.2f} ficando no total R$ {rentabilidade:.2f}')

if escolha == 3:
    valor_pego = float(input('Quanto você pegou emprestado? '))
    taxa_de_juros = float(input('Qual a porcentagem de juros ao mês em números decimais ? '))
    tempo_de_aplicação = float(input('Quantas parcelas você vai pagar? '))
    empréstimo = (1+taxa_de_juros)**tempo_de_aplicação*taxa_de_juros
    divisão = (1+taxa_de_juros)**tempo_de_aplicação-1
    pestação = valor_pego*(empréstimo/divisão)
    total = pestação*tempo_de_aplicação
    print(f'Você vai pagar um total de R$ {total:.2f} ')
