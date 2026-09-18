print("TIPO DE TRIÂNGULO")
print()

a = float(input("Digite o primeiro lado: "))
b = float(input("Digite o segundo lado: "))
c = float(input("Digite o terceiro lado: "))

# Primeiro verifica se pode formar um triângulo
if a < b + c and b < a + c and c < a + b:

    # Verifica o tipo do triângulo
    if a == b and b == c:
        print()
        print("RESULTADO: EQUILÁTERO")

    elif a == b or a == c or b == c:
        print()
        print("RESULTADO: ISÓSCELES")

    else:
        print()
        print("RESULTADO: ESCALENO")

else:
    print()
    print("RESULTADO: NÃO FORMA TRIÂNGULO")