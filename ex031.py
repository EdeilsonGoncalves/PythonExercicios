'''Desenvolva um programa que pergunte a distância de uma viagem em km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km
e R$0,45 para viagens mais longas.
'''



'''distancia = float(input("Qual é a disatância de sua viagem? "))
print("Você está prestes a começar uma viagem de {}Km.".format(distancia))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print("O preço da sua passagem será de R${:.2f}".format(preco))'''




#Outra forma de fazer:

distancia = float(input("Qual é a disatância de sua viagem? "))
print("Você está prestes a começar uma viagem de {}Km.".format(distancia))
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print("O preço da sua passagem será de R${:.2f}".format(preco))