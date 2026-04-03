from datetime import date
ano = int(input('Ano de Nascimento: '))
idade = date.today().year - ano
print('Sua idade é de {} anos'.format(idade))
if idade < 18 :
    print('Ainda vai se alistar')
    print('Faltam {} anos para o alistamento'.format(18-idade))
elif idade == 18:
    print('Está na hora de se alistar')
elif idade > 18:
    print('Já passou o prazo para alistamento')
    print('Você passou {} anos do prazo'.format(idade-18))
    print('Você deveria ter se alistado no ano de {}'.format(date.today().year - idade + 18))
