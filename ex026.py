#Faça um programa que leia uma frase pelo teclao e mostre:

#Quantas vezes aparece a letra "A".
#Em que posição ela aparece a primeira vez.
#Em que posição ela aaparece a última vez.

#upper vai fazer jogar todas as letras "A" para maiúscula.
#strip retira os espaços indesejados
frase = str(input("Digite uma frase: ")).upper().strip()

#Através da variável frase na entrada de dados input vai contar quantas vezes a letra A foi digitada.
print("A letra A aparece {} vezes na frase.".format(frase.count("A")))

#find para ir no índice e +1 é para ignorar o primeiro do índice que é zero e ser 1.
print("A primeira letra A apareceu na posição {}".format(frase.find("A")+1))


#rfind significa procure apartir do lado right (à direita).
print("A última letra A apareceu na posição {}".format(frase.rfind("A")+1))



















