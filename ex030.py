#Crie um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar.

numero = int(input("Me diga um número qualquer: "))
resultado = numero % 2
print("O resultado foi {}.".format(resultado))
if resultado == 0:
    print("O número {} é PAR.".format(numero))
else:
    print("O número {} é ÍMPAR.".format(numero))



