NotaUm = float(input("qual a primeira nota?: "))
NotaDois = float(input("qual a segunda nota?: "))
MediaEscolar = float(input("qual a média?: "))
MediaAluno = (NotaUm + NotaDois) / 2

print(f"A média do aluno foi: {MediaAluno}")

if MediaAluno > MediaEscolar:
    print("Parabéns, o aluno foi aprovado.")
else:
    print("Dessa vez o aluno foi reprovado.")
