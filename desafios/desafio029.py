#ESCREVA UM PROGRAMA QUE LEIA A VELOCIDADE DE UM CARRO
#SE ELE ULTRAPASSAR 80KM MOSTRE UMA MENSAGEM DIZENDO QUE FOI MULTADO
#A MULTA VAI CUSTAR R$7,00 POR CADA KM ACIMA DO LIMITE

velocidade_atual = input("Digite sua velocidade: ")

velocidade_maxima = 80
multa = 0.07
valor_multa = float(velocidade_atual) * float(multa)
valor_total = float(velocidade_atual) - float(valor_multa)  

if int(velocidade_atual) > int(velocidade_maxima):
    print(velocidade_atual)

    print('Multado no valor de R$ {}'.format(valor_total))
else:
    print("Não multado") 
