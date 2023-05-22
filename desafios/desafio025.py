#CRIE UM PROGRAMA QUE LEIA O NOME DE UMA PESSOA E DIGA SE ELA TEM "SILVA" NO NOME.

nome = input("Digite seu nome: ").upper()

palavra = 'SILVA'

if nome not in 'SILVA':
    print ("Tem silva no nome")
else:
    print ("Não tem silva no nome")
