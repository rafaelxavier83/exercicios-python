import random
# print('-='*30)
# print('VAMOS JOGAR PAR OU IMPAR')
# print('-='*30)
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = random.randint(0, 10)
    soma = jogador + computador
    tipo = ' '
    while tipo not in 'PpIi':
        tipo = input('Par ou Impar? [P/I] ')
    print(f'Vôce jogou {jogador} e o computador {computador}. Total de {soma} ', end='')
    print('Deu PAR' if soma % 2 == 0 else 'Deu IMPAR')
    if tipo == 'Pp':
        if soma % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'Ii':
        if soma % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')     
print(f'GAME OVER! Você venceu {v} vezes.')  

