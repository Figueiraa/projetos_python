#Início das Variáveis Globais
lista_peca = []
codigo_peca = 0
#Fim das Variáveis Globais

#Início de cadastrar_peca()
def cadastrar_peca(codigo): #função para cadastrar as novas peças
    print('Bem vindo ao menu de Cadastrar Peça')
    print('Código da Peça: {}'.format(codigo)) #mostrar para o usuario o código da peça
    nome = input('Entre com o NOME da peça: ') #input para receber o nome da peça
    fabricante = input('Entre com o FABRICANTE da peça: ') #input para receber o nome do fabricante
    valor = int(input('Entre com o VALOR(R$) da peça: ')) #input para receber o valor da peça
    dicionario_peca = {'codigo' : codigo, #dicionario para guardar as informaçoes do input
                       'nome' : nome,
                       'fabricante' : fabricante,
                       'valor' : valor}
    lista_peca.append(dicionario_peca.cop1y()) #copiar o dicionario para dentro da lista
#Fim de cadastrar_peca()

#Início de consultar_peca()
def consultar_peca(): #função para consultar as peças
    print('Bem vindo ao menu de Consultar Peça')
    while True: #laço de repetição infinito
        opcao_consultar = input('\nEscolha a opção desejada:\n' + #"menu" para o usuario escolher sua opção desejada
                                '1-Consultar TODAS as Peças\n' +
                                '2-Consultar Peça por CÓDIGO\n' +
                                '3-Consultar Peça(s) por FABRICANTE\n' +
                                '4-Retornar\n' +
                                '>> ')
        if opcao_consultar == '1': #caso escolha a opção 1
            print('Você escolheu a opção Consultar TODAS as Peças')
            for peca in lista_peca: #produto vai varrer toda a lista de produto
                print('--------------------')
                for key, value in peca.items(): #varrer todos os conjuntos chave e valor do dicionario produto
                    print('{}: {}' .format(key,value))
                print('--------------------')
        elif opcao_consultar == '2': #caso escolha a opção 2
            print('Você escolheu a opção Consultar Peça por CÓDIGO')
            valor_desejado = int(input('Entre com o CÓDIGO desejado: ')) #pede o código da peça para ser consultado
            for peca in lista_peca:
                if peca['codigo'] == valor_desejado: #o valor do campo código desse dicionario é igual o valor desejado
                    print('--------------------')
                    for key, value in peca.items():  # varrer todos os conjuntos chave e valor do dicionario produto
                        print('{}: {}'.format(key, value))
                    print('--------------------')
        elif opcao_consultar == '3': #caso escolha a opção 3
            print('Você escolheu a opção Consultar Peça(s) por FABRICANTE')
            valor_desejado = input('Entre com o FABRICANTE desejado: ') #pede o fabricante da peça para ser consultado
            for peca in lista_peca:
                if peca['fabricante'] == valor_desejado:  #o valor do campo fabricante desse dicionario é igual ao fabricante desejado
                    print('--------------------')
                    for key, value in peca.items():  # varrer todos os conjuntos chave e valor do dicionario produto
                        print('{}: {}'.format(key, value))
                    print('--------------------')
        elif opcao_consultar == '4': #caso escolha a opção 4
            return #retorna
        else: #caso digite qualquer coisa que não seja uma das opções
            print('Opção Inválida. Tente Novamente')
            continue #volta para o começo do laço de repetição
#Fim de consultar_peca()

#Início de remover_peca()
def remover_peca(): #função para remover alguma peça
    print('Bem vindo ao menu de Remover Peça')
    valor_desejado = int(input('Entre com o CÓDIGO da peca que deseja remover: ')) #pede o codigo da peça para ser removida
    for peca in lista_peca:
        if peca['codigo'] == valor_desejado:  # o valor do campo código desse dicionario é igual o valor desejado
           lista_peca.remove(peca) #remove da lista o item desejado
           print('Peça Removido')
#Fim de remover_peca()

#Início do Main
print('Bem vindo ao Controle de Estoque da Bicicletaria do Pedro Henrique Figueira Silva') #identificador
while True: #laço de repetição infinito
    opcao_principal = input('\nEscolha a opção desejada:\n'+ #"menu" para o usuario escolher sua opção desejada
                            '1-Cadastrar Peça\n'+
                            '2-Consultar Peça(s)\n'+
                            '3-Remover Peça\n'+
                            '4-Sair\n'+
                            '>> ')
    if opcao_principal == '1': #caso escolha a opção 1
        codigo_peca = codigo_peca + 1 #aumenta em 1 o número do código
        cadastrar_peca(codigo_peca) #puxa a função de cadastrar
    elif opcao_principal == '2': #caso escolha a opção 3
        consultar_peca() #puxa a função de consultar
    elif opcao_principal == '3': #caso escolha a opção 3
        remover_peca() #puxa a função de remover
    elif opcao_principal == '4': #caso escolha a opção 4
        break #termina o laço de repetição/finaliza o código
    else: #caso digite qualquer coisa que não seja uma das opções
        print('Opção Inválida. Tente Novamente')
        continue #volta para o inicio do laço de repetição
#Fim do Main