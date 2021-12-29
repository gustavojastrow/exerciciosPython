lista = [[], []]
valor = 0
try:
    for i in range(0, 7):
        valor = int(input('Digite um valor: '))
        if valor % 2 == 0:
            lista[0].append(valor)
        else:
            lista[1].append(valor)
    lista[0].sort()
    lista[1].sort()
    print(f'Valores pares: {lista[0]}')
    print(f'Valores ímpares: {lista[1]}')
except Exception as erro:
    print(f'Erro: {erro}')