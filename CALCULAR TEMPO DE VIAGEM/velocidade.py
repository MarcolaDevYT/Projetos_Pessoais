while 1: #v=d/t #d=v*t #t=d/v

    pergunta = int(input('Escolha uma opção: [1] Calcular velocidade média da viagem\n\
        [2] Calcular distância da aproxiamda da viagem\n\
        [3] Calcular tempo médio da viagem\n\
        O que você vai escolher? '))

    if pergunta == 1:
        distância = float(input('Qual a distância percorrida? '))
        tempo = float(input('Quantas horas gastou para chegar ao destino? '))
        velocidade = distância/tempo
        print(f'A velocidade média nessa viagem foi de {velocidade} km/h')
        print('Escolha uma opção: [1] Voltar ao menu, [2] Sair do programa')
        escolha = int(input('Qual a opção escolhida? '))
        if escolha == 1: 
            i = 1
        else: 
            i = 0

    if pergunta == 2:
        velocidade = int(input('Qual a velocidade média obtida no veiculo? '))
        tempo = float(input('Quantas horas gastou para chegar ao destino? '))
        distância = velocidade*tempo
        print(f'A distância aproximada dessa viagem foi de {distância} km')
        print('Escolha uma opção: [1] Voltar ao menu, [2] Sair do programa')
        escolha = int(input('Qual a opção escolhida? '))
        if escolha == 1: 
            i = 1
        else: 
            i = 0

    if pergunta == 3:
        distância = float(input('Qual a distância percorrida? '))
        velocidade = int(input('Qual a velocidade média obtida no veiculo? '))
        tempo = distância/velocidade
        print(f'O tempo gasto nessa viagem foi de aproximadamente {tempo} horas')
        print('Escolha uma opção: [1] Voltar ao menu, [2] Sair do programa')
        escolha = int(input('Qual a opção escolhida? '))
        if escolha == 1: 
            i = 1
        else: 
            i = 0
            