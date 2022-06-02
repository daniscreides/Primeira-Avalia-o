#Faça um programa para um restaurante capaz de efetuar o cálculo da conta. Para obter o cálculo, o usuário deverá fornecer ao programa: a) o nome do garçom, b) o número da mesa, c) o valor inicial da conta (sem 10% do garçom), e d) o número de integrantes da mesa. O programa, então, deverá apresentar estes valores digitados juntamente com o cálculo dos 10% do garçom, o novo valor final da despesa (com 10% do garçom) e, finalmente, quanto cada integrante da mesa deverá pagar. Exiba, na tela, o resultado do processamento com duas casas decimais, quando possível.

garcom= input("Nome do Garçon: ")
mesa= int(input("Nº da Mesa: "))
valor_inicial= float(input("Valor da conta sem os 10%: "))
pessoas= int(input("Quantidade de pessoas na mesa: "))

valor_final = valor_inicial * 0.1 + valor_inicial

divisao= valor_final / pessoas

print ("Valor a ser pago: " + "{:.2f}".format(valor_final))
print ("Valor a ser pago por pessoa: " + "{:.2f}".format(divisao))