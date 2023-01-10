#FAÇA UM PROGRAMA QUE LEIA UMA FRASE PELO TECLADO E MOSTRE:
#QUANTAS VEZES APARECE A LETRA "A", EM QUE POSIÇÃO ELA APARECE A PRIMEIRA VEZ
#EM QUE POSIÇÃO ELA APARECE A ÚLTIMA VEZ

frase = input("Digite uma frase: ")

#vezes = frase.count('a')
#print('A letra A aparece ' + vezes)

quant = frase.find('a')
print('A primeira posição é na ' + quant)

