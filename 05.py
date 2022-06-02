"""
Faça um programa para uma escola que, dadas três notas de um aluno e seu nome completo, exiba, no final, o nome do estudante, a média final e o seu conceito, observando que:
a média final é calculada a partir da média aritmética simples das 3 notas;
o conceito é determinado a partir da tabela a seguir (continua na próxima página):
MÉDIA FINAL
CONCEITO
95 - 100
A

70 - 94
B

50 - 69
C

0  - 49
D

A mensagem final exibida do sistema deve ter o seguinte formato (substitua os espaços entre <> pelos respectivos valores passado como entrada para o sistema):
“<Fulano de tal> obteve conceito <X>”
“As notas fornecidas como entrada foram: <N1>, <N2> e <N3> com Média final: <M>”
"""

nome= input("Nome do aluno: ")
nota1= int(input("1ª nota: "))
nota2= int(input("2ª nota: "))
nota3= int(input("3ª nota: "))

media = (nota1 + nota2 + nota3) / 3

conceito = "x"

if media >= 95 and media <=100:
  conceito = "A" 
elif media >= 70 and media <= 94:
  conceito = "B"
elif media >= 50 and media <= 69:
  conceito = "C"
else:
  conceito = "D"

print ( nome + " obteve conceito " + conceito )

print ("As notas fornecidas como entrada foram: " + "(" + str(nota1) + "," + str(nota2) + "," + str(nota3) + ")" + " com média final: " + '"' + str(conceito) + '"')