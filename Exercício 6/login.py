login = input('Insira o login abaixo:\n>> ')

tentativas = 4
if login == 'admin':
    while tentativas > 0:
       senha = input('Senha: ')
       if senha == 'admin123':
           print('Acesso permitido!')
           break
       else:
           
           tentativas -= 1
           print(f'Senha incorreta... Sobram {tentativas} tentativas')
    else:
        print('Tentativas esgotadas. Acesso negado.')
else:
    print('Acesso negado. Dados de login incorretos.')