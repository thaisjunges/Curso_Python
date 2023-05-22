#DESENVOLVA UM PROGRAMA QUE LEIA O COMPRIMENTO DE TRÊS RETAS E DIGA AO USUÁRIO
#SE ELAS PODEM OU NÃO FORMAR UM TRIÂNGULO.

primeira = int(input("Digite o primeiro comprimento: "))
segundo = int(input("Digite o segundo comprimento: "))
terceiro = int(input("Digite o terceiro comprimento: "))

soma = (primeira) + (segundo)

if soma > terceiro:
    print("Pode formar um triângulo")
else:
    print("Não pode formar um triângulo")