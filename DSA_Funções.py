import math

# Definindo uma função
def primeiraFrase():
    print('Hello World')

primeiraFrase()

# Definindo uma função com parâmetro.
def primeiraFunc(nome):
    print('Hello {}'.format(nome))

primeiraFunc('Patrick')

def funcLeitura():
    for i in range(0, 5):
        print('Número {}'.format(str(i)))

funcLeitura()

# Função para somar números
def addNum(firstnum, secondnum):
    print('Primeiro número: {}'.format(firstnum))
    print('Segundo número: {}'.format(secondnum))
    print('Soma dos dois: {}'.format(firstnum+secondnum))

addNum(6, 7)

# Variável Global
var_global = 10

def multiply(num1, num2):
    var_global = num1 * num2 # Esta é uma variável local, pois só existe dentro da função específica
    print(var_global)

# Variável Local
def multiplicacao(num1, num2):
    var_local = num1 * num2
    print(var_local)

print(multiply(5, 3))
print(multiplicacao(5, 3))



def numPrimo(num):
    '''Verificando se o número é primo'''
    if num % 2 == 0 and num > 2:
        return "Este não é um número primo."
    for i in range(3, int(math.sqrt(num))+ 1, 2): #sqrt é uma função do pacote MATH
        if num % i == 0:
            return "Este não é um número primo"
    return "Este número é primo"

print(numPrimo(541))


# Fazendo split dos dados
def split_string(text):
    return text.split(' ')

texto = 'Essa função será bastante útil para análise de dados!'
print(split_string(texto))


# Criando uma função para caixa baixa.
caixabaixa = 'Esta Frase Deveria Estar Em Caixa Baixa.'

def lowercase(text):
    return text.lower()

print(lowercase(caixabaixa))


# Funções com número variável de argumentos

def printVarInfo( arg1, *vartuple): #o asterisco indica que vai receber vários argumentos, que não são conhecidos
    # Imprimindo o valor do primeiro argumento
    print('O parâmetro passado foi: {}'.format(arg1))

    # Imprimindo o valor do segundo argumento, para cada valor passado
    for item in vartuple:
        print('O parâmetro passado foi: {}'.format(item))
    return;

# Fazendo chamada à função usando apenas um argumento
printVarInfo(10)

# Fazendo chamada à função usando vários argumentos
printVarInfo('Chocolate', 'Morango', 'Banana')



