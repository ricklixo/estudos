
estudantes_lista = ['Mateus', 24, 'Fernanda', 22, 'Tamires', 26, 'Cristiano', 25]
print('Essa é a lista de estudantes: {}'.format(estudantes_lista))

estudantes_dic = {'Mateus': 24, 'Fernanda':22, 'Tamires': 26, 'Cristiano': 25}
print('Esse é o dicionário de estudantes: {}'.format(estudantes_dic))

print('Idade de Mateus: {} anos'.format(estudantes_dic['Mateus']))

estudantes_dic['Pedro'] = 23

print('Esse é o dicionário de estudantes atualizado: {}'.format(estudantes_dic))

print(len(estudantes_dic))

print('Chaves do dicionário: {}'.format(estudantes_dic.keys()))
print('Valores do dicionário: {}'.format(estudantes_dic.values()))
print('Items do dicionário: {}'.format(estudantes_dic.items()))

#criando um novo dicionário
estudantes2 = {'Erika': 28, 'Milton': 26, 'Maria': 27}

#atualiza o dicionário
estudantes_dic.update(estudantes2)

print('Esse é o dicionário de estudantes atualizado: {}'.format(estudantes_dic))

dic1 = {}

dic1['Key one'] = 2
print(dic1)
dic1[8] = 4
print(dic1)
dic1[10] = 'Python'
print('Strings que são chaves, e strings que são valores: {}'.format(dic1))

#EVITE UTILIZAR MESMA STRING COMO CHAVE E COMO VALOR


#a prática abaixo é considerada ideal
dic2 = {'key1': 8, 'key2': 'Big Data', 'key3': 10.5}
print('Imprimindo todo o dicionário 2: {}'.format(dic2))

a = dic2['key1']
b = dic2['key2']
c = dic2['key3']
print('Imprimindo os valores das chaves atribuídos as variáveis a, b e c: {}, {}, {}'.format(a, b, c))

#dicionário de listas
dic3 = {'key1': 1245, 'key2':[22, 45, 576, 34], 'key3':['Leite', 'Maçã', 'Pão', 'Ovos']}

print('Imprimindo um dicionário contendo listas: {}'.format(dic3))

print(dic3['key2'])
print(dic3['key3'][2].upper())
var1 = dic3['key2'][2] - 76
print(var1)

#DICIONÁRIOS ANINHADOS (BASTANTE ESPECÍFICO E NÃO RECOMENDADO)
dic_aninhado = {'key1': {'key2_aninhada':{'key3_aninhada': 'Dicionário aninhado em Python'}}}
print('Exemplo de dicionário aninhado em python: {}'.format(dic_aninhado))













