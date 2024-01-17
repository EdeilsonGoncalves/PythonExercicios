#Condições

'''nome = str(input("Qual é seu nome? "))
if nome == "Ed":
    print("\nQue lindo nome você tem!")
else:
    print("\nSeu nome é tão normal!")
print("\nBom dia, {}!".format(nome))'''

#Outro exemplo com condição composta::

'''nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) /2

print("\nA sua média foi {:.1f}".format(media))

if media>= 6.0:
    print("\nSua média foi boa, PARABÉNS!")
else:
    print("\nSua média foi ruim! ESTUDE MAIS!")'''

#Outra forma de fazer atarvés da condição simplificada:

'''nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) /2

print("\nA sua média foi {:.1f}".format(media))
print("\nParabéns" if media >=6 else "ESTUDE MAIS!")'''

'''Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário
tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário 
venceu ou perdeu.'''

from random import randint
from  time import sleep #Faz esperar
computador = randint (0, 5) #Faz o computador sortear
print("-==-" * 20)
print("Vou pensar em um número entre 0 e 5. Tente acertar...")
print("-==-" * 20)
jogador = int(input('Em que número eu pensei? ')) #Jogador tenta acertar
print("PROCESSANDO...")
sleep(3)
if jogador == computador: #Se meu valor digitado for igual o do computador
    print("PARABÉNS! Você conseguiu me vencer!")
else:
    print("GANHEI! Eu pensei no número {} e não no número {}!".format(computador, jogador))






















