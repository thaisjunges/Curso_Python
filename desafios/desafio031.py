#DESENVOLVA UM PROGRAMA QUE PERGUNTE A DISTÂNCIA DE UM VIAGEM EM KM.
#CALCULE O PREÇO DA PASSAGEM,COBRANDO R$0.50 PO KM PARA VIAGENS DE ATÉ 200KM
#E R$0.45 PARA VIAGENS MAIS LONGAS.

viagem_km = input("Digite a distância da sua viagem em KM: ")

viagens_limite = float(viagem_km) * float(0.50)
ultrapassa_limite = float(viagem_km) * float(0.45)
limite = 200

if float(viagem_km) <= limite:
    print("Você percorreu " + viagem_km + "KM e vai pagar {}".format(viagens_limite))
else:
    print("Você percorreu " + viagem_km + "KM e vai pagar {}".format(ultrapassa_limite))
