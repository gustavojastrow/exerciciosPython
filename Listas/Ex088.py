from random import randint
try:
    temp = []
    lista = []
    print('=' * 40)
    print(f"{'Gerador de jogos - MEGA SENA' : ^40}")
    print('=' * 40)
    jogos = int(input('Quantidade de jogos a serem gerados: '))
    print()
    total = 0

    while total < jogos:
        contador = 0
        while True:
            numero = randint(1,60)
            if numero not in temp:
                temp.append(numero)
                contador +=1
            if contador >= 6:
                break
        temp.sort()
        lista.append(temp[:])
        temp.clear()
        total += 1
    for i, l in enumerate(lista):
        print(f'Jogo {i+1}: {l}')
except Exception as erro:
    print(f'Erro: {erro}')

