#FAÇA UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA,MOSTRANDO EM SEGUIDA O PRIMEIRO 
#E O ÚLTIMO NOME SEPARADAMENTE
#EX: ANA MARIA DE SOUZA
#PRIMEIRO: ANA
#ÚLTIMO: SOUZA

nome_completo = input("Digite seu nome completo: ").upper()
print("Seu nome completo é: " + str(nome_completo))
primeiro_nome = nome_completo.split()[0]
print("O primeiro nome é " + str(primeiro_nome))
ultimo_nome = nome_completo.split()[-1]
print(str(ultimo_nome))
