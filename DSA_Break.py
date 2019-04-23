# Utilizando BREAK e PASS para interromper ou continuar o loop.
counter = 0
while counter < 100:
    if counter == 4:
        break
    else:
        pass
    print(counter)
    counter += 1

# Utilizando continue para pular a letra H e dar prosseguimento a verificação
for verificador in 'Python':
    if verificador == 'h':
        continue
    print(verificador)

# Utilizando os loops While e For juntos para verificar numeros primos:

for i in range (2, 30):
    j = 2
    counter = 0
    while j < i:
        if i % j == 0:
            counter = 1
            j += 1
        else:
            j += 1
    if counter == 0:
        print('{} é um número primo'.format(i))
        counter = 0
    else:
        counter = 0
