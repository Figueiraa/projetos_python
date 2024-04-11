print('Bem-Vindo a lanchonete do Pedro Henrique Figueira Silva') #identificador
print('-------------------CARDAPIO-------------------') #cardapio da lanchonete
print('CÓDIGO |        DESCRIÇÃO        |  VALOR(R$)')
print('  100  |     Cachorro-Quente     |    9,00')
print('  101  |  Cachorro-Quente Duplo  |    11,00')
print('  102  |          X-Egg          |    12,00')
print('  103  |         X-Salada        |    13,00')
print('  104  |         X-Bacon         |    14,00')
print('  105  |         X-Tudo          |    17,00')
print('  200  |    Refrigerante Lata    |    5,00')
print('  201  |        Chá Gelado       |    4,00')

valor = 0
while True: #laço de repetição infinito
    codigo = input('Digite o código do produto desejado: ') #entrada do código do produto
    if codigo != '100' and codigo != '101' and codigo != '102' and codigo != '103' and codigo != '104' and codigo != '105' and codigo != '200' and codigo != '201': #if para determinar se algum dos códigos foi selecionado
        print('Código invalido, tente novamente!') #mensagem para mostrar o erro
        continue#Volta para o inicio ddo while

    if codigo == '100': #caso o codigo escolhida seja '100'
        print('Você pediu um Cachorro-Quente no valor de R$9,00') #print para mostrar o pedido escolhido
        valor = valor + 9 #acumulador para adicionar o preço

    elif codigo == '101': #caso o codigo escolhida seja '101'
        print('Você pediu um Cachorro-Quente Duplo no valor de R$11,00') #print para mostrar o pedido escolhido
        valor = valor + 11 #acumulador para adicionar o preço

    elif codigo == '102': #caso o codigo escolhida seja '102'
        print('Você pediu um X-Egg no valor de R$12,00') #print para mostrar o pedido escolhido
        valor = valor + 12 #acumulador para adicionar o preço

    elif codigo == '103': #caso o codigo escolhida seja '103'
        print('Você pediu um X-Salada no valor de R$13,00') #print para mostrar o pedido escolhido
        valor = valor + 13 #acumulador para adicionar o preço

    elif codigo == '104': #caso o codigo escolhida seja '104'
        print('Você pediu um X-Bacon no valor de R$14,00') #print para mostrar o pedido escolhido
        valor = valor + 14 #acumulador para adicionar o preço

    elif codigo == '105': #caso o codigo escolhida seja '105'
        print('Você pediu um X-Tudo no valor de R$17,00') #print para mostrar o pedido escolhido
        valor = valor + 17 #acumulador para adicionar o preço

    elif codigo == '200': #caso o codigo escolhida seja '200'
        print('Você pediu um Refrigerante Lata no valor de R$5,00') #print para mostrar o pedido escolhido
        valor = valor + 5 #acumulador para adicionar o preço

    elif codigo == '201': #caso o codigo escolhida seja '201'
        print('Você pediu um Chá Gelado no valor de R$4,00') #print para mostrar o pedido escolhido
        valor = valor + 4 #acumulador para adicionar o preço

    pedir_mais = input('Deseja pedir mais alguma coisa? \n' #input para a pessoa escolher se quer mais alguma coisa ou se não
                       '1 = Sim\n'
                       '0 = Não\n'
                       '>> ')
    if pedir_mais == '1': #se escolher o 1 volta para o inicio do codigo para escolher outra coisa
        continue #volta para o inicio do while
    else: #se escolher o outro finaliza o while
        print('O valor total a ser pago: R${:.2f}' .format(valor)) #mostra o valor final
        break #finaliza o codigo