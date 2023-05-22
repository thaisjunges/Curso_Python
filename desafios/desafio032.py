#FAÇA UM ROGRAMA QUE LEIA UM ANO QUALQUER E MOSTRE SE ELE É BISSEXTO

ano = input("Digite uma ano: ")

bissexto = int(ano) % int(4)

if bissexto == 0:
    print(str(ano) + (" é um ano bissexto"))
else: 
    print(str(ano) + (" não é um ano bissexto"))