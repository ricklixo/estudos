# Abrindo o arquivo para leitura
arq1 = open('arquivos/arquivo2.txt', 'r')

# Lendo o arquivo
print(arq1.read())

# Contar o número de caracteres
print(arq1.tell())

# Retornar para o início do arquivo
print(arq1.seek(0,0))

# Ler os primeiros 10 caracteres
print(arq1.read(10))

# Abrindo arquivo para gravação#

arq2 = open('arquivos/arquivo1.txt', 'w')

# Gravando arquivo
arq2.write('Patrick está testando gravação de arquivos em Python')
print('Gravando {} caracteres...'.format(arq2.tell()))

# Fechando arquivo
arq2.close()

# Lendo o arquivo gravado
arq2 = open('arquivos/arquivo1.txt', 'r')

print(arq2.read())

# Acrescentando conteúdo
arq2 = open('arquivos/arquivo1.txt', 'a')
arq2.write('\nAcrescentando conteúdo')
arq2.close()
arq2 = open('arquivos/arquivo1.txt', 'r')
print(arq2.read())





