#CRIE UM PROGRAMA QUE LEIA O NOME DE UMA CIDADE E DIGA SE ELA COMEÇA OU NÃO COM O NOME "SANTO".

cidade = input("Digite uma cidade:").upper().split()[0]
print(cidade)

if cidade == 'SANTO':
    print ("A cidade começa com SANTO")
else:
    print ("A cidade não começa com SANTO")
