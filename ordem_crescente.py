# Ler três números inteiros do usuário
numero1 = int(input('Digite o primeiro número inteiro: '))
numero2 = int(input('Digite o segundo número inteiro: '))
numero3 = int(input('Digite o terceiro número inteiro: '))


if numero2 < numero1:
    numero1, numero2 = numero2, numero1
if numero3 < numero2:
    numero2, numero3 = numero3, numero2
if numero2 < numero1:
    numero1, numero2 = numero2, numero1

# Mostrar os números em ordem crescente
print(f'Números em ordem crescente: {numero1}, {numero2}, {numero3}')
