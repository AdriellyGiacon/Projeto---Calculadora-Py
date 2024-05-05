import os 
os.system ('cls')
from colorama import init, Fore, Back
init()

print(Back.RED+'Calculadora com conversão da base decimal para as bases binário, hexadecimal e octadecimal:')

while True:
    print(Back.RESET +'[1] Conversão da base decimal para a base binário;\n[2] Conversão da base decimal para a base hexadecimal;\n[3] Conversão da base decimal para a base octadecimal;')
    print('[4] Dados do projeto;\n[5] Encerrar.')
    opcao = int(input('Digite uma opção:'))

    if opcao == 1:
        num = int(input(Fore.LIGHTBLACK_EX +'Digite um número inteiro: '))
        converte = ''
        numero = num
        while num> 0:
            c = num %2
            converte = str(c) + converte
            num = num//2
        print(f'O numero {numero} em binario é {converte}')
        input('Enter continua...')

    elif opcao == 2:
        num = int(input(Fore.LIGHTCYAN_EX +'Digite um número inteiro: '))
        converte = ''
        digitos = '0123456789ABCDEF'
        base= 16
        numero = num
        while num> 0:
            c = num%base
            converte = digitos[c] + converte
            num = num//base
        print(f'O numero {numero} em hexadecimal é {converte}')
        input('Enter continua...')

    elif opcao == 3:
        num = int(input(Fore.LIGHTRED_EX+'Digite um número inteiro: '))
        converte = ''
        numero = num
        while num > 0:
            c = num % 8
            converte = str(c) + converte
            num = num // 8
        print(f'O numero {numero} em octadecimal é {converte}')
        input('Enter continua...')

    elif opcao == 4:
       print(Fore.LIGHTMAGENTA_EX+'Curso: Ciência da computação \nComponentes do grupo: Adrielly Molina Giacon // Bruno Pereira Alves // Rafael de Matos Lima.   \nDisciplinas envolvidas: Programação de computadores  \nVersão do aplicativo: 2024 .\n')
       input('Enter continua...\n')

    elif opcao == 5: break

    else:
        print(Fore.RESET +'Opção inválida!!!')
        input('Enter continua...')