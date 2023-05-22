#FAÇA UM PROGRAMA QUE LEIA TRÊS NÚMEROS E MOSTRE QUAL É O MAIOR E QUAL É O MENOR.

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

maior = n1

if n1 >= n2 and n1 >= n3: 
    maior = n1
if n2 >= n1 and n2 >= n3:
    maior = n2

menor = n1

if n1 <= n2 and n1<= n3:
    menor = n1
if n2 <= n1 and n2 <= n3:
    menor = n2

print('Menor {}'.format(menor))
print('Maior {}'.format(maior)) 