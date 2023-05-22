#ESCREVA UM PROGRAMA QUE FAÇA O COMPUTADOR 'PENSAR' EM UM NÚMERO INTEIRO
#ENTRE 0 E 5 E PEÇA PARA O USUÁRIO TENTAR DESCOBRIR QUAL FOI O NÚMERO ESCOLHIDO
#O PROGRAMA DEVERÁ ESCREVER NA TELA SE O USUÁRIO VENCEU OU PERDEU.
import random

numero = input("Digite um numero de 0 a 5:" )

numero_escolhido = random.randint(0,5)

if numero == numero_escolhido:
    print('Você venceu o numero_escolhido foi {}'.format(numero_escolhido))
else:
    print('Você perdeu o número foi {}'.format(numero_escolhido))