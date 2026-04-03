salario = float(input('Qual seu salário: '))
if salario >= 1250:
    print('Seu salário foi reajustado para: R${:.2f}'.format(salario+(salario*0.1)))
else :
    print('Seu salárop foi reajustado para: R${:.2f}'.format(salario+(salario*0.15)))