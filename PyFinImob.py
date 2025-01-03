# Solicita o nome do usuário
nome = input('Olá, seja bem-vindo ao Rael Bank!\nQual é o seu nome? ')

# Solicita o valor da casa que o usuário deseja comprar
valor_casa = int(input('Qual é o valor da casa que você deseja comprar? R$ '))

# Solicita o valor do salário do usuário
salario = int(input('Agora, por favor, informe o valor do seu salário: R$ '))

# Solicita o número de anos que o usuário deseja para pagar o empréstimo
anos_pagar = int(input('Ótimo! Em quantos anos você gostaria de parcelar o seu empréstimo? '))

# Calcula o número de parcelas (meses) com base nos anos fornecidos
num_parcelas = anos_pagar * 12

# Calcula o valor de cada parcela do empréstimo
valor_parcelas = valor_casa / num_parcelas

# Calcula 30% do salário do usuário, que será o valor máximo permitido para a parcela
score30 = salario * 0.30

# Verifica se o valor da parcela é menor ou igual a 30% do salário
if valor_parcelas <= score30:
    # Se sim, aprova o empréstimo
    print(f'\nParabéns, {nome}! Seu empréstimo foi APROVADO!!!')
else:
    # Se não, informa ao usuário que a parcela excede o limite permitido
    print(f'\nInfelizmente, {nome}, o valor da parcela ultrapassa 30% do seu salário.')

    # Ajusta o número de anos para pagar até que a parcela esteja dentro do limite permitido
    while valor_parcelas > score30:
        anos_pagar += 1  # Aumenta o número de anos
        num_parcelas = anos_pagar * 12  # Recalcula o número de parcelas
        valor_parcelas = valor_casa / num_parcelas  # Recalcula o valor da parcela

    # Mensagem informando que o prazo foi aumentado e a parcela ficou mais acessível
    print(f'\nAo aumentar o prazo para {anos_pagar} anos, as parcelas ficaram mais acessíveis, mas o total pago ao final será maior.')

    # Pergunta se o cliente aceita a nova proposta
    resposta = input(f'Que tal parcelar em {anos_pagar} anos ({num_parcelas} parcelas de R$ {valor_parcelas:.2f})? Deseja continuar com essa proposta? (sim/não) ').strip().lower()

    if resposta == 'sim':
        # Exibe o resumo do empréstimo se o cliente aceitar
        print(f'\nResumo do seu empréstimo, {nome}:')
        print(f'Valor da casa: R$ {valor_casa}')
        print(f'Salário: R$ {salario}')
        print(f'Prazo para pagar: {anos_pagar} anos')
        print(f'Número de parcelas: {num_parcelas}')
        print(f'Valor da parcela: R$ {valor_parcelas:.2f}')
    else:
        # Informa que o cliente recusou a proposta
        print(f'\nTudo bem, {nome}. Caso mude de ideia, estaremos à disposição!')
