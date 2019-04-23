# AUTOMATIZANDO O PROCESSO DE GRAVAÇÃO
'''fileName = input('Digite o nome do arquivo: ')

fileName = fileName + '.txt'

arq3 = open('arquivos/{}'.format(fileName), 'w')

frase = input('Digite o texto: ')

arq3.write(frase)
arq3.close()
arq3 = open('arquivos/{}'.format(fileName), 'r')
print(arq3.read())'''

# ABRINDO UM DATA SET EM UMA ÚNICA LINHA
f = open('arquivos/salarios.csv', 'r')

data = f.read()

rows = data.split('\n')

print(rows)

# Dividindo um dataset em colunas

f = open('arquivos/salarios.csv', 'r')
data = f.read()
rows = data.split('\n') #separa o texto em cada tecla ENTER pressionada
full_data = [] #cria uma lista vazia

for row in rows: #cria um loop para verificar o to do o texto presente no arquivo.
    split_row = row.split(',') #utiliza a separação por virgulas para atribuir cada valor a uma coluna. NEM SEMPRE A VIRGULA É O SEPARADOR
    full_data.append(split_row) #adiciona os valores já separados acima à lista vazia.

    primeira_linha = full_data[0] #atribui as colunas contidas nas linhas da lista FULL DATA à variável. SEMPRE COMEÇA DO 0 = COLUNA 1.

print(full_data)

# CONTANDO AS LINHAS DE UM ARQUIVO
count_linha = 0
for row in full_data: #checa cada linha contida na lista
    count_linha += 1

print('Número de linhas: {}'.format(count_linha))

#CONTANDO AS COLUNAS DE UM ARQUIVO
count_coluna = 0
for coluna in primeira_linha: #checa cada coluna contida na lista
    count_coluna += 1

print('Número de colunas: {}'.format(count_coluna))

