# Exercício 1 - Crie uma estrutura que pergunte ao usuário qual o dia da semana. Se o dia for igual a Domingo ou
# igual a sábado, imprima na tela "Hoje é dia de descanso", caso contrário imprima na tela "Você precisa trabalhar!"
'''
dia = str(input('Digite o dia da semana: ')).title()
if dia == 'Segunda':
    print('Hoje é {}-Feira! Você precisa trabalhar!'.format(dia))
elif dia == 'Terça':
    print('Hoje é {}-Feira! Você precisa trabalhar!'.format(dia))
elif dia == 'Quarta':
    print('Hoje é {}-Feira! Você precisa trabalhar!'.format(dia))
elif dia == 'Quinta':
    print('Hoje é {}-Feira! Você precisa trabalhar!'.format(dia))
elif dia == 'Sexta':
    print('Hoje é {}-Feira! Você precisa trabalhar!'.format(dia))
elif dia == 'Sábado':
    print('Hoje é {}. Dia de descanso!'.format(dia))
elif dia == 'Domingo':
    print('Hoje é {}! Dia supremo de descanso!'.format(dia))
else:
    print('Dia inválido!!!')
'''

# Exercício 2 - Crie uma lista de 5 frutas e verifique se a fruta 'Morango' faz parte da lista
frutas = ['Uva', 'Maçã', 'Morango', 'Melancia', 'Limão']
for fruta in frutas:
    if fruta == 'Morango':
        print('A fruta {} está presente na lista!'.format(fruta))


# Exercício 3 - Crie uma tupla de 4 elementos, multiplique cada elemento da tupla por 2 e guarde os resultados em uma
# lista
tupla1 = (4, 6, 2, 5)
lista2 = []
print(tupla1)
for i in tupla1:
    duploi = i * 2
    lista2.append(duploi)
print(lista2)

# Exercício 4 - Crie uma sequência de números pares entre 100 e 150 e imprima na tela
for i in range(100, 151):
    if i % 2 == 0:
        print(i)

# Exercício 5 - Crie uma variável chamada temperatura e atribua o valor 40. Enquanto temperatura for maior que 35,
# imprima as temperaturas na tela
'''temperatura = 40
while temperatura > 35:
    print('O valor da temperatura é igual a {}'.format(temperatura))
    print('A temperatura está baixando...')
    temperatura -= 1
else:
    print('A temperatura é de 35 graus e está estável.')'''

# Exercício 6 - Crie uma variável chamada contador = 0. Enquanto counter for menor que 100, imprima os valores na tela,
# mas quando for encontrado o valor 23, interrompa a execução do programa
'''contador = 0
while contador < 100:
    if contador == 23:
        break
    else:
        pass
    contador += 1
    print(contador)'''

# Exercício 7 - Crie uma lista vazia e uma variável com valor 4. Enquanto o valor da variável for menor ou igual a 20,
# adicione à lista, apenas os valores pares e imprima a lista
lista3 = []
var4 = 4
while var4 <= 20:
    if var4 % 2 == 0:
        lista3.append(var4)
    var4 += 1
print(lista3)

# Exercício 8 - Transforme o resultado desta função range em uma lista: range(5, 45, 2)
# Solução do professor
nums = range(5, 45, 2)
print(list(nums))

# Minha solução
lista4 = []
for i in range(5, 45, 2):
    lista4.append(i)
print(lista4)


# Exercício 9 - Faça a correção dos erros no código abaixo e execute o programa. Dica: são 3 erros.
'''temperatura = float(input('Qual a temperatura? '))
if temperatura > 30:
    print('Vista roupas leves.')
else:
    print('Busque seus casacos.')'''


# Exercício 10 - Faça um programa que conte quantas vezes a letra "r" aparece na frase abaixo. Use um placeholder na
# sua instrução de impressão

frase = "É melhor, muito melhor, contentar-se com a realidade; se ela não é tão brilhante como os sonhos, tem pelo menos a vantagem de existir."

# MINHA SOLUÇÃO - ERRADA
contagem = frase.find('r')
print('A letra "R" aparece {} vezes na frase'.format(contagem))

# SOLUÇÃO DO PROFESSOR
count = 0
for caracter in frase:
    if caracter == 'r':
        count += 1
print('O caracter "r" aparece {} vezes na frase.'.format(count))