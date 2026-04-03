velocidade = float(input('Velocidade do veiculo: '))
multa = (velocidade-70)*7+150
if velocidade >70:

    print('Você foi multado, no valor de R${:.2f}'.format(multa))

else :
    print('Veiculo não foi multado')

