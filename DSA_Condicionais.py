
#Outro Exemplo

resposta = 'S'

while resposta == 'S':
    disc = str(input('Digite a disciplina: ')).title()
    nota = float(input('Digite a média da disciplina: '))

    if disc == 'Matematica':
        if nota >= 7.0:
            print('Parabéns!! Você foi aprovado em {} com a média {}'.format(disc, nota))
        else:
            print('Você foi reprovado em {}!'.format(disc))
    else:
        print('A disciplina não existe')
    resposta = str(input('Deseja Continuar? [S/N]')).isupper()