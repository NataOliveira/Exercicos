a = int(input('cumprimento da primeira reta: '))
b = int(input('cumprimento da segunda reta: '))
c = int(input('cumprimento da terceira reta: '))

if ((a+b)>c) and ((b+c)>a) and ((a+c)>b):
    print('Triangulo feito')
else:
    print('Não é possível')
