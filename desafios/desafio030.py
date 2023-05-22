#CRIE UM PROGRAMA QUE LEIA UM NÚMERO INTERIRO E MOSTRE NA TELA SE ELE É PAR OU ÍMPAR

numero_int = int(input("Digite um numero inteiro: "))

par = (numero_int % 2)

if par == 0:
    print('É par')
else:
    print('É ímpar')

