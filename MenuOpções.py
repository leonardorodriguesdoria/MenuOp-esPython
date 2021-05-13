'''Crie um programa que leia dois valores e mostre um menu
como ao lado da tela:
Seu programa deverá realizar a operação solicitada em cada caso'''
from time import sleep
n1 = int(input('Digite o primeiro valor:'))
n2 = int(input('Digite o seegundo valor:'))
opção = 0
while opção != 5:
    print('''      [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa''')
    opção = input('>>>Digite qual opção deseja executar ?:')
    if opção == 1:
        soma = n1 + n2
        print(f'A soma dos dois números é igual a {soma}')
    elif opção == 2:
        multiplicar = n1 * n2
        print(f'O produto dos dois números é igual a {multiplicar}')
    elif opção == 3:
        if n1 > n2:
            maior =  n1
        else:
            maior = n2
        print(f'Entre {n1} e {n2} o maior é {maior}')
    elif opção == 4:
        print('Informe os números novmanete:')
        n1 = int(input('Primeiro Valor:'))
        n2 = int(input('Segundo Valor:'))
    elif opção == 5:
        print('Finalizando....')
    else:
        print('Opção inválida.Tente Novamente')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa. Volte Sempre1')