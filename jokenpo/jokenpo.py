import random
import time
print('.*.*'*20)
opcoes = ['PEDRA','PAPEL','TESOURA']
opch = int(input('Qual você escolhe:\n1-PEDRA\n2-PAPEL\n3-TESOURA\n>>> '))
if opch == 1 :
    opch ='PEDRA'
elif opch == 2:
    opch = 'PAPEL'
else:
    opch = 'TESOURA'

jogo = random.choice(opcoes)

print('JO')
time.sleep(0.5)
print('KEN')
time.sleep(0.5)
print('PO')
time.sleep(0.5)
print('.*.*'*20)

print('VOCÊ ESCOLHEU {}'.format(opch))

if opch == jogo:
    print('EU ESCOLHI {}\nEMPATE'.format(jogo))

elif (opch == 'PEDRA' and jogo == 'TESOURA') or (opch == 'PAPEL' and jogo == 'PEDRA')\
      or (opch == 'TESOURA' and jogo == 'PAPEL'):
    print('EU ESCOLHI {}\n\033[32mVOCÊ GANHOU\033[;m'.format(jogo))
else:
    print('EU ESCOLHI {}\n\033[31mVOCÊ PERDEU\033[;m'.format(jogo))

print('.*.*'*20)

