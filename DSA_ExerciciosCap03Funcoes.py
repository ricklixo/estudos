import pandas as pd
# Exercício 1 - Crie uma função que imprima a sequência de números pares entre 1 e 20 (a função não recebe parâmetro) e
# depois faça uma chamada à função para listar os números
# MINHA SOLUÇÃO
def pares():
    for i in range(0,21):
        if i % 2 == 0:
            print(i)
pares()

# SOLUÇÃO DO PROFESSOR
def pares():
    for i in range(0, 21, 2):
        print(i)
pares()

# Exercício 2 - Crie uam função que receba uma string como argumento e retorne a mesma string em letras maiúsculas.
# Faça uma chamada à função, passando como parâmetro uma string
# MINHA SOLUÇÃO - CORRIGIDA.
def maiuscula(text):
    print(text.upper())
    return

maiuscula('essa frase deverá ser escrita em caixa alta.')

# SOLUÇÃO DO PROFESSOR - melhor
def maiuscula(texto):
    print(texto.upper())
    return

maiuscula('Rumo a analise de dados...')

# Exercício 3 - Crie uma função que receba como parâmetro uma lista de 4 elementos, adicione 2 elementos a lista e
# imprima a lista

# MINHA SOLUÇÃO - ERREI, CORRIGI.
def listagem(lista):
    lista.append(5)
    lista.append(6)

lista1 = [1, 2, 3, 4]
listagem(lista1)
print(lista1)


# SOLUÇÃO DO PROFESSOR
def listagem(lista):
    lista.append(5)
    lista.append(6)

lista1 = [1, 2, 3, 4]
listagem(lista1)
print(lista1)

# Exercício 4 - Crie uma função que receba um argumento formal e uma possível lista de elementos. Faça duas chamadas
# à função, com apenas 1 elemento e na segunda chamada com 4 elementos

# MINHA SOLUÇÃO
def variada( arg1, *vartuple): # tupla com valores variados.
    print('O valor passado foi {}'.format(arg1))

    for item in vartuple:
        print('O valor passado foi {}'.format(item))

variada('Valor Único')
variada('Valor UM', 'Valor DOIS', 'Valor TRÊS')


# SOLUÇÃO DO PROFESSOR
def printNum(arg1, *lista):
    print(arg1)
    for i in lista:
        print(i)
    return;
# chamada à função
printNum(100)
printNum('A', 'B', 'C')


# Exercício 5 - Crie uma função anônima e atribua seu retorno a uma variável chamada soma. A expressão vai receber 2
# números como parâmetro e retornar a soma deles

# MINHA SOLUÇÃO
soma = lambda x, y: x+y
print(soma(3, 4))

# SOLUÇÃO DO PROFESSOR

soma2 = lambda arg1, arg2: arg1 + arg2
print('A Soma é: {}'.format(soma(452, 298)))



# Exercício 6 - Execute o código abaixo e certifique-se que compreende a diferença entre variável global e local

# MINHA SOLUÇÃO
total = 800 #variavel que percorre o código
def soma( arg1, arg2 ):
    total1 = arg1 + arg2; #variável local. Não é boa prática ter dois nomes iguais.
    print ("Dentro da função o total é: ", total1)
    return total1;

soma( 10, 20 );
print ("Fora da função o total é: ", total)



# Exercício 7 - Abaixo você encontra uma lista com temperaturas em graus Celsius
# Crie uma função anônima que converta cada temperatura para Fahrenheit
# Dica: para conseguir realizar este exercício, você deve criar sua função lambda, dentro de uma função
# (que será estudada no próximo capítulo). Isso permite aplicar sua função a cada elemento da lista
# Como descobrir a fórmula matemática que converte de Celsius para Fahrenheit? Pesquise!!!

# MINHA SOLUÇÃO
Celsius = [39.2, 36.5, 37.3, 37.8]
Fahrenheit = map(lambda x: x * 1.8 + 32, Celsius) #aplica a aformula a casa elemento da lista. AGORA ENTENDI
print (list(Fahrenheit))


# SOLUÇÃO DO PROFESSOR
Celsius = [39.2, 36.5, 37.3, 37.8]
Fahrenheit = map(lambda x: float(9)/5 * x + 32, Celsius) #aplica a aformula a casa elemento da lista. AGORA ENTENDI
print (list(Fahrenheit))

# Exercício 8
# Crie um dicionário e liste todos os métodos e atributos do dicionário

# MINHA SOLUÇÃO
dic1 = {'key1': 'Python', 'key2': 13, 'key3': 45.3}
print(dir(dic1))

# SOLUÇÃO DO PROFESSOR


# Exercício 9
# Abaixo você encontra a importação do Pandas, um dos principais pacotes Python para análise de dados.
# Analise atentamente todos os métodos disponíveis. Um deles você vai usar no próximo exercício.
print(dir(pd))

# ************* Desafio ************* (pesquise na documentação Python)

# Exercício 10 - Crie uma função que receba o arquivo abaixo como argumento e retorne um resumo estatístico descritivo
# do arquivo. Dica, use Pandas e um de seus métodos, describe()
# Arquivo: "binary.csv"
# MINHA SOLUÇÃO
file_name = "binary.csv"

def arquivo(file_name):
    data = pd.read_csv(file_name)
    desc = data.describe()
    print(desc)

arquivo(file_name)

# SOLUÇÃO DO PROFESSOR
def retornaArq(file_name):
    df = pd.read_csv(file_name)
    return df.describe()

print(retornaArq(file_name))