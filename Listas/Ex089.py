lista = []
while True:
    nome = input('Nome: ')
    nota1 = float(input('Primeira nota: '))
    nota2 = float(input('Segunda nota: '))
    media = (nota1 + nota2) / 2
    lista.append([nome,[nota1, nota2],media])
    resposta = input('Quer continuar? [S/N]: ')
    if resposta in 'Nn':
        break
    if resposta not in 'Nn' and resposta not in 'Ss':
        print('Erro de digitação!')
print()
print(f'{"Boletim": ^30}')
print('=' * 30)
print(f"{'Número': <10}{'Nome': <10}{'Média':<10}")
for i, n in enumerate(lista):
    print(f'{i:<10}{n[0]:<10}{n[2]:<10.2f}')
while True:
    print('=' * 30)
    opcao = int(input('Mostrar nota de qual aluno? (999 interrompe): '))
    if opcao == 999:
        print('Fim do programa!')
        break
    if opcao <= len(lista) - 1:
        print(f'Notas de {lista[opcao][0]} são {lista[opcao][1]}')


