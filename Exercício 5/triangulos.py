lado_a = int(input('Digite o tamanho do primeiro lado: '))
lado_b = int(input('Digite o tamanho do segundo lado: '))
lado_c = int(input('Digite o tamanho do terceiro lado: '))

if lado_a + lado_b > lado_c and lado_a + lado_c > lado_b and lado_b + lado_c > lado_a:
    if lado_a == lado_b == lado_c:
        print('É um triângulo equilátero!')
    elif lado_a==lado_b or lado_b == lado_c or lado_c ==lado_a:
        print('É um triângulo isósceles!')
    else:
        print('É um triângulo escaleno!')
else:
    print('Os lados não fornecem um triângulo')