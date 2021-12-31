aluno = {}
aluno['nome'] = input('Digite o nome: ')
aluno['media'] = float(input('Digite a média do aluno: '))
if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovação'
elif 5 <= aluno['media'] < 7:
    aluno['situacao'] = 'Recuperação'
else:
    aluno['situacao'] = 'Reprovação'
print(30 * '-')
for v, k in aluno.items():
    print(f' ¨ {v} : {k}')

