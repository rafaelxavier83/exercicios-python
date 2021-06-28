import random
import time
jogada = 'pedra', 'papel','tesoura'
print('''SUAS OPÇÕES:
      [ 0 ] PEDRA
      [ 1 ] PAPEL
      [ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
cpu = random.randint(0, 2)
print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PÔ')
time.sleep(1)
print('-='*12)
print(f'computador jogou: {jogada[cpu]}')
print(f'jogador jogou: {jogada[jogador]}')
print('-='*12)

if cpu == 0: 
    if jogador == 0:
        print('EMPATE')        
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVALIDA')
        
elif cpu == 1: 
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVALIDA')
        
elif cpu == 2: 
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')    
    else:
        print('JOGADA INVALIDA')
