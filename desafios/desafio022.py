#CRIE UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA E MOSTRE:

#O NOME COM TODAS AS LETRAS MAIÚSCULAS, MINÚSCULAS E QUANTAS LETRAS AO todo
#SEM CONSIDERAR ESPAÇOS E QUANTAS LETRAS TEM O PRIMEIRO NOME.

nome = input("Digite seu nome completo:")

n = nome.replace(" ", "")
print(nome.upper())
print(n.lower())
print(len(n))

 

