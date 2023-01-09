#FAÇA UM PROGRAMA QUE LEIA UM NÚMERO DE 0 A 9999
#E MOSTRE NA TELA CADA UM DOS DÍGITOS SEPARADOS.

#EX: DIGITE UM NÚMERO: 18347

#UNIDADE: 4 
#DEZENA: 3
#CENTENA:8
#MILHAR:1

numero = input('Digite um número de 0 a 9999:')
print(" ".join(numero))
n = numero.split()
#print(numero[1][2][3][4])
print('Unidade: ' + numero[3])
print('Dezena: ' + numero[2])
print('Centena: ' + numero[1])
print('Milhar: ' + numero[0])


