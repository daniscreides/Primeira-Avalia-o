#Escreva um programa para uma loja capaz de calcular o valor final da compra para um cliente. O programa deve receber como entrada: a) o valor da compra, e b) a quantidade de parcelas desejada. Importante! se o número de parcelas for igual a “1” (ou seja, pagamento à vista), o programa deverá aplicar um desconto de 10% sobre o valor inicial da compra e exibir apenas o valor final calculado. Porém, se a compra for parcelada, o programa deverá, primeiro, aplicar um juros de 50% sobre o valor inicial da compra e, depois, dividir o valor final (com juros) pela quantidade de parcelas recebida como entrada. Exiba, na tela, todo o resultado do processamento (valores inicial e final da compra, bem como a quantidade e o valor final da parcela) com duas casas decimais, quando possível.

valor_compra= float(input("Valor da compra: "))
parcelas= int(input("Quantidade de parcelas: "))

sem_juros = valor_compra * (- 0.1) + valor_compra
com_juros = valor_compra * 0.5 + valor_compra
valor_parcela = com_juros / parcelas

if parcelas == 1:
  print ("CUPOM FISCAL")
  print ("Você ganhou 10% de desconto na sua compra. ")
  print ("Valor inicial: " + "{:.2f}".format(valor_compra))
  print ("valor com desconto: " + "{:.2f}".format(sem_juros))
else:
  print ("Por causa das parcelas, o valor final de sua compra ficará de " + "{:.2f}".format(com_juros))
  print ("CUPOM FISCAL")
  print ("Valor inicial: " + "{:.2f}".format(valor_compra))
  print ("valor com juros: " + "{:.2f}".format(com_juros))
  print ("Valor de cada parcela é: " + "{:.2f}".format(valor_parcela))
