# Exercício 1 - Imprima na tela os números de 1 a 10. Use uma lista para armazenar os números.
ex01 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('Resposta01: ')
for i in ex01:
    print(i)

# Exercício 2 - Crie uma lista de 5 objetos e imprima na tela
ex02 = ['Abacaxi', 'Maçã', 'Pera', 'Uva', 'Laranja']
print('Resposta 02:')
print('Lista de frutas: ')
for i in ex02:
    print(i)

# Exercício 3 - Crie duas strings e concatene as duas em uma terceira string
str1 = 'Patrick'
str2 = 'Dourado'
concat = str1 + ' ' + str2
print('Resposta 03: {} + {} = {}'.format(str1, str2, concat))

# Exercício 4 - Crie uma tupla com os seguintes elementos: 1, 2, 2, 3, 4, 4, 4, 5 e depois utilize a função count do
# objeto tupla para verificar quantas vezes o número 4 aparece na tupla
ex04 = (1, 2, 2, 3, 4, 4, 4, 5)
print('Resposta 04: ')
print('Número de vezes que o número "4" aparece: {}'.format(ex04.count(4)))

# Exercício 5 - Crie um dicionário vazio e imprima na tela
ex05 = {}
print('Resposta 05: ')
print('Imprimindo um dicionário vazio na tela: {}'.format(ex05))

# Exercício 6 - Crie um dicionário com 3 chaves e 3 valores e imprima na tela
ex06 = {'Patrick': 36, 'Mauro': 65, 'Patricio': 38}
print('Resposta 06: ')
print(ex06)

# Exercício 7 - Adicione mais um elemento ao dicionário criado no exercício anterior e imprima na tela
ex07 = ex06
ex07['Cesar'] = 64
print('Resposta 07: ')
print(ex07)

# Exercício 8 - Crie um dicionário com 3 chaves e 3 valores. Um dos valores deve ser uma lista de 2 elementos numéricos.
# Imprima o dicionário na tela.
ex08 = {'key1': 2, 'key2': [0, 1], 'key3': 'Python'}
print('Resposta 08: {}'.format(ex08))
print('Apenas a lista numérica: {}'.format(ex08['key2']))

# Exercício 9 - Crie uma lista de 4 elementos. O primeiro elemento deve ser uma string,
# o segundo uma tupla de 2 elementos, o terceiro um dcionário com 2 chaves e 2 valores e
# o quarto elemento um valor do tipo float.
# Imprima a lista na tela.
ex09 = ['Python', ('Segunda-feira', 'Terça-Feira'), {'key1': 42, 'key2': 'Redrum'}, 1.47]
print('Resposta 09: {}'.format(ex09))

# Exercício 10 - Considere a string abaixo. Imprima na tela apenas os caracteres da posição 1 a 18.
ex10 = 'Cientista de Dados é o profissional mais sexy do século XXI'
print('Resposta 10: {}'.format(ex10[0:18]))

