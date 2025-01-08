from datetime import datetime

# Obtém a hora atual e define a saudação
hora_atual = datetime.now().hour
saudacao = "Bom dia" if hora_atual < 12 else "Boa tarde" if hora_atual < 18 else "Boa noite"

# Mensagem de boas-vindas
print(f'✨ {saudacao}, bem-vindo ao Rael Bank! ✨')
print('Aqui, nosso objetivo é ajudar você a transformar seus sonhos em realidade.\n')

# Solicita o nome e informações do usuário
nome = input('Qual é o seu nome? ')

while True:
    try:
        valor_casa = float(input(f'\nQual o valor da casa que você deseja comprar, {nome}? R$ '))
        entrada = float(input('Você pretende dar uma entrada? Se sim, informe o valor (ou digite 0): R$ '))
        salario = float(input('Qual o valor do seu salário mensal? R$ '))
        anos_pagar = int(input('Em quantos anos você gostaria de parcelar o seu empréstimo? '))
        
        # Validações simples para garantir que os valores sejam razoáveis
        if valor_casa <= 0 or salario <= 0 or anos_pagar <= 0:
            print("Valores inválidos, por favor, insira valores positivos.")
            continue
        break
    except ValueError:
        print("Por favor, insira um número válido.")

# Calcula valores
valor_financiado = valor_casa - entrada
num_parcelas = anos_pagar * 12
valor_parcelas = valor_financiado / num_parcelas
score30 = salario * 0.30

# Simulação de juros: taxa de 6% ao ano
taxa_juros_ano = 0.06
juros_totais = valor_financiado * taxa_juros_ano * anos_pagar
valor_total_com_juros = valor_financiado + juros_totais
valor_parcelas_com_juros = valor_total_com_juros / num_parcelas

# Exibe o valor da parcela inicial sem juros
print(f'\nO valor da sua parcela sem juros seria: R$ {valor_parcelas:.2f}')

# Exibe o valor da parcela com juros
print(f'Com juros de {taxa_juros_ano * 100}% ao ano, o valor da sua parcela seria: R$ {valor_parcelas_com_juros:.2f}\n')

# Verifica aprovação do empréstimo
if valor_parcelas_com_juros <= score30:
    print(f'🎉 Seu empréstimo foi APROVADO, {nome}! 🎉\n')
else:
    print(f'⚠ A parcela excede 30% do seu salário. Vamos ajustar!\n')
    while valor_parcelas_com_juros > score30:
        anos_pagar += 1
        num_parcelas = anos_pagar * 12
        valor_parcelas_com_juros = valor_total_com_juros / num_parcelas
    print(f'🔄 Ajustamos para {anos_pagar} anos, diminuindo o valor da parcela.\n')

# Pergunta se o cliente aceita a nova proposta
if input('O que você acha dessa nova proposta? (sim/não): ').strip().lower() == 'sim':
    print(f'\nPerfeito, {nome}! Vamos em frente! 🎉\n')
else:
    print(f'\nSem problema, {nome}! Vamos encontrar a melhor solução para você. 🤝\n')

# Exibe o resumo final
print(f'🔑 Resumo do seu empréstimo:')
print(f'Valor da casa: R$ {valor_casa:.2f}')
print(f'Valor da entrada: R$ {entrada:.2f}')
print(f'Valor financiado: R$ {valor_financiado:.2f}')
print(f'Número de parcelas: {num_parcelas} parcelas')
print(f'Valor da parcela com juros: R$ {valor_parcelas_com_juros:.2f}')
print(f'Valor total pago ao final do financiamento (incluindo juros): R$ {valor_total_com_juros:.2f}')
