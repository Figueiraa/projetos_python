print('Bem-vindo a loja do Pedro Henrique Figueira Silva') #identificador
valor_produto = float(input('Digite o preço do produto: ')) #Entrada do valor do produto
qtd_produto = int(input('Digite a quantidade do produto: ')) #Entrada da quantidade do produto
desconto_produto = 0

# Teste para determinar o desconto do produto
if qtd_produto <= 9: #Desconte até 9 unidades
    desconto_produto = 0.00 #0% = 0.00 / 100% = 1.00
elif 10 <= qtd_produto <= 99: #Desconte entre 10 e 99 unidades
    desconto_produto = 0.05 # 5% = 0.05 / 100% = 1.00
elif 100 <= qtd_produto <= 999: #Desconte entre 100 e 999 unidades
    desconto_produto = 0.10 # 10% = 0.10 / 100% = 1.00
else: #Desconte para 1000 ou mais unidades
    desconto_produto = 0.15 # 15% = 0.15 / 100% = 1.00

total_sem_desconto = valor_produto * qtd_produto #Calculo do valor sem desconto
print('O valor sem desconto foi: R$ {:.2f}' .format(total_sem_desconto))  #print do valor sem desconto
total_com_desconto = total_sem_desconto - total_sem_desconto * desconto_produto #Calculo do valor com desconto
print('O valor com desconto foi: R$ {:.2f}' .format(total_com_desconto,desconto_produto)) #print do valor com desconto