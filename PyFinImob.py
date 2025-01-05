# Mensagem de boas-vindas personalizada
print('✨ Bem-vindo ao Rael Bank! ✨')
print('Aqui, transformamos seus sonhos em realidade. Seja para conquistar a casa dos seus sonhos ou planejar um futuro financeiro seguro, estamos aqui para ajudar você em cada passo dessa jornada!')

# Solicita o nome do usuário
nome = input('\nAntes de começarmos, qual é o seu nome? ')

print(f'\nÉ um prazer imenso ter você conosco, {nome}! Vamos trabalhar juntos para encontrar a melhor solução para o seu financiamento. 🚀')

# Solicita o valor da casa que o usuário deseja comprar
valor_casa = float(input('\nQual é o valor da casa que você deseja adquirir? R$ '))

# Solicita o valor do salário do usuário
salario = float(input('Agora, para que possamos calcular o melhor financiamento, por favor, informe o valor do seu salário: R$ '))

# Solicita o número de anos que o usuário deseja para pagar o empréstimo
anos_pagar = int(input('Perfeito! Em quantos anos você gostaria de parcelar o seu empréstimo? '))

# Calcula o número de parcelas (meses) com base nos anos fornecidos
num_parcelas = anos_pagar * 12

# Calcula o valor de cada parcela do empréstimo
valor_parcelas = valor_casa / num_parcelas

# Calcula 30% do salário do usuário, que será o valor máximo permitido para a parcela
score30 = salario * 0.30

# Verifica se o valor da parcela é menor ou igual a 30% do salário
if valor_parcelas <= score30:
    # Se sim, aprova o empréstimo
    print(f'\n🎉 Parabéns, {nome}! Seu empréstimo foi APROVADO com sucesso!!! 🎉')
else:
    # Se não, informa ao usuário que a parcela excede o limite permitido
    print(f'\n⚠ Infelizmente, {nome}, o valor da parcela ultrapassa 30% do seu salário. Mas não se preocupe, temos uma solução!')

    # Ajusta o número de anos para pagar até que a parcela esteja dentro do limite permitido
    while valor_parcelas > score30:
        anos_pagar += 1  # Aumenta o número de anos
        num_parcelas = anos_pagar * 12  # Recalcula o número de parcelas
        valor_parcelas = valor_casa / num_parcelas  # Recalcula o valor da parcela

    # Mensagem informando que o prazo foi aumentado e a parcela ficou mais acessível
    print(f'\n🔄 Para tornar o pagamento mais acessível, ajustamos o prazo para {anos_pagar} anos.')
    print('Essa alteração reduz o valor da parcela mensal, mas o valor total pago ao final do financiamento será maior.')

    # Pergunta se o cliente aceita a nova proposta
    resposta = input(f'Gostaria de seguir com essa nova proposta? (sim/não): ').strip().lower()
    if resposta == 'sim':
        print(f'\nExcelente, {nome}! Vamos seguir com essa opção e transformar seu sonho em realidade.')
    else:
        print(f'\nSem problemas, {nome}. Estamos aqui para ajudar a encontrar a melhor solução para você!')  
