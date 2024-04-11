km = int(input('Quantos Km foram percorridos? '))
dias = int(input('Por quantos dias ele foi alugado '))

preco = 60 * dias + 0.15 * km
print('Km = {} Dias: {}' .format(km, dias))
print('Valor a ser pago: {}' .format(preco))