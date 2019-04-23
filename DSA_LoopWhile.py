# Usando o loop while apra imprimir os valores de 0 a 9
counter = 0
while counter < 10: #condição enquanto for verdadeira
    print(counter)
    counter += 1

# Também é possível usar a claúsula else para encerrar o loop while

x = 0
while x < 10:
    print ('O valor de x nesta iteração é {}'.format(x))
    print(' X ainda é menor que 10, somando 1 a x')
    x += 1

else:
    print('O valor de x nesta iteração é 10')
    print('Loop Concluído!!')

