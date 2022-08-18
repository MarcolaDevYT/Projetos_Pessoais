while 1:
 print('-'*12)
 preço = float(input('Qual o preço do produto que você quer comprar? '))
 dinheiro = float(input('Quanto você tem para pagar o produto? '))
 falta = preço-dinheiro
 print('Está faltando {} reais'.format(falta))

 print('Você gostaria de parcelar esse produto? ')
 print('-'*12)
 parcelar = int(input('Escolha uma opção: [1] Sim, [2] Não: '))

 if parcelar == 1:
    nparcelas = int(input('Em quantas parcelas gostaria de pagar? '))
    print('Possui juros?\nEscolha uma opção: [1] Sim, [2] Não: ')
    juros = int(input('Qual a opção escolhida? '))
    if juros == 1:
        print('-'*12)
        porcentagem = int(input('Qual a porcentagem de juros? '))
        juros_a_pagar = falta*porcentagem/100
        fatura = (falta+juros_a_pagar)/nparcelas
        print(f'Você vai pagar R${juros_a_pagar} de juros, Sua fatura vai ser R${fatura} por {nparcelas} meses')
        print('Escolha uma opção: [1] Voltar ao menu, [2] Sair do programa')
        escolha = int(input('Qual a opção escolhida? '))
        if escolha == 1: 
            i = 1
        else: 
            i = 0

    if juros == 2: 
        valor_da_parcela = falta/nparcelas
        print(f'A sua fatura vai ficar R${valor_da_parcela:.2f} por {nparcelas} meses')
        print('Escolha uma opção: [1] Voltar ao menu, [2] Sair do programa')
        escolha = int(input('Qual a opção escolhida? '))
        if escolha == 1: 
            i = 1
        else: 
            i = 0

 if parcelar == 2:
    print('Agora que você já sabe quanto falta para conseguir o produto desejado só economizar! ')       
    print('Escolha uma opção: [1] Voltar ao menu, [2] Sair do programa')
    escolha = int(input('Qual a opção escolhida? '))
    if escolha == 1: 
        i = 1
    else: 
        i = 0
