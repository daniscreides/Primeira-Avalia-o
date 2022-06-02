#Escreva um programa que possa ler um número inteiro entre 1 e 12 e, assumindo que esse valor representa um determinado mês do ano, imprimir o nome do mês por extenso. O programa deve verificar se uma entrada inválida foi digitada pelo usuário do programa (por exemplo, -5 ou 100). Neste caso, o programa deve exibir na tela apenas uma mensagem de erro.

mes= int(input("Digite o número do mês: "))

nome1= "Janeiro"
nome2= "Fevereiro"
nome3= "Março"
nome4= "Abril"
nome5= "Maio"
nome6= "Junho"
nome7= "Julho"
nome8= "Agosto"
nome9= "Setembro"
nome10= "Outubro"
nome11= "Novembro"
nome12= "Dezembro"


if mes >=1 and mes <= 12: 
  if mes == 1: 
    print (nome1)
  elif mes == 2: 
    print (nome2)
  elif mes == 3: 
    print (nome3)
  elif mes == 4: 
    print (nome4)
  elif mes == 5: 
    print (nome5)
  elif mes == 6: 
    print (nome6)
  elif mes == 7: 
    print (nome7)
  elif mes == 8: 
    print (nome8)
  elif mes == 9: 
    print (nome9)
  elif mes == 10: 
    print (nome10)
  elif mes == 11: 
    print (nome11)
  elif mes == 12: 
    print (nome12)
else:
    print ("Mês Inexistente!")