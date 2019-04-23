tupla1 = ('Geografia', 23, 'Elefantes')

print('Imprimindo a tupla 1: {}'.format(tupla1))

# TUPLAS NÃO SUPORTAM APPEND

# TUPLAS NÃO SUPORTAM A OPÇÃO DELETE

# CONVERTER A TUPLA PARA UMA LISTA
lista_tupla1 = list(tupla1)

print('A tupla convertida em lista: {}'.format(lista_tupla1))

# Adicione os elementos que desejar
lista_tupla1.append(55)

# CONVERTA A LISTA EM TUPLA NOVAMENTE
tupla1 = tuple(lista_tupla1)

print('Imprimindo a tupla atualizada: {}'.format(tupla1))

