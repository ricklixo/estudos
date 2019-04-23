# Definindo uma função - 3 linhas de código

def potencia(num):
    result = num**2
    return result

print(potencia(4))

# Definindo uma função - 2 linhas de código
def potencia(num):
    return num ** 2

print(potencia(5))

# Definindo uma função - 1 linha de código

def potencia(num): return num ** 2

print(potencia(3))

# Definindo uma expressão lambda
potencia = lambda num: num ** 2

print(potencia(9))

# Lembre: operadores de comparação retornam boolean, true or false
par = lambda x: x%2 == 0
print(par(3))
print(par(4))

# Utilizando strings
first = lambda s: s[0]
print(first('Patrick'))

# Invertendo a string
reverse = lambda r: r[::-1]
print(reverse('Patrick'))

# Operação de adição
addnum = lambda x, y: x+y
print(addnum(5, 2))

