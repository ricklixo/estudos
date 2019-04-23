# LAB 02 - PROJETO DE calculadora

continuar = 'S'
while continuar == 'S':
    print('Selecione a operação que deseja realizar.')
    print('1 - SOMA')
    print('2 - SUBTRAÇÃO')
    print('3 - MULTPLICAÇÃO')
    print('4 - DIVISÃO')
    print()
    opcao = int(input('Digite sua opoção: '))
    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo número: '))

    def soma(x, y):
        return x + y

    def subtracao(x, y):
        return x - y

    def divisao(x, y):
        return x // y

    def multiplic(x, y):
        return x * y

    if opcao == 1:
        print('A Soma entre os números {} e {} é igual a {}'.format(num1, num2, soma(num1, num2)))
    elif opcao == 2:
        print('A Subtração entre os números {} e {} é igual a {}'.format(num1, num2, subtracao(num1, num2)))
    elif opcao == 3:
        print('A Multiplicação de {} vezes {} é igual a {}'.format(num1, num2, multiplic(num1, num2)))
    elif opcao == 4:
        print('{} dividido por {} é igual a {}'.format(num1, num2, divisao(num1, num2)))
    else:
        print('Opção inválida.')

    continuar = str(input('Deseja Continuar? [S/N]')).upper()

