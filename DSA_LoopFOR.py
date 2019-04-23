tp = (1, 2, 3, 4)
for i in tp:
    print(i)

listamercado = ['Leite', 'Pão', 'Café']
for i in listamercado:
    print(i)

for contador in range(0, 11):
    print(contador)

#verificar numeros pares
numero = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numero:
    if num % 2 == 0:
        print(num)


#LOOPS ANINHADOS

for i in range(0, 5):
    for a in range(0,5):
        print(a)


listab = [32, 53, 85, 10, 15, 17, 19]
soma = 0
count = 0
for i in listab:
    count += 1
    duplo_i = i * 2
    soma += duplo_i
    print(duplo_i)
print('total da soma: {}'.format(soma))
print('total de elementos: {}'.format(count))


# Contando o número de colunas
lst = [[1, 2 , 3], [3, 4, 5], [5, 6, 7]]
primeira_linha = lst[0]
count = 0
for coluna in primeira_linha:
    count += 1
print('Total de elementos na primeira linha: {}'.format(count))

# Pesquisando em listas
listac = [5, 6, 7, 8, 9, 10]
for i in listac:
    if i == 8:
        print('Numero encontrado na lista!!')

# Listando as chaves de um dicionário
dict = {'k1': 'Python', 'k2':'R', 'k3':'Scala'}
for item in dict:
    print(item)

#Imprimindo a chave e valor do dicionário utilizando o método items() para retornar itens
for k, v in dict.items():
    print(k, v)

# IMPRIMINDO CADA ELEMENTO DE UMA LISTA
lista = ['Uva', 'Banana', 'Maçã', 'Laranja', 'Abacaxi']
lista_size = len(lista)
for i in range(0, lista_size):
    print(lista[i])
