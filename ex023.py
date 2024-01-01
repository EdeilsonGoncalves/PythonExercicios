'''Faça um programa que leia um número de 0 a 9999 e mostre na tela
cada um dos dígitos separados.
#Ex
Digite um número: 1834
unidade: 4 dezena: 3 centena: 8 milhar 1



num = int(input("Informe um número: "))

#Converte número em string
n = str(num)

print('\nAnalisando o número {}'.format(num))

print("\nUnidade: {}".format(n[3])) #Pega a posição que está o número
print("Dezena: {}".format(n[2]))
print("Centena: {}".format(n[1]))
print("Milhar: {}".format(n[0]))'''

#Outra forma de fazer:

num = int(input("Informe um número: "))

unidade = num // 1 % 10  # // Divisão inteira por um e % retira o resto da divisão por 10.
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10



print('\nAnalisando o número {}'.format(num))

print("\nUnidade: {}".format(unidade))
print("Dezena: {}".format(dezena))
print("Centena: {}".format(centena))
print("Milhar: {}".format(milhar))


























































