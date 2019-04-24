texto = 'Cientista de Dados é a profissão que mais tem crescido em todo o mundo.\n'
texto = texto + 'Esses profissionais precisam se especializar em Programação, Estatística, Machine Learning\n'
texto += 'e claro, Big Data'

#print(texto)

# Importando o módulo OS (OPERATIONAL SYSTEM)
import os

# Criando um arquivo
arquivo = open(os.path.join('arquivos/cientista.txt'), 'w') # caso o arquivo não exista, a linguagem cria automaticamente

# Gravando os dados no arquivo
for palavra in texto.split(): # sem nada entre parenteses separa a string por espaço em branco
    arquivo.write(palavra+' ') # adiciona as palavras e grava no arquivo.

# Fechando o arquivo
arquivo.close()

# Lendo o arquivo
arquivo = open('arquivos/cientista.txt', 'r') # abre o arquivo em modo leitura
conteudo = arquivo.read()
arquivo.close()

#print(conteudo) # imprime o conteúdo na tela.


with open('arquivos/cientista.txt', 'r') as arquivo: # com o arquivo aberto como ARQUIVO,
    conteudo = arquivo.read()  # faça a leitura do arquivo e grave em CONTEUDO

print('Caracteres: {}'.format(len(conteudo)))
print(conteudo)

with open('arquivos/cientista.txt', 'w') as arquivo:
    arquivo.write(texto[:21])
    arquivo.write('\n')
    arquivo.write(texto[:33])

arquivo = open('arquivos/cientista.txt', 'r')
conteudo = arquivo.read()
arquivo.close()
print(conteudo)