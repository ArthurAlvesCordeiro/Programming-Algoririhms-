NotaUm = float(input("Primeira nota foi : "))
NotaDois = float(input("Segunda nota foi : "))

Media = (NotaUm + NotaDois) / 2

print(f"Sua média foi: {Media:.1f}")

if Media < 5:
    print("Situação: REPROVADO")
elif Media < 7:
    print("Situação: RECUPERAÇÃO")
else:
    print("Situação: APROVADO")