# Solicita o nome do usuário
nome = input('Olá! seja bem-vindo ao Rael Bank.\nPor gentileza, me informe seu nome: ')

# Solicita o valor da casa que o usuário pretende comprar
valor_casa = int(input('Qual o valor da casa que você pretende comprar? '))

# Solicita o valor do salário do usuário
salario = int(input('Por gentileza, digite o valor do seu salário: '))

# Solicita o número de anos que o usuário deseja para pagar o empréstimo
anos_pagar = int(input('Está quase tudo pronto!\nMe informe a quantidade de anos que você quer parcelar seu empréstimo: '))

# Calcula o número de parcelas (meses) com base nos anos fornecidos
num_parcelas = anos_pagar * 12

# Calcula o valor de cada parcela do empréstimo
valor_parcela = valor_casa / num_parcelas

# Calcula 30% do salário do usuário, que será o valor máximo permitido para a parcela
score30 = salario * 0.30

# Verifica se o valor da parcela é menor ou igual a 30% do salário
if valor_parcela <= score30:
    # Se sim, aprova o empréstimo
    print(f'Tenho uma ótima notícia para você, {nome}!\nSeu empréstimo foi APROVADO!!!')
else:
    # Se não, informa ao usuário que a parcela excede o limite permitido
    print(f'Poxa, {nome}, infelizmente o valor da parcela excede os limites do seu salário.')
    
    # Continua ajustando o número de anos para pagar até que a parcela esteja dentro do limite permitido
    while valor_parcela > score30:
        # Aumenta o número de anos para pagar
        anos_pagar += 1
        # Recalcula o número de parcelas
        num_parcelas = anos_pagar * 12
        # Recalcula o valor da parcela
        valor_parcela = valor_casa / num_parcelas
    
    # Informa ao usuário a nova proposta de pagamento com mais anos
    print(f'Será necessário aumentar o número de anos para pagar. Que tal pagar em {anos_pagar} anos ({num_parcelas} parcelas de R$ {valor_parcela:.2f})?')

# Exibe um resumo das condições do empréstimo para o usuário
print(f'\nResumo do empréstimo para {nome}:')
print(f'Valor da casa: R$ {valor_casa}')
print(f'Salário: R$ {salario}')
print(f'Anos para pagar: {anos_pagar}')
print(f'Número de parcelas: {num_parcelas}')
print(f'Valor da parcela: R$ {valor_parcela:.2f}')
