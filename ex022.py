'''Crie um programa que leia o nome completo de uma pessoa e mostre:
O nome com todas as letras maíusculas e minúsculas.
Quantas letras ao todo (sem considerar espaços).
Quantas letras tem o primeiro nome.'''


nome = str(input('Digite seu nome completo: '))
print('Analisando seu nome...')
print('Seu nome em maiúscula é {}'.format(nome.upper()))
print("Seu nome em minúscula é {}".format(nome.lower()))

letras = nome.split()
print("Seu nome tem ao todo {} letras".format(sum(len(l) for l in letras)))

primeira_palavra = letras[0]

print("A primeira palavra do seu nome tem {} letras".format(len(primeira_palavra)))

