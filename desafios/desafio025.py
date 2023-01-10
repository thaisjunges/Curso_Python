#CRIE UM PROGRAMA QUE LEIA O NOME DE UMA PESSOA E DIGA SE ELA TEM "SILVA" NO NOME.

nome = input("Digite seu nome: ").upper()


if 'SILVA' in nome:
    print ("Tem silva no nome")
else:
    print("Não tem silva no nome")