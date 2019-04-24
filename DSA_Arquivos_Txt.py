texto = 'Cientista de Dados é a profissão que mais tem crescido em todo o mundo\n'
texto = texto + 'Esses profissionais precisam se especializar em Programação, Estatística e Machine Learning'
texto += 'E claro, Big Data'

print(texto)

# Importando o módulo OS
import os

# Criando um arquivo
arquivo = open(os.path.join('arquivos/cientista.txt'), 'w')
