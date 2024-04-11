import math

print(math.sqrt(9))

while True :
  try:
    entrada = int(input('Insira um número : '))
    print(f'O número inserido foi {entrada} e não houve erro, tudo certo !')
    option = input('Deseja tentar de novo ? S - Sim ou N - Não ')
    option = option.upper()
    if (option == 'S'):
      print(option)
      continue
    else:
      break
  except:
    print(f'Foi inserido algum caracter que não é numerico e houve um erro, então entrou aqui no except !')
    continue
print('Saindo do programa...')