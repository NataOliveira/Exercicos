valorcasa = float (input ('Qual o valor do imóvel: '))   
salario = float (input ('Qual a sua renda mensal: '))
tempo = int (input ('Em quanto anos pretende quitar o imóvel: '))

quantidadeparcelas = tempo*12
valorparcelas = valorcasa/quantidadeparcelas

if valorparcelas <= (salario*0.30):
    print('Empréstimo liberado')
    
    print('\nValor do imóvel: {}'.format(valorcasa))
    print('\nSalário: {}'.format(salario))
    print('\nQuantidades de pacelas: x{}'.format(quantidadeparcelas))
    print('\nValor das parcelas: R${:.2f}'.format(valorparcelas))

else :
    print('Empréstimo negado')

