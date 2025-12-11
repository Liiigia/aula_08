# Solicitar ao usuário, o preço e a quantidade referente a 3 vendas
# Para cada venda o sistema deve calcular o valor total 
# exibir o resultado


def valor_total(preço1, preço2):
   total = preço1 * preço2
#  print(f'O valor total par cada venda é: {total} ')
   return total   # pra retornar um valor la para baixo na linha 16, sendo assim travei  com # a linha 8 - devolve para onde foi chamado



for v in range(3):
   venda = float(input('Digite o preço1:'))
   quantidade = float(input('Digite a quantidade1: '))  
   totalidade = valor_total(venda, quantidade)    # lê -se, totalidade recebe o valor da função
   print(f' valor total :{totalidade} ')





