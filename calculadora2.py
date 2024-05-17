# Desenvolva uma calculadora estilo HP.

# Irá solicitar para o usuário informar a opção

# 1 - Adição

# 2- Subtração

# 3 - Multiplicação

# 4 - Divisão

# X - Sair

# Quando escolher uma das opções, irá receber os valores numéricos até o usuário digitar a letra P, posterior a isso exibirá o resultado do calculo escolhido, e voltará para o menu.

# Exemplo comentários e docstring: https://github.com/arielguareschi/algoritmos_dv_2024/blob/main/repeticao/calculadora.py

# Entregar o link do github, não esquecer dos comentários de docstring, comentar o código explicando-o com suas palavras, e respeitar as normas da PEP8.

# Pode ser utilizando while, if, print, input, for, match. Se utilizar funções def nota ZERADA!

# Comentários idênticos em dois ou mais trabalhos nota ZERADA PARA TODOS QUE ESTIVER IGUAL.

#Desenvolvido por Prô Terra - MakerZine
#Para mais detalhes, acesse: https://www.makerzine.com.br

#Peça para o usuario escolher uma opção de conta
opcao = ''
while opcao.upper() != 'X':
    print("Escolha a opção:")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("X - Sair")
#insira os numeros invalidos 
    opcao = input("Opção: ").strip().upper()

    if opcao == 'X':
        print("Saindo...")
        break
    elif opcao not in {'1', '2', '3', '4'}:
        print("Opção inválida! Tente novamente.")
        continue
#pedir para o usuario inseriir um numero valido e digitar o P para processar
    numeros = []
    print("Insira os valores numéricos (digite 'P' para processar):")
    valor = ''
    while valor.upper() != 'P':
        valor = input().strip().upper()
        if valor == 'P':
            break
        try:
            numero = float(valor)
            numeros.append(numero)
        except ValueError:
            print("Valor inválido! Insira um número ou 'P' para processar.")

    if not numeros:
        print("Nenhum número foi inserido. Voltando ao menu.")
        continue
#realização das operações que podem ser escolhidas pelo usuario 
    if opcao == '1':
        resultado = sum(numeros)
        operacao = "Adição"
    elif opcao == '2':
        resultado = numeros[0]
        for num in numeros[1:]:
            resultado -= num
        operacao = "Subtração"
    elif opcao == '3':
        resultado = 1
        for num in numeros:
            resultado *= num
        operacao = "Multiplicação"
    elif opcao == '4':
        resultado = numeros[0]
        for num in numeros[1:]:
            if num == 0:
                print("Erro: Divisão por zero!")
                resultado = None
                break
            resultado /= num
        operacao = "Divisão"
#mostrar ao usuario o resultado da operação 
    if resultado is not None:
        print(f"Resultado da {operacao}: {resultado}")