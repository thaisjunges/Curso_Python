#ESCREVA UM PROGRAMA QUE PERGUNTE O SALÁRIO DE UM FUNCIONÁRIO 
#E CALCULE O VALOR DO SEU AUMENTO
#PARA SALÁRIOS SUPERIORES A R$1.250,00, calcule um aumento de 10%
#PARA OS INFERIORES OU IGUAIS,O AUMENTO É DE 15%

salario_funci = float(input('Digite seu salário: '))
fixo = float(1250)

if salario_funci > fixo :
    aumento_10 = salario_funci * 0.10
    total = aumento_10 + salario_funci
    print('Você recebeu um aumento de R$ {} e o valor total do seu salário é {}'.format(aumento_10, total))
    
else :
    aumento_15 = salario_funci * 0.15
    total = aumento_15 + salario_funci
    print('Você recebeu um amumento de R$ {} e o valor total do seu salário {}'.format(aumento_15, total))
