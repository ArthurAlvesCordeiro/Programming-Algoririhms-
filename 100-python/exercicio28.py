print("É POSSÍVEL FORMAR UM TRIÂNGULO?")
print()

a = float(input("Digite o primeiro lado: "))
b = float(input("Digite o segundo lado: "))
c = float(input("Digite o terceiro lado: "))

if a < b + c and b < a + c and c < a + b:
    print()
    print("RESULTADO: FORMAM UM TRIÂNGULO")
else:
    print()
    print("RESULTADO: NÃO FORMAM UM TRIÂNGULO")