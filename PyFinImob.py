nome = input('Olá! seja bem-vindo ao Rael Bank.\nPor gentileza, me informe seu nome: ')
valor_casa = int(input('Qual o valor da casa que você pretende comprar? '))
salario = int(input('Por gentileza, digite o valor do seu salário: '))
anos_pagar = int(input('Está quase tudo pronto!\nMe informe a quantidade de anos que você quer parcelar seu empréstimo: '))

num_parcelas = anos_pagar * 12
valor_parcela = valor_casa / num_parcelas
score30 = salario * 0.30

if valor_parcela <= score30:
    print(f'Tenho uma ótima notícia para você, {nome}!\nSeu empréstimo foi APROVADO!!!')
else:
    print(f'Poxa, {nome}, infelizmente o valor da parcela excede os limites do seu salário.')
    while valor_parcela > score30:
        anos_pagar += 1
        num_parcelas = anos_pagar * 12
        valor_parcela = valor_casa / num_parcelas
    print(f'Será necessário aumentar o número de anos para pagar. Que tal pagar em {anos_pagar} anos ({num_parcelas} parcelas de R$ {valor_parcela:.2f})?')

print(f'\nResumo do empréstimo para {nome}:')
print(f'Valor da casa: R$ {valor_casa}')
print(f'Salário: R$ {salario}')
print(f'Anos para pagar: {anos_pagar}')
print(f'Número de parcelas: {num_parcelas}')
print(f'Valor da parcela: R$ {valor_parcela:.2f}')
