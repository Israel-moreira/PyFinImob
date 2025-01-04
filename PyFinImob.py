# Mensagem de boas-vindas personalizada
print('✨ Bem-vindo ao Rael Bank! ✨')
print('Aqui, transformamos seus sonhos em realidade. Seja para comprar sua casa própria ou planejar um futuro seguro, estamos prontos para ajudar!')

# Solicita o nome do usuário
nome = input('\nAntes de começarmos, qual é o seu nome? ')

print(f'\nÉ um prazer tê-lo aqui, {nome}! Vamos juntos encontrar a melhor opção para o seu financiamento. 🚀')

# Solicita o valor da casa que o usuário deseja comprar
valor_casa = float(input('\nQual é o valor da casa que você deseja comprar? R$ '))

# Solicita o valor do salário do usuário
salario = float(input('Agora, por favor, informe o valor do seu salário: R$ '))

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
    print(f'\n🎉 Parabéns, {nome}! Seu empréstimo foi APROVADO!!! 🎉')
else:
    # Se não, informa ao usuário que a parcela excede o limite permitido
    print(f'\n⚠ Infelizmente, {nome}, o valor da parcela ultrapassa 30% do seu salário.')

    # Ajusta o número de anos para pagar até que a parcela esteja dentro do limite permitido
    while valor_parcelas > score30:
        anos_pagar += 1  # Aumenta o número de anos
        num_parcelas = anos_pagar * 12  # Recalcula o número de parcelas
        valor_parcelas = valor_casa / num_parcelas  # Recalcula o valor da parcela

    # Mensagem informando que o prazo foi aumentado e a parcela ficou mais acessível
    print(f'\n🔄 Para tornar o pagamento mais acessível, aumentamos o prazo para {anos_pagar} anos.')
    print('Isso reduz o valor da parcela, mas aumenta o valor total pago ao final.')

    # Pergunta se o cliente aceita a nova proposta
    resposta = input(f'Que tal par
