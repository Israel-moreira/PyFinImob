# Mensagem de boas-vindas personalizada
print('✨ Bem-vindo ao Rael Bank! ✨')
print('Aqui, estamos prontos para ajudar você a transformar seus sonhos em realidade. Seja para adquirir o seu lar ou para planejar um futuro financeiro mais tranquilo, nosso objetivo é fazer isso de forma simples e sem complicações.')

# Solicita o nome do usuário
nome = input('\nAntes de seguirmos, qual é o seu nome? ')

print(f'\nÉ um prazer imenso ter você conosco, {nome}! Vamos embarcar juntos nessa jornada para encontrar a melhor solução para o seu financiamento. 🚀')

# Solicita o valor da casa que o usuário deseja comprar
valor_casa = float(input('\nAgora, me conte, qual o valor da casa que você deseja comprar? R$ '))

# Solicita o valor do salário do usuário
salario = float(input('Perfeito! Agora, qual o valor do seu salário mensal? R$ '))

# Solicita o número de anos que o usuário deseja para pagar o empréstimo
anos_pagar = int(input('E em quantos anos você gostaria de parcelar o seu empréstimo? '))

# Calcula o número de parcelas (meses) com base nos anos fornecidos
num_parcelas = anos_pagar * 12

# Calcula o valor de cada parcela do empréstimo
valor_parcelas = valor_casa / num_parcelas

# Calcula 30% do salário do usuário, que será o valor máximo permitido para a parcela
score30 = salario * 0.30

# Verifica se o valor da parcela é menor ou igual a 30% do salário
if valor_parcelas <= score30:
    # Se sim, aprova o empréstimo
    print(f'\n🎉 Uau, {nome}! Seu empréstimo foi APROVADO com sucesso!!! 🎉 Agora você está mais perto de conquistar o seu novo lar!')

else:
    # Se não, informa ao usuário que a parcela excede o limite permitido
    print(f'\n⚠ Opa, {nome}, a parcela ficou um pouco acima de 30% do seu salário. Mas não se preocupe, isso não é um obstáculo, é só um pequeno ajuste!')

    # Ajusta o número de anos para pagar até que a parcela esteja dentro do limite permitido
    while valor_parcelas > score30:
        anos_pagar += 1  # Aumenta o número de anos
        num_parcelas = anos_pagar * 12  # Recalcula o número de parcelas
        valor_parcelas = valor_casa / num_parcelas  # Recalcula o valor da parcela

    # Mensagem informando que o prazo foi aumentado e a parcela ficou mais acessível
    print(f'\n🔄 Para facilitar, aumentamos o prazo para {anos_pagar} anos. Isso vai diminuir o valor da sua parcela mensal, mas o valor total pago ao final será um pouquinho maior. A boa notícia é que você vai ter mais tempo para respirar financeiramente.')

    # Pergunta se o cliente aceita a nova proposta
    resposta = input(f'O que você acha dessa nova proposta? Vamos em frente? (sim/não): ').strip().lower()
    if resposta == 'sim':
        print(f'\nPerfeito, {nome}! Estamos animados para dar o próximo passo com você e fazer seu sonho virar realidade.')
    else:
        print(f'\nSem problema, {nome}! Estamos aqui para ajustar e encontrar a melhor opção para o seu bolso e seus sonhos.')
