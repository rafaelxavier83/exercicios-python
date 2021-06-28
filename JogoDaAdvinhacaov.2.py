import random
cpu = random.randint(0, 10)
print('Sou seu computador')
print('Acabei de pensar em um numero entre 0 e 10.')
print('Sera que você consegue adivinhar qual foi?')
#num = int(input('Qual é seu palpite? ')) 
acertou = False
palpite = 0
while not acertou:
    num = int(input('Qual é seu palpite? '))
    palpite += 1    
    if num > cpu:
        print('Menos...Tente mais uma vez')    
    elif num < cpu:
        print('Mais...Tente mais uma vez')                             
    elif num == cpu:                    
        acertou = True
        
    
print(f'ACERTOU! com {palpite} tentativas, PARABENS!')
