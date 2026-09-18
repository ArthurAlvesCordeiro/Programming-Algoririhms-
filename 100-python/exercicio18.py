PreimeiroNumero = int(input("Digite o primeiro número: "))
SegundoNumero = int(input("Digite o segundo número: "))

if PreimeiroNumero > SegundoNumero:
    print(f"O primeiro número {PreimeiroNumero} é maior que o segundo número {SegundoNumero}.")
elif SegundoNumero > PreimeiroNumero:
    print(f"O segundo número {SegundoNumero} é maior que o primeiro número {PreimeiroNumero}.")
else:
    print(f"Os números {PreimeiroNumero} e {SegundoNumero} são iguais.")    