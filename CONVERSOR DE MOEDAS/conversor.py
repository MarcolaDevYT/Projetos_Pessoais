while 1:

    print('-'*12)
    print('Escolha uma moeda para comerçar a converção. [1] Dólar para Real,\n[2] Real para Dólar, [3] Euro para Real, [4] Real para Euro ')
    pergunta = int(input('Escolha uma opção: '))
    print('-'*12)

    if pergunta == 1:
        print('Conversor de Dólar para Real')
        cotação = float(input('Qual o valor do Real ? '))
        dinheiro = float(input('Quantos Dólares você quer converter ? '))
        conversão = dinheiro/cotação
        print('-'*12)
        print(f'Com ${dinheiro:.2f} dólares você consegue R${conversão:.2f} reais')
        print('-'*12)
        print('O que você deseja fazer? [1] retornar ao menu, [0] sair do programa')
        escolha = int(input('O que deseja fazer? '))
        if escolha == 1:
            i = 1
        else: 
            i = 0
           
    if pergunta == 2:
        print('Conversor de Real para Dólar')
        cotação = float(input('Qual o valor do Dólar ? '))
        dinheiro = float(input('Quantos Reais você quer converter ? '))
        conversão = dinheiro/cotação
        print('-'*12)
        print(f'Com R${dinheiro:.2f} reais você consegue ${conversão:.2f} dólares')
        print('-'*12)
        print('O que você deseja fazer? [1] retornar ao menu, [0] sair do programa')
        escolha = int(input('O que deseja fazer? '))
        if escolha == 1:
            i = 1
        else: 
            i = 0     

    if pergunta == 3:
        print('Conversor de Euro para Real')
        cotação = float(input('Qual o valor do Real ? '))
        dinheiro = float(input('Quantos Euros você quer converter ? '))
        conversão = dinheiro/cotação
        print('-'*12)
        print(f'Com €{dinheiro:.2f} euros você consegue R${conversão:.2f} reais')
        print('-'*12)
        print('O que você deseja fazer? [1] retornar ao menu, [0] sair do programa')
        escolha = int(input('O que deseja fazer? '))
        if escolha == 1:
            i = 1
        else: 
            i = 0

    if pergunta == 4:
        print('Conversor de Real para Euro')
        cotação = float(input('Qual o valor do Euro ? '))
        dinheiro = float(input('Quantos Reais você quer converter ? '))
        conversão = dinheiro/cotação
        print('-'*12)
        print(f'Com R${dinheiro:.2f} reais você consegue €{conversão:.2f} euros')
        print('-'*12)
        print('O que você deseja fazer? [1] retornar ao menu, [0] sair do programa')
        escolha = int(input('O que deseja fazer? '))
        if escolha == 1:
            i = 1
        else: 
            i = 0     
            