def dimensoesObjetos():  # função para receber as medidas do objeto e calcular o volume dele

    while True:  # laço de repetição infinito

        try:

            alturaObjeto = float(input('Digite a altura do objeto (em cm): '))  # entrada da altura do objeto

            comprimentoObjeto = float(
                input('Digite o comprimento do objeto (em cm): '))  # entrada do comprimento do objeto

            larguraObjeto = float(input('Digite a largura do objeto (em cm): '))  # entrada da largura do objeto

            volumeObjeto = alturaObjeto * comprimentoObjeto * larguraObjeto  # calculo do volume do objeto

            print('O volume do objeto é (em cm³): {}'.format(volumeObjeto))  # print do volume do objeto

            # Teste para determinar o valor do objeto

            if volumeObjeto < 1000:  # Volume menor que 1000

                valorObjeto = 10  # 10 reais

            elif 1000 <= volumeObjeto < 10000:  # Volume entre 1000 e 10000

                valorObjeto = 20  # 20 reais

            elif 10000 <= volumeObjeto < 30000:  # Volume entre 10000 e 30000

                valorObjeto = 30  # 30 reais

            elif 30000 <= volumeObjeto < 100000:  # Volume entre 30000 e 100000

                valorObjeto = 50  # 50 reais

            else:  # Caso o volume seja igual ou maior que 100000

                print('Não aceitamos objetos com dimensões tão grandes')

                print('Entre com as dimensoes desejadas novamente')

                continue  # Volta para o inicio da função

            return valorObjeto  # retorna o valor do objeto

            break  # Acaba a função

        except:  # Caso ocorra algum erro quando digitar as dimenões do objeto

            print('Você digitou alguma dimensão do objeto com valor não númerico')

            print('Por favor entre com a dimensão do objeto desejado novamente')

            continue  # Volta para o inicio da função


def pesoObjeto():  # função para receber o peso do objeto e calcular o multiplicador dele

    while True:  # laço de repetição infinito

        try:

            pesoDoObjeto = float(input('Digite o peso do objeto (em kg): '))  # entrada do peso do objeto

            # Teste para determinar o multiplicador do peso do objeto

            if pesoDoObjeto <= 0.1:  # Peso menor ou igual a 0.1

                multiplicadorObjeto = 1  # Multiplicador 1

            elif 0.1 <= pesoDoObjeto < 1:  # Peso entre 0.1 e 1

                multiplicadorObjeto = 1.5  # Multiplicador 1.5

            elif 1 <= pesoDoObjeto < 10:  # Peso entre 1 e 10

                multiplicadorObjeto = 2  # Multiplicador 2

            elif 10 <= pesoDoObjeto < 30:  # Peso entre 10 e 30

                multiplicadorObjeto = 3  # Multiplicador 3

            else:  # Caso o pesa seja igual ou maior que 30

                print('Não aceitamos objetos tão pesados')

                print('Entre com o peso desejado novamente')

                continue  # Volta para o inicio da função

            return multiplicadorObjeto  # retorna o multiplicador do peso do objeto

            break  # Acaba a função

        except:  # Caso ocorra algum erro quando digitar o peso do objeto

            print('Você digitou o peso do objeto com valor não númerico')

            print('Por favor entre com o peso desejado novamente')

            continue  # Volta para o inicio da função


def rotaObjeto():  # função para receber a rota que o objeto vai fazer e ver o multiplicador que vai ser aplicado nessa rota

    print('----------SELECIONE SUA ROTA----------')  # Uma espécie de menu com opçoes de rotas

    print('SR - De São Paulo até Rio Grande do Sul')

    print('SM - De São Paulo até Maceió')

    print('ST - De São Paulo até Tocantins')

    while True:  # laço de repetição infinito

        siglaRota = input('Digite a sigla da rota a ser utilizada: ')  # entrada da rota a ser utilizada

        siglaRota = siglaRota.upper()  # Transforma o que foi digitado em maiusculo

        if siglaRota != 'SR' and siglaRota != 'SM' and siglaRota != 'ST':  # if para determinar se alguma das rotas foi selecionada

            print('Você digitou uma rota que não existe')  # mensagem para mostrar o erro

            continue  # Volta para o inicio da função

        if siglaRota == 'SR':  # caso a sigla escolhida seja 'SR'

            multiplicadorRota = 1  # Multiplicador 1




        elif siglaRota == 'SM':  # caso a sigla escolhida seja 'SM'

            multiplicadorRota = 1.2  # Multiplicador 1.2




        elif siglaRota == 'ST':  # caso a sigla escolhida seja 'ST'

            multiplicadorRota = 1.5  # Multiplicador 1.5

        break  # Acaba a função

    return multiplicadorRota  # retorna o multiplicador do rota do objeto


# Inicio do Main

print('Bem vindo a Companhia de Logistica Pedro Henrique Figueira Silva')  # identificador

dimensoes = dimensoesObjetos()  # trandormando o return do dimensoesObjetos em uma variavel

peso = pesoObjeto()  # trandormando o return do pesoObjetos em uma variavel

rota = rotaObjeto()  # trandormando o return do rotaObjetos em uma variavel

valorFinal = dimensoes * peso * rota  # calcula o valor final a ser pago

print('Total a pagar(R$): {} (dimensões: {} * peso: {} * rota: {})'.format(valorFinal, dimensoes, peso,
                                                                           rota))  # print do valor e do calculo pro usuario