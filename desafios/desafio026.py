#FAÇA UM PROGRAMA QUE LEIA UMA FRASE PELO TECLADO E MOSTRE:
#QUANTAS VEZES APARECE A LETRA "A", EM QUE POSIÇÃO ELA APARECE A PRIMEIRA VEZ
#EM QUE POSIÇÃO ELA APARECE A ÚLTIMA VEZ

frase = input('Digite uma frase: ').lower()
qtd_letra = frase.count('a')
print("A palavra aparece " + str(qtd_letra) + " vezes")
primeira_posicao = frase.find('a')
print("Aparece pela primeira vez na posição " + str(primeira_posicao))
ultima_posicao = frase.find('a',-1)
print(str(ultima_posicao))
    
#for i in list(frase):
 #   print(i)
#le = print(len(str(i)))
#print(str(le).find('a'))
#indice = print(str(frase).split('o'))
#print(str(indice))
#letras = frase.split()
#print(len(letras))