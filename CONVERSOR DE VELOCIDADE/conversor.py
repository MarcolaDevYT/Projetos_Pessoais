import math


while 1:
    medida = int(input('Você vai converter o que?\nEscolha uma opção [1] Quilometros para Milhas, [2] Milhas para Quilometros '))
    if medida == 1:
        velocidade = float(input('Qual a velocidade em KM/H que você quer fazer a conversão? '))
        conversão = velocidade/1.62
        print(f'A velocidade é aproximadamente {math. ceil(conversão)} M/H')
        escolha = int(input('Escolha uma opção: [1] Retornar ao menu, [2] Sair do programa '))
        if escolha == 1:
            i = 1
        else:
            i = 0

    elif medida == 2:
        velocidade = float(input('Qual a velocidade em M/H que você quer fazer a conversão? '))
        conversão = velocidade*1.62
        print(f'A velocidade é aproximadamente {math. ceil(conversão)} KM/H')
        escolha = int(input('Escolha uma opção: [1] Retornar ao menu, [2] Sair do programa '))
        if escolha == 1:
            i = 1
        else:
            i = 0        
