
lista_total = [['elmo', 'armadura', 'escudo', 'espada'], ['ferro', 'aço', 'ouro', 'diamante'], [1, 2, 3, 4]]

equip = lista_total[0]
mat = lista_total[1]
quant = lista_total[2]

quantia = int(input('Digite a quantidade de itens que deseja (1-4): '))
if quantia == 1:
    quant = quant[0]
elif quantia == 2:
    quant = quant[1]
elif quantia == 3:
    quant = quant[2]
elif quantia == 4:
    quant = quant[3]
else:
    print('Quantidade indisponível')



print('Por favor, gostaria de {} {}(s) de {}'.format(quantia, equip[2], mat[3]))

