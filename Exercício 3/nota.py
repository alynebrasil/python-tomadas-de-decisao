while True:
    try:
        nota = int(input('Digite uma nota de 0 a 10: '))

        if 0 <= nota <= 10:
            print('Muito obrigada pela nota. Até a próxima!')
            break
        else:
            print('Número inválido. Tente novamente...')
    except:
        print('A entrada não é válida, por favor, insira um número válido.')