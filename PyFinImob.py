nome = input('Olá, seja bem-vindo ao Rael Bank!\nQual é o seu nome? ')

valor_casa = int(input('Qual é o valor da casa que você deseja comprar? R$ '))

salario = int(input('Agora, por favor, informe o valor do seu salário: R$ '))

anos_pagar = int(input('Ótimo! Em quantos anos você gostaria de parcelar o seu empréstimo? '))

num_parcelas = anos_pagar * 12

valor_parcelas = valor_casa / num_parcelas

score30 = salario * 0.30

if valor_parcelas <= score30:
    print(f'\nParabéns, {nome}! Seu empréstimo foi APROVADO!!!')
else:
    print(f'\nInfelizmente, {nome}, o valor da parcela ultrapassa 30% do seu salário.')

    while valor_parcelas > score30:
        anos_pagar += 1
        num_parcelas = anos_pagar * 12
        valor_parcelas = valor_casa / num_parcelas

    print(f'\nAo aumentar o prazo para {anos_pagar} anos, as parcelas ficaram mais acessíveis, mas o total pago ao final será maior.')

    resposta = input(f'Que tal parcelar em {anos_pagar} anos ({num_parcelas} parcelas de R$ {valor_parcelas:.2f})? Deseja continuar com essa proposta? (sim/não) ').strip().lower()

    if resposta == 'sim':
        print(f'\nResumo do seu empréstimo, {nome}:')
        print(f'Valor da casa: R$ {valor_casa}')
        print(f'Salário: R$ {salario}')
        print(f'Prazo para pagar: {anos_pagar} anos')
        print(f'Número de parcelas: {num_parcelas}')
        print(f'Valor da parcela: R$ {valor_parcelas:.2f}')
    else:
        print(f'\nTudo bem, {nome}. Caso mude de ideia, estaremos à disposição!')
