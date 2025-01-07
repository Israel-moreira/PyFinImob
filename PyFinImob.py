from datetime import datetime

# Obtém a hora atual e define a saudação
hora_atual = datetime.now().hour
saudacao = "Bom dia" if hora_atual < 12 else "Boa tarde" if hora_atual < 18 else "Boa noite"

# Mensagem de boas-vindas
print(f'✨ {saudacao}, bem-vindo ao Rael Bank! ✨')
print('Aqui, nosso objetivo é ajudar você a transformar seus sonhos em realidade.')

# Solicita o nome e informações do usuário
nome = input('\nQual é o seu nome? ')
valor_casa = float(input(f'\nQual o valor da casa que você deseja comprar, {nome}? R$ '))
entrada = float(input('Você pretende dar uma entrada? Se sim, informe o valor (ou digite 0): R$ '))
salario = float(input('Qual o valor do seu salário mensal? R$ '))
anos_pagar = int(input('Em quantos anos você gostaria de parcelar o seu empréstimo? '))

# Calcula valores
valor_financiado = valor_casa - entrada
num_parcelas = anos_pagar * 12
valor_parcelas = valor_financiado / num_parcelas
score30 = salario * 0.30

# Verifica aprovação do empréstimo
if valor_parcelas <= score30:
    print(f'\n🎉 Seu empréstimo foi APROVADO, {nome}! 🎉')
else:
    print(f'\n⚠ A parcela excede 30% do seu salário. Vamos ajustar!')
    while valor_parcelas > score30:
        anos_pagar += 1
        num_parcelas = anos_pagar * 12
        valor_parcelas = valor_financiado / num_parcelas
    print(f'\n🔄 Ajustamos para {anos_pagar} anos, diminuindo o valor da parcela.')

    # Pergunta se o cliente aceita a nova proposta
    if input(f'O que você acha dessa nova proposta? (sim/não): ').strip().lower() == 'sim':
        print(f'\nPerfeito, {nome}! Vamos em frente!')
    else:
        print(f'\nSem problema, {nome}! Vamos encontrar a melhor solução para você.')
