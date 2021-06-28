import random
import time
print('-='*30)
print('Vou pensar em um numero entre 0 e 5. Tente adivinhar...')
print('-='*30)
num = int(input('Em que numero eu pensei? ')) 
print('Processando...')
time.sleep(2)
cpu = random.randint(0, 5)
if cpu != num:
    print(f'GANHEI!Eu pensei no numero {cpu} e não no {num}')
else:
    print(f'PARABÉNS!!Você conseguiu me vencer!')
